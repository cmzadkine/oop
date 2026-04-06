# winkel.py (alles in één bestand)

class Product:
    def __init__(self, naam, prijs, voorraad):
        self.naam = naam
        self.prijs = prijs
        self._voorraad = voorraad

    def toon_info(self):
        print(f"{self.naam} | €{self.prijs} | voorraad: {self._voorraad}")

    def is_op_voorraad(self, aantal=1):
        return self._voorraad >= aantal

    def verlaag_voorraad(self, aantal):
        if self.is_op_voorraad(aantal):
            self._voorraad -= aantal
        else:
            raise ValueError(f"Niet genoeg voorraad voor {self.naam}")


class Winkelmandje:
    def __init__(self):
        self.items = []  # lijst van tuples (Product, aantal)

    def voeg_toe(self, product, aantal):
        if product.is_op_voorraad(aantal):
            self.items.append((product, aantal))
            product.verlaag_voorraad(aantal)
            print(f"{aantal}x {product.naam} toegevoegd aan het mandje.")
        else:
            print(f"Kan niet toevoegen: onvoldoende voorraad voor {product.naam}.")

    def totaal_prijs(self):
        return sum(p.prijs * aantal for p, aantal in self.items)

    def toon(self):
        if not self.items:
            print("Winkelmandje is leeg.")
            return
        print("\n--- Winkelmandje ---")
        for p, aantal in self.items:
            print(f"{p.naam} | €{p.prijs} x {aantal} = €{p.prijs * aantal}")
        print(f"Totaal: €{self.totaal_prijs()}")


def vraag_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ongeldige invoer, probeer opnieuw.")


def main():
    producten = [
        Product("Laptop", 899, 3),
        Product("Muis", 25, 10),
        Product("Toetsenbord", 59, 5)
    ]

    mandje = Winkelmandje()

    while True:
        print("\n--- MENU ---")
        print("1: Toon producten")
        print("2: Voeg toe aan mandje")
        print("3: Toon mandje")
        print("0: Stoppen")

        keuze = vraag_int("Kies: ")

        if keuze == 1:
            for i, p in enumerate(producten, 1):
                print(f"{i}. ", end="")
                p.toon_info()

        elif keuze == 2:
            for i, p in enumerate(producten, 1):
                print(f"{i}. ", end="")
                p.toon_info()
            prod_nr = vraag_int("Welk product wil je toevoegen? (nummer) ") - 1
            if 0 <= prod_nr < len(producten):
                aantal = vraag_int("Aantal: ")
                mandje.voeg_toe(producten[prod_nr], aantal)
            else:
                print("Ongeldig productnummer.")

        elif keuze == 3:
            mandje.toon()

        elif keuze == 0:
            print("Programma gestopt.")
            break

        else:
            print("Ongeldige keuze.")


if __name__ == "__main__":
    main()