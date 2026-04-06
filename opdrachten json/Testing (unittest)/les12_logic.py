# les12_logic.py

class Product:
    def __init__(self, naam, prijs, voorraad):
        self.naam = naam
        self.prijs = prijs
        self.voorraad = voorraad

    def verlaag_voorraad(self, aantal):
        if aantal <= 0:
            return False
        if self.voorraad >= aantal:
            self.voorraad -= aantal
            return True
        else:
            return False


class Winkelmandje:
    def __init__(self):
        self.items = []  # lijst van tuples (Product, aantal)

    def voeg_toe(self, product, aantal):
        if product.verlaag_voorraad(aantal):
            self.items.append((product, aantal))
            return True
        else:
            return False

    def totaal_prijs(self):
        return sum(p.prijs * aantal for p, aantal in self.items)