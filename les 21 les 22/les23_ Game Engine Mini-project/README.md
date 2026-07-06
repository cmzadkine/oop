# Text-based RPG (+ bonus multiplayer via sockets)

Een turn-based text RPG in Python met OOP: Player, Enemy, Item en Level
classes, plus een bonus multiplayer-versie via sockets.

## Projectstructuur

```
les23_rpg/
│
├── main.py                     # Bouwt de wereld op en start de singleplayer game
├── game.py                     # De game-engine: game-loop + command handling
│
├── models/
│   ├── __init__.py
│   ├── player.py                # Player class (hp, attack, inventory)
│   ├── enemy.py                 # Enemy class (hp, attack)
│   ├── item.py                  # Item class (heal / attack_boost effecten)
│   └── level.py                 # Level class (description, enemies, items, exits)
│
├── tests/
│   ├── __init__.py
│   └── test_rpg.py              # Unittests voor alle classes
│
└── bonus_multiplayer/
    ├── server.py                 # Socket-server (1 client, zie hints voor 2 spelers)
    └── client.py                 # Socket-client
```

## Singleplayer spelen

```bash
cd les23_rpg
python main.py
```

Commando's in het spel:
- `look` — bekijk de huidige kamer (beschrijving, vijanden, items, uitgangen)
- `fight <nr>` — val een vijand aan op basis van zijn nummer, bv. `fight 0`
- `take <item>` — pak een item op, bv. `take potion`
- `use <item>` — gebruik een item uit je inventory, bv. `use potion`
- `go <richting>` — loop naar een andere level, bv. `go east`
- `quit` — stop het spel

De wereld bestaat uit 3 levels: **Forest → Cave → Boss Room**. Je moet
alle vijanden in een level verslaan voordat je verder kan lopen. Versla
de Dragon in de Boss Room om te winnen.

## Bonus: multiplayer via sockets

Open twee terminals.

**Terminal 1 — start de server:**
```bash
cd les23_rpg
python bonus_multiplayer/server.py
```

**Terminal 2 — start de client:**
```bash
cd les23_rpg
python bonus_multiplayer/client.py
```

Typ in de client commando's zoals: `LOOK`, `ATTACK 0`, `TAKE potion`,
`USE potion`, `GO east`, `QUIT`.

Deze versie ondersteunt op dit moment 1 client. Onderaan
`server.py` staan hints om het uit te breiden naar 2 spelers met
beurten (turn-based multiplayer).

## Tests draaien

```bash
cd les23_rpg
python -m unittest -v
```

Er zitten 13 tests in die Player, Enemy, Item en Level dekken:
schade/healing binnen grenzen, aanvallen, items gebruiken, en levels
als "cleared" herkennen.

## Wat heb je geleerd?

- Een mini game-engine bouwen met een duidelijke game-loop
- Samenwerkende OOP-classes: Player, Enemy, Item en Level
- Data organiseren met lijsten en dicts (inventory, exits, levels)
- Turn-based combat implementeren
- Basis netwerken met sockets: een server die state beheert en een
  client die commando's stuurt en antwoorden toont
