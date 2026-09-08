#!/usr/bin/env python3
"""
verde.py - GREEN SCREEN: estrae con precisione un soggetto disegnato su
fondo VERDE puro (o magenta), conservando aloni, luci e fiamme.
Uso: python3 verde.py <file o cartella> [--out cartella]
     python3 verde.py --tasti <file o cartella>   (tasti SPIN/TURBO/AUTO/MENU/BET)
Il colore del fondo lo stima dai bordi (tollera i verdi non perfetti).
TASTI (v3.72): i file vanno chiamati con la parola chiave nel nome
(spin, turbo_off, turbo_on, auto, stop, menu, bet); escono tasto_*.png e chip_bet.png
ritagliati stretti; TURBO on/off sulla STESSA tela (le fiamme ci stanno) e
ridotti a 512 px. Copiarli in ~/slot-mvp/assets/.
"""
import sys, os, re
import numpy as np
from PIL import Image
from scipy import ndimage

def stima_fondo(rgb):
    # cerco il verde (o il magenta) ovunque nell'immagine, non solo ai bordi
    R, G, B = rgb[...,0], rgb[...,1], rgb[...,2]
    verdi = (G > 90) & (G > R + 40) & (G > B + 40)
    magenta = (R > 140) & (B > 140) & (G < R - 60) & (G < B - 60)
    if verdi.mean() > 0.01 and verdi.sum() >= magenta.sum():
        return np.median(rgb[verdi], axis=0)
    if magenta.mean() > 0.01:
        return np.median(rgb[magenta], axis=0)
    h, w, _ = rgb.shape
    b = np.concatenate([rgb[:10].reshape(-1,3), rgb[-10:].reshape(-1,3), rgb[:, :10].reshape(-1,3), rgb[:, -10:].reshape(-1,3)])
    return np.median(b, axis=0)

def key(path_in, path_out, intero=False, riempi=False, personaggio=False, specchia=False):
    rgb = np.asarray(Image.open(path_in).convert("RGB")).astype(np.float32)
    bg = stima_fondo(rgb)
    R, G, B = rgb[...,0], rgb[...,1], rgb[...,2]
    if riempi:
        _riempi(rgb, R, G, B, path_out); return
    img = _key_rgba(rgb, bg)
    _salva(img, path_out, intero, personaggio, specchia)

def _key_rgba(rgb, bg):
    """green screen -> immagine RGBA sulla tela intera (nessun ritaglio)"""
    R, G, B = rgb[...,0], rgb[...,1], rgb[...,2]
    verde = bg[1] > max(bg[0], bg[2]) + 35
    # misura di "verdezza" indipendente dalla luminosita' (regge vignettature e angoli scuri)
    if verde:
        ecc = (G - np.maximum(R, B)) / np.maximum(G, 1.0)
        ecc_bg = (bg[1] - max(bg[0], bg[2])) / max(bg[1], 1.0)
    else:
        ecc = (np.minimum(R, B) - G) / np.maximum(np.minimum(R, B), 1.0)
        ecc_bg = (min(bg[0], bg[2]) - bg[1]) / max(min(bg[0], bg[2]), 1.0)
    a = 1.0 - np.clip(ecc / max(ecc_bg, 0.05), 0, 1)
    # pixel praticamente identici al fondo -> 0
    dist = np.sqrt(((rgb - bg) ** 2).sum(axis=2))
    a = np.where((dist < 18) | (ecc > 0.92 * ecc_bg), 0.0, a)
    A = np.clip(a, 0.02, 1.0)[..., None]
    fg = np.clip((rgb - (1 - A) * bg) / A, 0, 255)
    # despill: via la contaminazione residua del fondo dai bordi
    if verde:
        fg[...,1] = np.minimum(fg[...,1], np.maximum(fg[...,0], fg[...,2]) + 12)
    a = np.clip(a, 0, 1)
    a[a < 0.02] = 0
    # isole
    lab, n = ndimage.label(a > 0.05)
    if n > 1:
        sizes = ndimage.sum(np.ones_like(a), lab, range(1, n+1))
        keep = np.zeros(n+1, bool); keep[1:] = sizes >= 400
        a = np.where(keep[lab], a, 0.0)
    return Image.fromarray(np.dstack([fg, a*255]).astype(np.uint8), "RGBA")

def _riempi(rgb, R, G, B, path_out):
    if True:
        # SFONDI: le zone verdi si RIEMPIONO coi colori vicini (soffitto/pavimento), niente trasparenza
        # buco = SOLO il verde vero (non i grigi verdastri della scena); colori originali intatti
        buco = (G > 140) & (G > R + 60) & (G > B + 60)
        buco_l = ndimage.binary_dilation(buco, iterations=10)
        idx = ndimage.distance_transform_edt(buco_l, return_distances=False, return_indices=True)
        pieno = rgb.copy()
        pieno[buco_l] = rgb[idx[0][buco_l], idx[1][buco_l]]
        for c in range(3):
            sm = ndimage.gaussian_filter(pieno[..., c], 30)
            pieno[..., c] = np.where(buco_l, sm, pieno[..., c])
        # ombra naturale: le zone riempite sono soffitto/pavimento, piu' scure
        dist = ndimage.distance_transform_edt(buco_l)
        ombra = 1.0 - 0.45 * np.clip(dist / 60.0, 0, 1)
        pieno = pieno * ombra[..., None]
        Image.fromarray(np.clip(pieno, 0, 255).astype(np.uint8), "RGB").save(path_out); return

