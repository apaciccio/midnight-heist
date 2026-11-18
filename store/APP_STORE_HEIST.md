# Midnight Heist – App Store (versione 1.3.0)

Guida da tenere aperta mentre compili App Store Connect. Ogni testo è già nei limiti di Apple.

## 1. Bundle ID (developer.apple.com → Identifiers → +)

- Tipo: **App IDs → App**
- Descrizione: `Midnight Heist`
- Bundle ID: **Explicit** → `com.apaciccio.midnightheist`
- Capabilities: **In-App Purchase** (di solito è già spuntato)

## 2. Nuova app (App Store Connect → App → +)

- Piattaforma: **iOS**
- Nome: `Midnight Heist – Casino Slots` (se è già preso: `Midnight Heist: Vault Slots`)
- Lingua principale: **Inglese (U.S.A.)**
- Bundle ID: `com.apaciccio.midnightheist`
- SKU: `midnightheist`
- Accesso utenti: **Accesso completo**

## 3. Informazioni app

- Categoria principale: **Giochi** → sottocategoria **Casinò**
- Seconda categoria: (vuota)
- Copyright: `2026 Francesco Saverio Prota`
- Diritti sui contenuti: **No, non contiene contenuti di terze parti** (grafica e musiche sono tue)
- URL privacy: `https://apaciccio.github.io/midnight-privacy/`
- URL supporto: `https://apaciccio.github.io/midnight-privacy/`

### Classificazione per età (questionario)

- Gioco d'azzardo **simulato**: **Frequente** → la classificazione esce **18+**
- Gioco d'azzardo con soldi veri: **No**
- Concorsi / premi: **No**
- Loot box / ricompense casuali a pagamento: **No**
- Violenza, linguaggio, sesso, droghe, orrore, contenuti medici: **Nessuno**
- Accesso libero al web / chat tra utenti / contenuti degli utenti: **No**
- Controlli parentali / verifica età nell'app: **No**
- Acquisti in-app: **Sì**

## 4. Privacy dell'app

- **Dati non raccolti** (il gioco non raccoglie niente: gli acquisti li gestisce Apple)

## 5. Prezzo e disponibilità

- Prezzo: **Gratis**
- Paesi: **tutti tranne Cina continentale** (in Cina i giochi richiedono una licenza statale)

## 6. Acquisti in-app (Monetizzazione → Acquisti in-app → +), tipo **Consumabile**

| ID prodotto | Nome di riferimento | Prezzo | Nome mostrato (EN / IT) | Descrizione (EN / IT) |
|---|---|---|---|---|
| `monete_10k` | Coins 10,000 | 0,99 € | 10,000 Coins / 10.000 Monete | 10,000 virtual coins for play / 10.000 monete virtuali per giocare |
| `monete_50k` | Coins 50,000 | 4,99 € | 50,000 Coins / 50.000 Monete | 50,000 virtual coins for play / 50.000 monete virtuali per giocare |
| `monete_150k` | Coins 150,000 | 9,99 € | 150,000 Coins / 150.000 Monete | 150,000 virtual coins for play / 150.000 monete virtuali per giocare |
| `monete_500k` | Coins 500,000 | 24,99 € | 500,000 Coins / 500.000 Monete | 500,000 virtual coins for play / 500.000 monete virtuali per giocare |
| `monete_2m` | Coins 2,000,000 | 49,99 € | 2,000,000 Coins / 2.000.000 Monete | 2,000,000 virtual coins for play / 2.000.000 monete virtuali per giocare |

Per ognuno:
- Disponibilità: tutti i paesi dell'app
- **Screenshot per la revisione**: `iap_review_shop.png` (lo trovi in `~/slot-mvp/store/`), lo stesso per tutti e 5
- Note per la revisione: `Consumable pack of virtual coins. Coins have no real-world value and cannot be cashed out.`
- Lo stato deve diventare **Pronto per l'invio**

## 7. Pagina della versione 1.3.0

