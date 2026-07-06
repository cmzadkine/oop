"""
models/player.py
-----------------
Bevat de Player class: de speelbare hoofdpersoon met hp, attack_power
en een inventory vol Items.
"""

from typing import List, Optional

from models.item import Item


class Player:
    """Representeert de speler in de RPG."""

    def __init__(self, name: str, hp: int = 100, attack_power: int = 10):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack_power = attack_power
        self.inventory: List[Item] = []

    def is_alive(self) -> bool:
        """True zolang de speler nog hp over heeft."""
        return self.hp > 0

    def take_damage(self, amount: int) -> None:
        """Verlaagt hp, maar nooit onder 0."""
        self.hp = max(0, self.hp - amount)

    def heal(self, amount: int) -> None:
        """Verhoogt hp, maar nooit boven max_hp."""
        self.hp = min(self.max_hp, self.hp + amount)

    def attack(self, enemy) -> str:
        """Valt een enemy aan met de attack_power van de speler."""
        enemy.take_damage(self.attack_power)
        return (
            f"{self.name} valt {enemy.name} aan voor {self.attack_power} damage! "
            f"({enemy.name} heeft nu {enemy.hp} HP)"
        )

    def add_item(self, item: Item) -> None:
        """Voegt een item toe aan de inventory."""
        self.inventory.append(item)

    def use_item(self, item_name: str) -> str:
        """Zoekt een item op naam in de inventory, past het toe en
        verwijdert het daarna. Geeft een boodschap terug."""
        item = self._find_item(item_name)
        if item is None:
            return f"Je hebt geen item genaamd '{item_name}'."

        boodschap = item.apply(self)
        self.inventory.remove(item)
        return boodschap

    def _find_item(self, item_name: str) -> Optional[Item]:
        """Zoekt een item op naam (niet hoofdlettergevoelig)."""
        for item in self.inventory:
            if item.name.lower() == item_name.lower():
                return item
        return None

    def inventory_str(self) -> str:
        """Leesbare weergave van de inventory."""
        if not self.inventory:
            return "Inventory is leeg."
        return ", ".join(str(item) for item in self.inventory)

    def __str__(self) -> str:
        return (
            f"{self.name} | HP: {self.hp}/{self.max_hp} | "
            f"Attack: {self.attack_power}"
        )
