"""
services/storage.py
--------------------
Verantwoordelijk voor het lezen en schrijven van reserveringen naar een
JSON-bestand, zodat de data bewaard blijft tussen sessies.
"""

import json
import os
from typing import List

from models.reservering import Reservering


class ReserveringStorage:
    """Leest en schrijft een lijst van Reservering-objecten naar JSON."""

    def __init__(self, bestandsnaam: str = "reserveringen.json"):
        self.bestandsnaam = bestandsnaam

    def load(self) -> List[Reservering]:
        """Laadt reserveringen uit het JSON-bestand.

        Als het bestand niet bestaat (of leeg/corrupt is), wordt een
        lege lijst teruggegeven zodat de app niet crasht bij eerste start.
        """
        if not os.path.exists(self.bestandsnaam):
            return []

        try:
            with open(self.bestandsnaam, "r", encoding="utf-8") as f:
                ruwe_data = json.load(f)
        except (json.JSONDecodeError, OSError):
            return []

        return [Reservering.from_dict(item) for item in ruwe_data]

    def save(self, reserveringen: List[Reservering]) -> None:
        """Slaat de lijst reserveringen op als JSON-bestand."""
        data = [r.to_dict() for r in reserveringen]
        with open(self.bestandsnaam, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
