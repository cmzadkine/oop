"""
main.py
-------
Bouwt de wereld op (player, levels, enemies, items, exits) en start de game.
"""

from models.player import Player
from models.enemy import Enemy
from models.item import Item
from models.level import Level
from game import Game


def maak_wereld():
    """Bouwt de speler en alle levels op, en koppelt de exits."""
    player = Player(name="Held", hp=100, attack_power=10)

    forest = Level(
        name="Forest",
        description="Je staat in een donker bos. Takken kraken om je heen.",
        enemies=[Enemy(name="Wolf", hp=20, attack_power=4)],
        items=[Item(name="Potion", item_type="heal", value=20)],
        exits={"east": "Cave"},
    )

    cave = Level(
        name="Cave",
        description="Een vochtige grot. Het druipt van de stalactieten.",
        enemies=[Enemy(name="Goblin", hp=25, attack_power=6)],
        items=[Item(name="Sword", item_type="attack_boost", value=5)],
        exits={"north": "Boss Room", "west": "Forest"},
    )

    boss_room = Level(
        name="Boss Room",
        description="Een enorme zaal. Je voelt een dreigende aanwezigheid.",
        enemies=[Enemy(name="Dragon", hp=50, attack_power=10)],
        items=[],
        exits={"south": "Cave"},
    )

    levels = {
        "Forest": forest,
        "Cave": cave,
        "Boss Room": boss_room,
    }

    return player, levels


def main() -> None:
    player, levels = maak_wereld()
    game = Game(player=player, levels=levels, start_level="Forest")
    game.run()


if __name__ == "__main__":
    main()