- **Screenshot iPhone 6,9"**: carica i 6 file di `~/slot-mvp/store/shots_iphone67/` in quest'ordine: **heist_02, 03, 04, 05, 06, 01** (il primo deve essere il gioco, non il titolo)
- iPad: non serve (l'app è solo per iPhone)
- Build: quella caricata da Xcode (punto 9)
- **Acquisti in-app**: nella sezione "Acquisti in-app e abbonamenti" della versione clicca **+** e seleziona tutti e 5 (fondamentale, altrimenti non vengono inviati)
- Rilascio: **Rilascia manualmente** (così decidi tu quando va online)

### Note per la revisione (Informazioni per la revisione dell'app)

- Accesso richiesto: **No**
- Contatto: nome, telefono, `francescosprota@gmail.com`
- Note:
```
Midnight Heist is a social casino game for entertainment only (18+). There is no real-money gambling: players cannot win money or prizes and virtual coins cannot be withdrawn or exchanged. Coins can be bought through consumable In-App Purchases (StoreKit). Tap the "+" button next to the balance to open the coin shop. No account or login is required; the game works offline.
```

## 8. Testi per lingua

Aggiungi le lingue dal menu in alto a destra della pagina della versione. Campi: Nome (in Informazioni app), Sottotitolo, Testo promozionale, Descrizione, Parole chiave.

### Italiano

**Nome** (28/30)
```
Midnight Heist – Slot Casinò
```
**Sottotitolo** (25/30)
```
Slot casinò con 4 jackpot
```
**Testo promozionale** (121/170)
```
Mezzanotte, un caveau e un Mastermind mascherato: fai girare i rulli, fai saltare la cassaforte e punta al GRAND jackpot.
```
**Parole chiave** (94/100)
```
slot,slot machine,casinò,vegas,jackpot,rapina,caveau,banca,rulli,giri,wild,offline,colpo,bisca
```
**Descrizione**
```
Slot 5×3, 10 linee, in un caveau a mezzanotte.

- Wild espanso, giri bonus con la dinamite
- Cassaforte con 4 jackpot e 3 mini-giochi

Gioco in italiano (gli screenshot sono in inglese). Offline, senza registrazione.

Acquisti in-app facoltativi: pacchetti di monete virtuali.

Questo è un gioco di intrattenimento che simula una slot machine. Destinato a un pubblico adulto (18+). Non offre gioco d'azzardo con denaro reale né possibilità di vincere denaro o premi reali; i crediti non hanno valore monetario. I risultati ottenuti nel gioco non implicano alcun successo futuro nel gioco d'azzardo con denaro reale.
```

### Inglese (U.S.A.)

**Nome** (29/30)
```
Midnight Heist – Casino Slots
```
**Sottotitolo** (27/30)
```
Vault slots with 4 jackpots
```
**Testo promozionale** (102/170)
```
Midnight, a vault and a masked Mastermind: spin the reels, blow the safe and go for the GRAND jackpot.
```
**Parole chiave** (94/100)
```
slot,slots,casino,vegas,jackpot,heist,vault,bank,robbery,reels,spin,wild,offline,machine,bonus
```
**Descrizione**
```
Midnight. A bank. A masked Mastermind. Midnight Heist is a 5-reel, 3-row slot machine with 10 paylines, set in a moonlit vault.

- EXPANDING WILD – the Mastermind's mask covers the whole reel
- THE HEIST – 3 safes trigger free spins: dynamite blows up symbols and multiplies your wins
- THE VAULT – hold & win bonus with 4 jackpots: Mini, Minor, Major and GRAND
- 3 MINI-GAMES – Lockpick, Diamond Cut and Perfect Robbery
- THE PLAN – collect the tools and unlock special bonuses
- Illustrated art, original soundtrack, 7 languages, autoplay and turbo

Play anytime, offline, no sign-up.

Optional in-app purchases: packs of virtual coins.

This is an entertainment game that simulates a slot machine. Intended for adults (18+). It does not offer real-money gambling or any opportunity to win real money or prizes; credits have no monetary value. Practice or success at this game does not imply future success at real-money gambling.
```

### Spagnolo (Spagna)

**Nome** (29/30)
```
Midnight Heist – Slots Casino
```
**Sottotitolo** (26/30)
```
Tragaperras con 4 jackpots
```
**Testo promozionale** (130/170)
```
Medianoche, una cámara acorazada y un Mastermind enmascarado: gira los rodillos, vuela la caja fuerte y ve a por el GRAND jackpot.
```
**Parole chiave** (93/100)
```
tragaperras,slot,casino,vegas,jackpot,atraco,banco,bóveda,rodillos,giros,wild,offline,máquina
```
**Descrizione**
```
Slot 5×3, 10 líneas, en una cámara acorazada a medianoche.

- Wild expansivo y giros bonus con dinamita
- Cámara con 4 jackpots y 3 minijuegos

Juego en español (las capturas están en inglés). Sin conexión y sin registro.

Compras opcionales dentro de la app: paquetes de monedas virtuales.

Este es un juego de entretenimiento que simula una tragaperras. Dirigido a adultos (18+). No ofrece apuestas con dinero real ni posibilidad de ganar dinero o premios reales; los créditos no tienen valor monetario. El éxito en este juego no implica éxito futuro en apuestas con dinero real.
```

### Tedesco

**Nome** (29/30)
```
Midnight Heist – Casino Slots
```
**Sottotitolo** (27/30)
```
Tresor-Slots mit 4 Jackpots
```
**Testo promozionale** (118/170)
```
Mitternacht, ein Tresor und ein maskierter Mastermind: Dreh die Walzen, spreng den Safe und hol dir den GRAND-Jackpot.
```
**Parole chiave** (92/100)
```
slot,spielautomat,casino,vegas,jackpot,raub,tresor,bank,walzen,drehen,wild,offline,automaten
```
**Descrizione**
```
5×3-Slot mit 10 Linien in einem Tresorraum um Mitternacht.

- Expanding Wild und Bonusrunden mit Dynamit
- Tresor mit 4 Jackpots und 3 Minispiele

Spiel auf Deutsch (die Screenshots sind auf Englisch). Offline, ohne Registrierung.

Optionale In-App-Käufe: Pakete mit virtuellen Münzen.

Dies ist ein Unterhaltungsspiel, das einen Spielautomaten simuliert. Für Erwachsene (18+). Es bietet kein Echtgeld-Glücksspiel und keine Möglichkeit, echtes Geld oder Preise zu gewinnen; Credits haben keinen Geldwert. Erfolg in diesem Spiel bedeutet keinen zukünftigen Erfolg beim Echtgeld-Glücksspiel.
```

### Francese

**Nome** (29/30)
```
Midnight Heist – Slots Casino
```
**Sottotitolo** (28/30)
```
Machine à sous et 4 jackpots
```
**Testo promozionale** (126/170)
```
Minuit, une chambre forte et un Mastermind masqué : fais tourner les rouleaux, fais sauter le coffre et vise le jackpot GRAND.
```
**Parole chiave** (94/100)
```
machine à sous,slot,casino,vegas,jackpot,braquage,coffre,banque,rouleaux,tours,wild,hors ligne
```
**Descrizione**
```
Slot 5×3, 10 lignes, dans une salle des coffres à minuit.

- Wild extensible et tours bonus à la dynamite
- Coffre avec 4 jackpots et 3 mini-jeux

Jeu en français (les captures d'écran sont en anglais). Hors ligne, sans inscription.

Achats intégrés facultatifs : packs de pièces virtuelles.

Ceci est un jeu de divertissement qui simule une machine à sous. Réservé aux adultes (18+). Il ne propose pas de jeu d'argent réel ni de possibilité de gagner de l'argent ou des prix réels ; les crédits n'ont aucune valeur monétaire. Réussir à ce jeu n'implique aucune réussite future aux jeux d'argent réel.
```

### Portoghese (Portogallo)

**Nome** (29/30)
```
Midnight Heist – Slots Casino
```
**Sottotitolo** (29/30)
```
Slots de cofre com 4 jackpots
```
**Testo promozionale** (103/170)
```
Meia-noite, um cofre e um Mastermind mascarado: gira os rolos, rebenta o cofre e tenta o jackpot GRAND.
```
**Parole chiave** (93/100)
```
slot,caça-níqueis,casino,vegas,jackpot,assalto,cofre,banco,rolos,rodadas,wild,offline,máquina
```
**Descrizione**
```
Slot 5×3, 10 linhas, numa casa-forte à meia-noite.

- Wild expansivo e rodadas bónus com dinamite
- Cofre com 4 jackpots e 3 minijogos

Jogo em português (as capturas de ecrã estão em inglês). Offline, sem registo.

Compras opcionais na app: pacotes de moedas virtuais.

Este é um jogo de entretenimento que simula uma slot machine. Destinado a adultos (18+). Não oferece apostas com dinheiro real nem possibilidade de ganhar dinheiro ou prémios reais; os créditos não têm valor monetário. O sucesso neste jogo não implica sucesso futuro em apostas com dinheiro real.
```

### Russo

**Nome** (29/30)
```
Midnight Heist – Слоты казино
```
**Sottotitolo** (27/30)
```
Слоты с сейфом и джекпотами
```
**Testo promozionale** (100/170)
```
Полночь, хранилище и Мастермайнд в маске: крути барабаны, взрывай сейф и охоться за джекпотом GRAND.
```
**Parole chiave** (91/100)
```
слоты,слот,казино,вегас,джекпот,ограбление,сейф,банк,барабаны,вращения,вайлд,офлайн,автомат
```
**Descrizione**
```
Слот 5×3, 10 линий, в полночном хранилище банка.

- Расширяющийся вайлд и бонусные вращения с динамитом
- Сейф с 4 джекпотами и 3 мини-игры

Игра на русском (скриншоты на английском). Офлайн, без регистрации.

Необязательные встроенные покупки: наборы виртуальных монет.

Это развлекательная игра, имитирующая игровой автомат. Для взрослых (18+). Игра не предлагает азартных игр на реальные деньги и возможности выиграть реальные деньги или призы; кредиты не имеют денежной стоимости. Успех в этой игре не означает успеха в азартных играх на реальные деньги.
```

## 9. Build con Xcode

1. Terminale (crea il progetto Xcode):
```
cd ~/slot-mvp && mkdir -p export/ios && ~/Desktop/Godot.app/Contents/MacOS/Godot --headless --path . --export-release "iOS" "export/ios/Midnight Heist.xcodeproj"
```
2. Aprilo:
```
open ~/slot-mvp/export/ios/"Midnight Heist.xcodeproj"
```
3. In Xcode: clicca il progetto a sinistra → target **Midnight Heist** → **Signing & Capabilities** → spunta *Automatically manage signing* → Team: il tuo. Se manca, **+ Capability → In-App Purchase**.
4. In alto come destinazione scegli **Any iOS Device (arm64)**.
5. Menu **Product → Archive** → quando finisce **Distribute App → App Store Connect → Distribute**.
6. Dopo 10-30 minuti la build compare in App Store Connect (scheda TestFlight, poi selezionabile nella versione).

## 10. Prova prima di inviare (consigliato)

- Il tuo iPhone 13 non va con Xcode, ma **TestFlight funziona** (serve iOS 15+). Installa TestFlight dall'App Store, aggiungiti come tester interno e prova un acquisto: con TestFlight è **gratis** (ambiente sandbox).
- Controlla: i prezzi compaiono nel negozio, l'acquisto arriva, esce "ACQUISTO RIUSCITO" e il saldo sale.

## 11. Invio

- **Aggiungi per la revisione → Invia**. Solo Heist per ora: Case ed Elixir dopo l'approvazione di Heist.
