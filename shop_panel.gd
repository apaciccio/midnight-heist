# shop_panel.gd - FINESTRA DEL NEGOZIO MONETE - v1.0
# Si crea dal codice:  var p := preload("res://shop_panel.gd").new(); add_child(p)
# Copre lo schermo (blocca i tocchi sotto), mostra i 5 pacchetti del Shop,
# si chiude con la X o toccando fuori. Segnale "chiuso" quando sparisce.
# I testi sono in lang.gd (chiavi shop_*).
extends Control

signal chiuso

const VW := 1152.0
const VH := 648.0
const ORO := Color("#e3b04b")
const ORO_CHIARO := Color("#ffe9a8")
const SCURO := Color("#140d05")

var _msg: Label
var _bottoni := {}     # id -> Button
var shop: Node = null  # autoload /root/Shop (preso a runtime)


func _T(k: String) -> String:
	return Lingue.t(k, Lingue.attiva())


func _ready() -> void:
	shop = get_node_or_null("/root/Shop")
	z_index = 200
	mouse_filter = Control.MOUSE_FILTER_STOP
	size = Vector2(VW, VH)
	position = Vector2.ZERO

	var velo := ColorRect.new()
	velo.color = Color(0, 0, 0, 0.72)
	velo.size = Vector2(VW, VH)
	velo.mouse_filter = Control.MOUSE_FILTER_STOP
	velo.gui_input.connect(func(ev: InputEvent):
		if (ev is InputEventMouseButton and ev.pressed) or (ev is InputEventScreenTouch and ev.pressed):
			chiudi())
	add_child(velo)

	var w := 600.0
	var h := 560.0
	var pannello := Panel.new()
	pannello.size = Vector2(w, h)
	pannello.position = Vector2((VW - w) / 2.0, (VH - h) / 2.0)
	pannello.mouse_filter = Control.MOUSE_FILTER_STOP
	var sb := StyleBoxFlat.new()
	sb.bg_color = Color("#1d1308")
	sb.border_color = ORO
	sb.set_border_width_all(4)
	sb.set_corner_radius_all(22)
	sb.shadow_color = Color(0, 0, 0, 0.7)
	sb.shadow_size = 14
	pannello.add_theme_stylebox_override("panel", sb)
	add_child(pannello)

	var titolo := _etichetta(_T("shop_titolo"), 34, ORO_CHIARO)
	titolo.size = Vector2(w, 50)
	titolo.position = Vector2(0, 16)
	titolo.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	pannello.add_child(titolo)

	var x := Button.new()
	x.text = "✕"
	x.size = Vector2(52, 52)
	x.position = Vector2(w - 64, 12)
	x.add_theme_font_size_override("font_size", 26)
	x.flat = true
	x.add_theme_color_override("font_color", ORO_CHIARO)
	x.pressed.connect(chiudi)
	pannello.add_child(x)

	var y := 82.0
	for pk in (shop.pacchetti() if shop != null else []):
		var riga := Panel.new()
		riga.size = Vector2(w - 48, 66)
		riga.position = Vector2(24, y)
		var sr := StyleBoxFlat.new()
		sr.bg_color = Color("#2b1d0c")
		sr.border_color = Color("#6b4a1c")
		sr.set_border_width_all(2)
		sr.set_corner_radius_all(14)
		riga.add_theme_stylebox_override("panel", sr)
		pannello.add_child(riga)

		var lab := _etichetta("%s %s" % [migliaia(int(pk["monete"])), _T("monete")], 26, ORO_CHIARO)
		lab.position = Vector2(20, 0)
		lab.size = Vector2(300, 66)
		lab.vertical_alignment = VERTICAL_ALIGNMENT_CENTER
		riga.add_child(lab)

		var b := Button.new()
		b.size = Vector2(190, 50)
		b.position = Vector2(riga.size.x - 200, 8)
		b.add_theme_font_size_override("font_size", 22)
		var sn := StyleBoxFlat.new()
		sn.bg_color = ORO
		sn.set_corner_radius_all(12)
		var sh := sn.duplicate(); sh.bg_color = ORO_CHIARO
		var sd := sn.duplicate(); sd.bg_color = Color("#6b5a3a")
		b.add_theme_stylebox_override("normal", sn)
		b.add_theme_stylebox_override("hover", sh)
		b.add_theme_stylebox_override("pressed", sh)
		b.add_theme_stylebox_override("disabled", sd)
		b.add_theme_color_override("font_color", SCURO)
		b.add_theme_color_override("font_hover_color", SCURO)
		b.add_theme_color_override("font_pressed_color", SCURO)
		var id: String = pk["id"]
		b.pressed.connect(func(): _compra(id))
		riga.add_child(b)
		_bottoni[id] = b
		y += 76.0

	_msg = _etichetta("", 20, Color("#ffd27a"))
	_msg.size = Vector2(w - 40, 30)
	_msg.position = Vector2(20, y + 4)
	_msg.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	pannello.add_child(_msg)

	var nota := _etichetta(_T("shop_nota"), 15, Color("#bfa98a"))
	nota.autowrap_mode = TextServer.AUTOWRAP_WORD_SMART
	nota.horizontal_alignment = HORIZONTAL_ALIGNMENT_CENTER
	nota.custom_minimum_size = Vector2(w - 60, 0)
	nota.size = Vector2(w - 60, 44)
	nota.position = Vector2(30, h - 56)
	pannello.add_child(nota)

	if shop != null:
		shop.prodotti_aggiornati.connect(_aggiorna)
		shop.messaggio.connect(_on_messaggio)
	_aggiorna()
	if shop != null and shop.e_prova():
		_msg.text = _T("shop_prova")
	elif shop == null or not shop.disponibile():
		_msg.text = _T("shop_non_disp")

	# entrata morbida
	modulate.a = 0.0
	var tw := create_tween()
	tw.tween_property(self, "modulate:a", 1.0, 0.15)


func _aggiorna() -> void:
	var attivi: bool = shop != null and shop.disponibile()
	for id in _bottoni.keys():
		var b: Button = _bottoni[id]
		b.text = shop.prezzo(id) if shop != null else ""
		b.disabled = not attivi


func _compra(id: String) -> void:
	if shop == null or shop.acquisto_in_corso:
		return
	_msg.text = _T("shop_attendi")
	shop.compra(id)


func _on_messaggio(chiave: String) -> void:
	if is_instance_valid(_msg):
		_msg.text = _T(chiave)


func chiudi() -> void:
	if shop != null:
		if shop.prodotti_aggiornati.is_connected(_aggiorna):
			shop.prodotti_aggiornati.disconnect(_aggiorna)
		if shop.messaggio.is_connected(_on_messaggio):
			shop.messaggio.disconnect(_on_messaggio)
	chiuso.emit()
	queue_free()


func _etichetta(testo: String, dim: int, col: Color) -> Label:
	var l := Label.new()
	l.text = testo
	l.add_theme_font_size_override("font_size", dim)
	l.add_theme_color_override("font_color", col)
	l.add_theme_color_override("font_outline_color", Color(0, 0, 0, 0.8))
	l.add_theme_constant_override("outline_size", 4)
	l.mouse_filter = Control.MOUSE_FILTER_IGNORE
	return l


static func migliaia(n: int) -> String:
	var s := str(n)
	var out := ""
	var c := 0
	for i in range(s.length() - 1, -1, -1):
		out = s[i] + out
		c += 1
		if c % 3 == 0 and i > 0:
			out = "." + out
	return out
