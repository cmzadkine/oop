"""
services/manager.py
--------------------
Bevat de business-logica: toevoegen, tonen, verwijderen, zoeken en
filteren van reserveringen, inclusief validatie en koppeling met opslag.
"""

from typing import List, Optional

from models.reservering import Reservering
from services.storage import ReserveringStorage


MAX_PERSONEN_PER_TIJDSLOT = 30  # Extra 3: max capaciteit per datum+tijd


class ReserveringManager:
    """Beheert alle reserveringen: toevoegen, tonen, verwijderen, opslaan."""

    def __init__(self, storage: ReserveringStorage):
        self.storage = storage
        self.reserveringen: List[Reservering] = self.storage.load()

    # ------------------------------------------------------------------
    # Validatie
    # ------------------------------------------------------------------
    @staticmethod
    def _validate(naam: str, datum: str, tijd: str, aantal_personen) -> bool:
        """Controleert of de invoer geldig is."""
        if not naam or not naam.strip():
            return False
        if not datum or not datum.strip():
            return False
        if not tijd or not tijd.strip():
            return False
        try:
            aantal = int(aantal_personen)
        except (TypeError, ValueError):
            return False
        if aantal <= 0:
            return False
        return True

    def _capaciteit_beschikbaar(self, datum: str, tijd: str, aantal: int) -> bool:
        """Extra 3: checkt of het max aantal personen per tijdslot niet
        wordt overschreden."""
        huidig_totaal = sum(
            r.aantal_personen
            for r in self.reserveringen
            if r.datum == datum and r.tijd == tijd
        )
        return huidig_totaal + aantal <= MAX_PERSONEN_PER_TIJDSLOT

    # ------------------------------------------------------------------
    # Basisfeatures
    # ------------------------------------------------------------------
    def voeg_toe(self, naam: str, datum: str, tijd: str, aantal_personen) -> bool:
        """Voegt een nieuwe reservering toe, na validatie."""
        if not self._validate(naam, datum, tijd, aantal_personen):
            return False

        aantal = int(aantal_personen)

        if not self._capaciteit_beschikbaar(datum, tijd, aantal):
            return False

        nieuwe_reservering = Reservering(
            naam=naam.strip(),
            datum=datum.strip(),
            tijd=tijd.strip(),
            aantal_personen=aantal,
        )
        self.reserveringen.append(nieuwe_reservering)
        self.storage.save(self.reserveringen)
        return True

    def alles(self) -> List[Reservering]:
        """Geeft alle reserveringen terug."""
        return self.reserveringen

    def verwijder(self, index: int) -> bool:
        """Verwijdert een reservering op basis van index (0-based)."""
        if index < 0 or index >= len(self.reserveringen):
            return False
        del self.reserveringen[index]
        self.storage.save(self.reserveringen)
        return True

    # ------------------------------------------------------------------
    # Extra features
    # ------------------------------------------------------------------
    def zoek_op_naam(self, zoekterm: str) -> List[Reservering]:
        """Extra 1: zoekt reserveringen waarvan de naam de zoekterm bevat."""
        zoekterm = zoekterm.strip().lower()
        return [r for r in self.reserveringen if zoekterm in r.naam.lower()]

    def filter_op_datum(self, datum: str) -> List[Reservering]:
        """Extra 2: geeft alle reserveringen op een specifieke datum terug."""
        datum = datum.strip()
        return [r for r in self.reserveringen if r.datum == datum]
