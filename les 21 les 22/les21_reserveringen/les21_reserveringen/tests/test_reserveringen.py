"""
tests/test_reserveringen.py
----------------------------
Minimaal 5 unittests voor het reserveringssysteem.

Run met:
    python -m unittest
"""

import os
import unittest

from services.storage import ReserveringStorage
from services.manager import ReserveringManager


TEST_BESTAND = "test_reserveringen.json"


class TestReserveringManager(unittest.TestCase):

    def setUp(self):
        """Wordt vóór elke test uitgevoerd: schone lei met een test-bestand."""
        if os.path.exists(TEST_BESTAND):
            os.remove(TEST_BESTAND)
        self.storage = ReserveringStorage(TEST_BESTAND)
        self.manager = ReserveringManager(self.storage)

    def tearDown(self):
        """Wordt na elke test uitgevoerd: opruimen van het test-bestand."""
        if os.path.exists(TEST_BESTAND):
            os.remove(TEST_BESTAND)

    def test_geldig_toevoegen(self):
        resultaat = self.manager.voeg_toe("Jan", "2026-02-06", "18:30", 4)
        self.assertTrue(resultaat)
        self.assertEqual(len(self.manager.alles()), 1)

    def test_toevoegen_met_lege_naam(self):
        resultaat = self.manager.voeg_toe("", "2026-02-06", "18:30", 4)
        self.assertFalse(resultaat)
        self.assertEqual(len(self.manager.alles()), 0)

    def test_toevoegen_met_aantal_nul(self):
        resultaat = self.manager.voeg_toe("Jan", "2026-02-06", "18:30", 0)
        self.assertFalse(resultaat)

    def test_verwijderen_geldig_index(self):
        self.manager.voeg_toe("Jan", "2026-02-06", "18:30", 4)
        resultaat = self.manager.verwijder(0)
        self.assertTrue(resultaat)
        self.assertEqual(len(self.manager.alles()), 0)

    def test_verwijderen_fout_index(self):
        resultaat = self.manager.verwijder(99)
        self.assertFalse(resultaat)

    def test_toevoegen_met_niet_numeriek_aantal(self):
        resultaat = self.manager.voeg_toe("Jan", "2026-02-06", "18:30", "abc")
        self.assertFalse(resultaat)

    def test_max_capaciteit_per_tijdslot(self):
        # Vult tijdslot bijna vol (30 personen max)
        self.manager.voeg_toe("Groep A", "2026-02-06", "19:00", 28)
        # Deze past er nog wel bij
        self.assertTrue(
            self.manager.voeg_toe("Groep B", "2026-02-06", "19:00", 2)
        )
        # Deze niet meer, want de 30 is al bereikt
        self.assertFalse(
            self.manager.voeg_toe("Groep C", "2026-02-06", "19:00", 1)
        )

    def test_opslag_blijft_bewaard_na_herladen(self):
        self.manager.voeg_toe("Jan", "2026-02-06", "18:30", 4)
        # Nieuwe manager met dezelfde storage simuleert een herstart
        nieuwe_manager = ReserveringManager(self.storage)
        self.assertEqual(len(nieuwe_manager.alles()), 1)
        self.assertEqual(nieuwe_manager.alles()[0].naam, "Jan")

    def test_zoek_op_naam(self):
        self.manager.voeg_toe("Jan Jansen", "2026-02-06", "18:30", 2)
        self.manager.voeg_toe("Piet Pieters", "2026-02-06", "19:00", 3)
        resultaten = self.manager.zoek_op_naam("jan")
        self.assertEqual(len(resultaten), 1)
        self.assertEqual(resultaten[0].naam, "Jan Jansen")

    def test_filter_op_datum(self):
        self.manager.voeg_toe("Jan", "2026-02-06", "18:30", 2)
        self.manager.voeg_toe("Piet", "2026-02-07", "19:00", 3)
        resultaten = self.manager.filter_op_datum("2026-02-06")
        self.assertEqual(len(resultaten), 1)
        self.assertEqual(resultaten[0].naam, "Jan")


if __name__ == "__main__":
    unittest.main()
