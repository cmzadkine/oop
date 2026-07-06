"""
models/enemy.py
-----------------
Bevat de Enemy class: tegenstanders met hp en attack_power.
"""


class Enemy:
    """Representeert een vijand in de RPG."""

    def __init__(self, name: str, hp: int = 30, attack_power: int = 5):
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    def is_alive(self) -> bool:
        """True zolang de enemy nog hp over heeft."""
        return self.hp > 0

    def take_damage(self, amount: int) -> None:
        """Verlaagt hp, maar nooit onder 0."""
        self.hp = max(0, self.hp - amount)

    def attack(self, player) -> str:
        """Valt de speler aan met de attack_power van de enemy."""
        player.take_damage(self.attack_power)
        return (
            f"{self.name} valt {player.name} aan voor {self.attack_power} damage! "
            f"({player.name} heeft nu {player.hp} HP)"
        )

    def __str__(self) -> str:
        return f"{self.name} (HP: {self.hp}, Attack: {self.attack_power})"