def _salva(img, path_out, intero=False, personaggio=False, specchia=False):
    if personaggio:
        # FRAME DEL MASTERMIND: ritaglio FISSO identico per tutti i frame (niente salti),
        # box 904x1004 su tela 1024: ci stanno anche le braccia spalancate (nodo 396x460)
        W, H = img.size
        sx, sy = W / 1024.0, H / 1024.0
        box = (int(60*sx), int(10*sy), int(964*sx), int(1014*sy))
        out = img.crop(box)
        if specchia:
            from PIL import ImageOps
            out = ImageOps.mirror(out)
        out.save(path_out); return
    if intero:
        # targhe e cornici: via i margini vuoti, ma NIENTE quadrato (proporzioni intatte)
        bb = img.getbbox()
        if bb: img = img.crop(bb)
        img.save(path_out); return
    bb = img.getbbox()
    if bb: img = img.crop(bb)
    w, h = img.size; s = max(w, h) + 40
    canvas = Image.new("RGBA", (s, s), (0,0,0,0)); canvas.paste(img, ((s-w)//2, (s-h)//2), img)
    canvas.save(path_out)

CHIAVI = [("turbo_on","tasto_turbo_on.png"),("turbo_off","tasto_turbo_off.png"),("turbo","tasto_turbo_off.png"),
          ("spin","tasto_spin.png"),("auto","tasto_auto.png"),("stop","tasto_stop.png"),("menu","tasto_menu.png"),("bet","chip_bet.png"),
          ("dinamite","symbols/dinamite.png"),("chiusa","scasso_cassaforte_chiusa.png"),("aperta","scasso_cassaforte_aperta.png"),
          ("crepato","diamante_crepato.png"),("frammento","frammento.png"),("diamante","diamante.png"),("polizia","scasso_polizia.png"),
          ("lucchetto","scasso_lucchetto.png"),("talk","mastermind_talk.png"),("lancio","mastermind_lancio.png"),("furia","mastermind_furia.png"),("disco","disco_cassaforte.png"),("lancio","mastermind_lancio.png"),("furia","mastermind_furia.png"),("disco","disco_cassaforte.png"),("med_frame","med_frame.png"),("scena","banner_scena.png"),("plate","sacco_plate.png"),("sacco","sacco_plate.png"),("jackpot","targa_jackpot.png"),("targa","banner_targa.png"),("sfondo","sfondo_colpo.png")]
def nome_gioco(n):
    n = n.lower()
    m = re.search(r"(idle|win)[ _-]?(\d)", n)
    if m: return f"mastermind_{m.group(1)}_{m.group(2)}.png"
    for k, v in CHIAVI:
        if k in n: return v
    return os.path.splitext(os.path.basename(n))[0] + ".png"

def _bbox_alpha(img, soglia=25):
    a = np.asarray(img)[..., 3]
    ys, xs = np.where(a > soglia)
    if len(xs) == 0: return None
    return (int(xs.min()), int(ys.min()), int(xs.max()) + 1, int(ys.max()) + 1)

def _pulisci_bagliore(img, rgb, bg, corpo=None):
    """Fiamme/bagliori che sfumano nel verde. Nella zona verdastra (fuori dal
    corpo del tasto) l'opacita' viene ricavata dal canale ROSSO, che il fondo
    verde non ha: piu' rosso = piu' bagliore. Poi il colore viene smiscelato
    dal fondo e tenuto nella gamma del fuoco (niente giallo-verde)."""
    a = np.asarray(img).astype(np.float32)
    R, G, B = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    ecc = (G - np.maximum(R, B)) / np.maximum(G, 1.0)
    zona = ecc > 0.04                       # pixel ancora tinti di verde = alone
    if corpo is not None:
        # stessa tela del tasto spento: tutto cio' che sta FUORI dal corpo e' fiamma/bagliore
        zona = zona | ~ndimage.binary_dilation(corpo, iterations=6)
    A = np.clip((R - bg[0]) / max(235.0 - bg[0], 1.0), 0, 1) ** 1.25
    A3 = np.clip(A, 0.02, 1.0)[..., None]
    fg = np.clip((rgb - (1 - A3) * bg) / A3, 0, 255)
    fg[..., 1] = np.minimum(fg[..., 1], fg[..., 0] * 0.62)   # gamma del fuoco
    fg[..., 2] = np.minimum(fg[..., 2], fg[..., 0] * 0.25)
    out = a.copy()
    out[..., :3] = np.where(zona[..., None], fg, a[..., :3])
    out[..., 3] = np.where(zona, np.minimum(a[..., 3], A * 255.0), a[..., 3])
    # anche fuori dalla zona verde il verde non deve mai dominare
    out[..., 1] = np.minimum(out[..., 1], np.maximum(out[..., 0], out[..., 2]) + 6)
    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8), "RGBA")

