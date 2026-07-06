"""
models/level.py
-----------------
Bevat de Level class: een "stuk wereld" met beschrijving, enemies,
items en exits naar andere levels.
"""

from typing import List, Dict, Optional

from models.enemy import Enemy
from models.item import Item


class Level:
    """Representeert één level/kamer in de wereld."""

    def __init__(
        self,
        name: str,
        description: str,
        enemies: Optional[List[Enemy]] = None,
        items: Optional[List[Item]] = None,
        exits: Optional[Dict[str, str]] = None,
    ):
        self.name = name
        self.description = description
        self.enemies: List[Enemy] = enemies if enemies is not None else []
        self.items: List[Item] = items if items is not None else []
        # exits: richting (bv. "east") -> naam van level
        self.exits: Dict[str, str] = exits if exits is not None else {}

    def is_cleared(self) -> bool:
        """True als alle enemies in dit level dood zijn (of er geen zijn)."""
        return all(not enemy.is_alive() for enemy in self.enemies)

    def levende_enemies(self) -> List[Enemy]:
        """Geeft alleen de enemies terug die nog leven."""
        return [e for e in self.enemies if e.is_alive()]

    def remove_item(self, item_name: str) -> Optional[Item]:
        """Haalt een item met deze naam uit het level en geeft het terug.
        Geeft None terug als het item niet gevonden is."""
        for item in self.items:
            if item.name.lower() == item_name.lower():
                self.items.remove(item)
                return item
        return None

    def beschrijving_volledig(self) -> str:
        """Volledige tekstbeschrijving: omschrijving + enemies + items."""
        regels = [f"=== {self.name} ===", self.description]

        levend = self.levende_enemies()
        if levend:
            regels.append("Vijanden hier:")
            for i, enemy in enumerate(levend):
                regels.append(f"  [{i}] {enemy}")
        else:
            regels.append("Geen vijanden hier.")

        if self.items:
            regels.append("Items hier:")
            for item in self.items:
                regels.append(f"  - {item}")
        else:
            regels.append("Geen items hier.")

        if self.exits:
            regels.append(
                "Uitgangen: " + ", ".join(
                    f"{richting} -> {level_naam}"
                    for richting, level_naam in self.exits.items()
                )
            )
        else:
            regels.append("Geen uitgangen vanaf hier.")

        return "\n".join(regels)

    def __str__(self) -> str:
        return f"Level: {self.name}"
