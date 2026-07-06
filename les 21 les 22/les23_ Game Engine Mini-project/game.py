"""
game.py
--------
De game-engine: bevat de game-loop, het menu en de verwerking van
commando's zoals look/fight/take/use/go.
"""

from typing import Dict

from models.player import Player
from models.level import Level


class Game:
    """Beheert de speler, alle levels en de game-loop."""

    def __init__(self, player: Player, levels: Dict[str, Level], start_level: str):
        self.player = player
        self.levels = levels
        self.current_level_name = start_level
        self.running = True

    @property
    def current_level(self) -> Level:
        return self.levels[self.current_level_name]

    # ------------------------------------------------------------------
    # Weergave
    # ------------------------------------------------------------------
    def show_status(self) -> None:
        print("\n" + "-" * 40)
        print(self.player)
        print(f"Inventory: {self.player.inventory_str()}")
        print(f"Locatie: {self.current_level.name}")
        print("-" * 40)

    def show_menu(self) -> None:
        print("\nActies: look | fight <nr> | take <item> | use <item> | "
              "go <richting> | quit")

    # ------------------------------------------------------------------
    # Command handling
    # ------------------------------------------------------------------
    def handle_command(self, cmd: str) -> None:
        """Verwerkt één regel input van de speler."""
        cmd = cmd.strip()
        if not cmd:
            return

        delen = cmd.split(maxsplit=1)
        actie = delen[0].lower()
        argument = delen[1] if len(delen) > 1 else ""

        if actie == "look":
            print(self.current_level.beschrijving_volledig())
        elif actie == "fight":
            self._fight(argument)
        elif actie == "take":
            self._take(argument)
        elif actie == "use":
            self._use(argument)
        elif actie == "go":
            self._go(argument)
        elif actie == "quit":
            print("Je stopt met spelen. Tot ziens!")
            self.running = False
        else:
            print("⚠️  Onbekend commando. Typ 'look', 'fight <nr>', "
                  "'take <item>', 'use <item>', 'go <richting>' of 'quit'.")

    def _fight(self, argument: str) -> None:
        levend = self.current_level.levende_enemies()
        if not levend:
            print("Er zijn hier geen vijanden om te bevechten.")
            return
        try:
            index = int(argument)
            enemy = levend[index]
        except (ValueError, IndexError):
            print("⚠️  Geef een geldig vijand-nummer op, bv. 'fight 0'.")
            return

        print(self.player.attack(enemy))
        if not enemy.is_alive():
            print(f"💀 {enemy.name} is verslagen!")
            return

        # Enemy vecht terug als hij nog leeft
        print(enemy.attack(self.player))

    def _take(self, argument: str) -> None:
        if not argument:
            print("⚠️  Welk item wil je pakken? bv. 'take potion'.")
            return
        item = self.current_level.remove_item(argument)
        if item is None:
            print(f"Er ligt hier geen item genaamd '{argument}'.")
            return
        self.player.add_item(item)
        print(f"Je hebt {item.name} opgepakt.")

    def _use(self, argument: str) -> None:
        if not argument:
            print("⚠️  Welk item wil je gebruiken? bv. 'use potion'.")
            return
        print(self.player.use_item(argument))

    def _go(self, argument: str) -> None:
        if not argument:
            print("⚠️  In welke richting wil je gaan? bv. 'go east'.")
            return
        if not self.current_level.is_cleared():
            print("⚠️  Je kunt dit level pas verlaten als alle vijanden "
                  "verslagen zijn!")
            return
        volgende_naam = self.current_level.exits.get(argument.lower())
        if volgende_naam is None:
            print(f"Er is geen uitgang '{argument}' vanaf hier.")
            return
        self.current_level_name = volgende_naam
        print(f"Je loopt naar {self.current_level.name}.")

    # ------------------------------------------------------------------
    # Einde van het spel
    # ------------------------------------------------------------------
    def check_end(self) -> bool:
        """Controleert of het spel voorbij is (win/lose).
        Geeft True terug als het spel gestopt moet worden."""
        if not self.player.is_alive():
            print("\n💀 Game Over! Je bent verslagen...")
            return True

        if self.current_level_name == "Boss Room" and self.current_level.is_cleared():
            print("\n🏆 Gefeliciteerd! Je hebt de baas verslagen en het spel gewonnen!")
            return True

        return False

    # ------------------------------------------------------------------
    # Game-loop
    # ------------------------------------------------------------------
    def run(self) -> None:
        print("=== Welkom bij de Text RPG! ===")
        print("Typ 'look' om je omgeving te bekijken.")

        while self.running:
            self.show_status()
            self.show_menu()

            if self.check_end():
                break

            cmd = input("> ")
            self.handle_command(cmd)

            if self.check_end():
                break
