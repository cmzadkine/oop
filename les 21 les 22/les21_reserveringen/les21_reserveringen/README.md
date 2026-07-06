# Restaurant Reserveringssysteem (CLI)

Een command-line applicatie om reserveringen voor een restaurant te beheren.
Gebouwd als portfolio-project met OOP, JSON-opslag, validatie en unittests.

## Wat doet de app?

Met deze app kun je:
- reserveringen toevoegen (naam, datum, tijd, aantal personen)
- alle reserveringen bekijken
- een reservering verwijderen
- zoeken op naam
- filteren op datum
- de max capaciteit per tijdslot (30 personen) laten bewaken

Alle data wordt opgeslagen in `reserveringen.json`, zodat je reserveringen
bewaard blijven, ook na het afsluiten van het programma.

## Hoe start je de app?

Vereisten: Python 3.8 of hoger (geen extra packages nodig).

```bash
cd les21_reserveringen
python main.py
```

Je krijgt dan een menu te zien:

```
=== Restaurant Reserveringssysteem ===
1. Toon reserveringen
2. Voeg reservering toe
3. Verwijder reservering
4. Zoek reservering op naam
5. Filter reserveringen op datum
6. Stoppen
```

## Features

**Basis**
- Toevoegen van reserveringen (met validatie)
- Tonen van alle reserveringen
- Verwijderen van een reservering
- Opslaan en laden via JSON-bestand

**Validatie**
- Naam mag niet leeg zijn
- Datum mag niet leeg zijn
- Tijd mag niet leeg zijn
- Aantal personen moet een getal zijn en groter dan 0

**Extra's**
- ⭐ Zoeken op naam
- ⭐ Filteren op datum
- ⭐ Maximale capaciteit van 30 personen per tijdslot (datum + tijd combinatie)

## Projectstructuur

```
les21_reserveringen/
│
├── main.py                     # CLI-menu, alleen input/output
├── README.md                   # Deze documentatie
├── reserveringen.json          # Wordt automatisch aangemaakt bij gebruik
│
├── models/
│   ├── __init__.py
│   └── reservering.py          # Class Reservering (alleen data)
│
├── services/
│   ├── __init__.py
│   ├── storage.py               # Class ReserveringStorage (lezen/schrijven JSON)
│   └── manager.py               # Class ReserveringManager (logica + validatie)
│
└── tests/
    ├── __init__.py
    └── test_reserveringen.py    # Unittests
```

## Hoe run je de tests?

Vanuit de hoofdmap `les21_reserveringen/`:

```bash
python -m unittest
```

Er zijn 10 tests die o.a. controleren:
- of geldig toevoegen werkt
- of lege naam / aantal 0 / niet-numeriek aantal wordt geweigerd
- of verwijderen op geldige/foute index correct werkt
- of de max capaciteit per tijdslot goed wordt bewaakt
- of data bewaard blijft na het "herstarten" van de manager (opslag)
- of zoeken en filteren correct werken

## Wat heb je geleerd?

- Een applicatie opdelen in duidelijke lagen: **models** (data),
  **services** (logica + opslag) en een **main**-bestand (UI/CLI)
- Werken met `@dataclass` voor een overzichtelijke data-class
- Data persistent opslaan met JSON (`json.dump` / `json.load`)
- Input valideren voordat je het verwerkt, zodat de app niet crasht
  op foute invoer
- Unittests schrijven met `unittest`, inclusief `setUp`/`tearDown`
  om tests van elkaar te isoleren
- Iteratief bouwen: eerst de basis-logica (in-memory), daarna opslag,
  daarna de CLI, en tot slot extra features
