"""
models/reservering.py
----------------------
Bevat alleen de data-class Reservering.
Geen logica of opslag hier, alleen data + omzetting naar/van dict.
"""

from dataclasses import dataclass, asdict


@dataclass
class Reservering:
    """Representeert één reservering voor het restaurant."""

    naam: str
    datum: str            # bv. "2026-02-06"
    tijd: str              # bv. "18:30"
    aantal_personen: int

    def to_dict(self) -> dict:
        """Zet de reservering om naar een dictionary (voor JSON-opslag)."""
        return asdict(self)

    @staticmethod
    def from_dict(data: dict) -> "Reservering":
        """Maakt een Reservering-object van een dictionary (bij het laden)."""
        return Reservering(
            naam=data["naam"],
            datum=data["datum"],
            tijd=data["tijd"],
            aantal_personen=data["aantal_personen"],
        )

    def __str__(self) -> str:
        return (
            f"{self.naam} | {self.datum} om {self.tijd} "
            f"| {self.aantal_personen} perso(o)n(en)"
        )
