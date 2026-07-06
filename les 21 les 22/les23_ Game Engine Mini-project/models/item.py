"""
models/item.py
---------------
Bevat de Item class. Een item heeft een naam, een type (wat het doet)
en een waarde (hoe sterk het effect is), en kan zichzelf toepassen op
een speler via apply(player).
"""


class Item:
    """Representeert een item zoals een potion of een sword."""

    def __init__(self, name: str, item_type: str, value: int):
        """
        name: bv. "Potion", "Sword"
        item_type: "heal" of "attack_boost"
        value: bv. 20 (heal) of 5 (attack_boost)
        """
        self.name = name
        self.type = item_type
        self.value = value

    def apply(self, player) -> str:
        """Past het effect van dit item toe op de gegeven player.

        Geeft een tekstboodschap terug die je in de game-loop kan printen.
        """
        if self.type == "heal":
            player.heal(self.value)
            return f"{player.name} gebruikt {self.name} en heelt {self.value} HP."
        elif self.type == "attack_boost":
            player.attack_power += self.value
            return (
                f"{player.name} gebruikt {self.name} en krijgt "
                f"+{self.value} attack power!"
            )
        else:
            return f"{self.name} heeft geen bekend effect."

    def __str__(self) -> str:
        return f"{self.name} ({self.type}, {self.value})"
