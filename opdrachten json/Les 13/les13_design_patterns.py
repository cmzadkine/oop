# les13_design_patterns.py

# --- Product ---
class Product:
    def __init__(self, naam, prijs):
        self.naam = naam
        self.prijs = prijs

    def __repr__(self):
        return f"{self.naam} (€{self.prijs})"


# --- Factory Pattern ---
class ProductFactory:
    def maak_product(self, soort):
        soort = soort.lower()
        if soort == "laptop":
            return Product("Laptop", 899)
        elif soort == "muis":
            return Product("Muis", 25)
        elif soort == "toetsenbord":
            return Product("Toetsenbord", 59)
        else:
            raise ValueError(f"Onbekend product: {soort}")


# --- Strategy Pattern voor korting ---
class KortingRegel:
    def pas_toe(self, totaal):
        """Interface-methode"""
        raise NotImplementedError


class GeenKorting(KortingRegel):
    def pas_toe(self, totaal):
        return 0


class TienProcentBoven500(KortingRegel):
    def pas_toe(self, totaal):
        if totaal > 500:
            return totaal * 0.10
        return 0


# --- Kassa ---
class Kassa:
    def __init__(self, korting_regel):
        self.producten = []
        self.korting_regel = korting_regel

    def voeg_toe(self, product):
        self.producten.append(product)

    def totaal(self):
        return sum(p.prijs for p in self.producten)

    def korting(self):
        return self.korting_regel.pas_toe(self.totaal())

    def eindbedrag(self):
        return self.totaal() - self.korting()


# --- Demo ---
if __name__ == "__main__":
    factory = ProductFactory()
    kassa = Kassa(TienProcentBoven500())

    # Voeg producten toe via factory
    kassa.voeg_toe(factory.maak_product("laptop"))
    kassa.voeg_toe(factory.maak_product("muis"))
    kassa.voeg_toe(factory.maak_product("toetsenbord"))
    kassa.voeg_toe(factory.maak_product("muis"))

    # Print overzicht
    print("Producten in kassa:", kassa.producten)
    print(f"Subtotaal: €{kassa.totaal():.2f}")
    print(f"Korting: €{kassa.korting():.2f}")
    print(f"Eindbedrag: €{kassa.eindbedrag():.2f}")