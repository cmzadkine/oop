from dataclasses import dataclass


@dataclass
class CryptoPrijs:
    naam: str
    prijs_eur: float

    def toon(self):
        print(f"{self.naam}: €{self.prijs_eur:.2f}")