def tasti(files, out, lato_max=512):
    """TASTI ILLUSTRATI: ritaglio stretto; TURBO on/off sulla stessa tela centrata sul corpo."""
    os.makedirs(out, exist_ok=True)
    imgs = {}
    for f in files:
        nome = nome_gioco(os.path.basename(f))
        rgb = np.asarray(Image.open(f).convert("RGB")).astype(np.float32)
        bg = stima_fondo(rgb)
        imgs[nome] = (_key_rgba(rgb, bg), f, rgb, bg)
    boxes = {}
    off = imgs.get("tasto_turbo_off.png"); on = imgs.get("tasto_turbo_on.png")
    if on is not None:
        corpo = None
        if off is not None and off[0].size == on[0].size:
            corpo = np.asarray(off[0])[..., 3] > 128
        imgs["tasto_turbo_on.png"] = (_pulisci_bagliore(on[0], on[2], on[3], corpo), on[1], on[2], on[3])
        on = imgs["tasto_turbo_on.png"]
    if off is not None and on is not None:
        bo = _bbox_alpha(off[0]); bf = _bbox_alpha(on[0], 12)
        if bo and bf:
            cx = (bo[0] + bo[2]) / 2.0; cy = (bo[1] + bo[3]) / 2.0
            hw = max(cx - bf[0], bf[2] - cx, (bo[2] - bo[0]) / 2.0) + 4
            hh = max(cy - bf[1], bf[3] - cy, (bo[3] - bo[1]) / 2.0) + 4
            box = (int(round(cx - hw)), int(round(cy - hh)), int(round(cx + hw)), int(round(cy + hh)))
            boxes["tasto_turbo_off.png"] = box; boxes["tasto_turbo_on.png"] = box
            print("TURBO: corpo %s, tela comune %s (tela/corpo = %.3f)" % (bo, box, (box[2]-box[0]) / float(bo[2]-bo[0])))
    for nome, (img, f, _rgb, _bg) in imgs.items():
        box = boxes.get(nome) or _bbox_alpha(img)
        if box is None:
            print("ATTENZIONE: soggetto non trovato in", f); continue
        # crop tollera un box fuori tela: il fuori resta trasparente
        W, H = img.size
        tela = Image.new("RGBA", (box[2] - box[0], box[3] - box[1]), (0, 0, 0, 0))
        tela.paste(img.crop((max(box[0], 0), max(box[1], 0), min(box[2], W), min(box[3], H))), (max(0, -box[0]), max(0, -box[1])))
        w, h = tela.size
        if max(w, h) > lato_max:
            sc = lato_max / float(max(w, h))
            tela = tela.resize((max(1, int(round(w * sc))), max(1, int(round(h * sc)))), Image.LANCZOS)
        dst = os.path.join(out, nome)
        tela.save(dst); print("ok ->", dst, tela.size)

if __name__ == "__main__":
    argv = sys.argv[1:]; out = "puliti"
    if "--out" in argv:
        i = argv.index("--out"); out = argv[i+1]; argv = argv[:i] + argv[i+2:]
    intero = "--intero" in argv
    riempi = "--sfondo" in argv
    specchia = "--specchia" in argv
    modo_tasti = "--tasti" in argv
    argv = [x for x in argv if x not in ("--intero", "--sfondo", "--specchia", "--tasti")]
    files = []
    for a in argv:
        files += [os.path.join(a, f) for f in sorted(os.listdir(a)) if f.lower().endswith((".jpg",".jpeg",".png"))] if os.path.isdir(a) else [a]
    if modo_tasti:
        tasti(files, out); sys.exit(0)
    os.makedirs(os.path.join(out, "symbols"), exist_ok=True)
    for f in files:
        nome = os.path.basename(f).lower()
        dst = os.path.join(out, nome_gioco(nome))
        # modalita' automatica dal nome: sfondi si riempiono, targhe/cornici restano intere
        auto_riempi = riempi or ("sfondo" in nome)
        auto_intero = intero or any(k in nome for k in ("scena", "targa", "jackpot", "plate", "frame", "banner"))
        auto_pers = re.search(r"(idle|win)[ _-]?\d", nome) is not None or any(k in nome for k in ("talk", "lancio", "furia"))
        auto_spec = specchia or any(k in nome for k in ("lancio", "furia"))   # Gemini le fa guardare a destra: le giro
        key(f, dst, auto_intero, auto_riempi, auto_pers, auto_spec); print("ok ->", dst)
