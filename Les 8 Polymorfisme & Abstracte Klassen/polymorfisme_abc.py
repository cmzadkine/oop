# les8_polymorfisme_abc.py

from abc import ABC, abstractmethod

# Stap 3 — Abstracte class
class Betaalmethode(ABC):
    def __init__(self, naam):
        self.naam = naam

    @abstractmethod
    def betaal(self, bedrag):
        """Elke subclass moet deze methode implementeren"""
        pass

# Stap 4 — Subclasses
class PinBetaling(Betaalmethode):
    def __init__(self):
        super().__init__("Pin")

    # Stap 5 — Override betaal()
    def betaal(self, bedrag):
        return f"{self.naam}-betaling: Betaling van €{bedrag:.2f} gepind."

class ContantBetaling(Betaalmethode):
    def __init__(self):
        super().__init__("Contant")

    def betaal(self, bedrag):
        return f"{self.naam}-betaling: Contant ontvangen, bedrag €{bedrag:.2f}."

class OnlineBetaling(Betaalmethode):
    def __init__(self):
        super().__init__("Online")

    def betaal(self, bedrag):
        return f"{self.naam}-betaling: Online betaling van €{bedrag:.2f} verwerkt."

# Stap 6 — Test met een lijst
if __name__ == "__main__":
    methodes = [PinBetaling(), ContantBetaling(), OnlineBetaling()]
    
    for methode in methodes:
        print(methode.betaal(49.95))