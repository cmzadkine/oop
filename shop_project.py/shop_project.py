import datetime

# -------------------------
# Stap 2 & 3: Product class
# -------------------------
class Product:
    def __init__(self, naam, prijs, voorraad):
        self.naam = naam
        self.prijs = prijs
        self._voorraad = voorraad

    def toon_info(self):
        print(f"{self.naam} - €{self.prijs} (voorraad: {self._voorraad})")

    def is_op_voorraad(self, aantal=1):
        return self._voorraad >= aantal

    def verlaag_voorraad(self, aantal):
        if aantal <= 0:
            print("Aantal moet groter dan 0 zijn.")
            return False
        if self._voorraad < aantal:
            print(f"Niet genoeg voorraad voor {self.naam}. Alleen {self._voorraad} beschikbaar.")
            return False
        self._voorraad -= aantal
        return True

# -------------------------
# Stap 4 & 5: Winkelmandje
# -------------------------
class Winkelmandje:
    def __init__(self):
        # items wordt lijst van tuples: (product, aantal)
        self.items = []

    def voeg_toe(self, product, aantal):
        if aantal <= 0:
            print("Aantal moet groter dan 0 zijn.")
            return
        if not product.is_op_voorraad(aantal):
            print(f"Niet genoeg voorraad voor {product.naam}.")
            return
        self.items.append((product, aantal))
        print(f"Toegevoegd: {product.naam} x{aantal}")

    def toon_mandje(self):
        if not self.items:
            print("Mandje is leeg.")
            return
        print("In je mandje:")
        for idx, (product, aantal) in enumerate(self.items, 1):
            subtotal = product.prijs * aantal
            print(f"{idx}. {product.naam} x{aantal} - €{subtotal}")
        print(f"Totaal: €{self.totaal_prijs()}")

    def totaal_prijs(self):
        totaal = sum(product.prijs * aantal for product, aantal in self.items)
        return totaal

    def leeg_mandje(self):
        self.items = []

# -------------------------
# Stap 6: Startproducten
# -------------------------
producten = [
    Product("Laptop", 899, 3),
    Product("Muis", 25, 10),
    Product("Toetsenbord", 59, 5),
]

mandje = Winkelmandje()

# -------------------------
# Stap 7 & 8: Menuloop
# -------------------------
while True:
    print("\n--- Mini Webshop ---")
    print("1 = Producten bekijken")
    print("2 = Product toevoegen")
    print("3 = Mandje bekijken")
    print("4 = Afrekenen")
    print("0 = Stoppen")

    keuze = input("Kies: ")

    if keuze == "1":
        print("\nBeschikbare producten:")
        for idx, product in enumerate(producten, 1):
            print(f"{idx}. ", end="")
            product.toon_info()

    elif keuze == "2":
        print("\nWelk product wil je toevoegen?")
        for idx, product in enumerate(producten, 1):
            print(f"{idx}. {product.naam} - €{product.prijs} (voorraad: {product._voorraad})")
        try:
            nummer = int(input("Kies productnummer: "))
            if nummer < 1 or nummer > len(producten):
                print("Ongeldig productnummer.")
                continue
            product = producten[nummer - 1]
            aantal = int(input(f"Hoeveel {product.naam} wil je toevoegen? "))
            mandje.voeg_toe(product, aantal)
        except ValueError:
            print("Ongeldige invoer, probeer opnieuw.")

    elif keuze == "3":
        mandje.toon_mandje()

    elif keuze == "4":
        if not mandje.items:
            print("Mandje is leeg, kan niet afrekenen.")
            continue

        # Check voorraad voor alle items
        voorraad_ok = True
        for product, aantal in mandje.items:
            if not product.is_op_voorraad(aantal):
                print(f"Niet genoeg voorraad voor {product.naam}. Afrekenen gestopt.")
                voorraad_ok = False
        if not voorraad_ok:
            continue

        # Bereken totaal en korting
        totaal = mandje.totaal_prijs()
        korting = 0
        if totaal > 500:
            korting = totaal * 0.10
            totaal_korting = totaal - korting
            print(f"10% korting toegepast! Nieuw totaal: €{totaal_korting:.2f}")
        else:
            totaal_korting = totaal

        # Voorraad verlagen
        for product, aantal in mandje.items:
            product.verlaag_voorraad(aantal)

        # Bonnetje opslaan
        now = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        bon_filename = f"bonnetje_{now}.txt"
        with open(bon_filename, "w") as f:
            f.write(f"--- Bonnetje {now} ---\n")
            for product, aantal in mandje.items:
                subtotal = product.prijs * aantal
                f.write(f"{product.naam} x{aantal} - €{subtotal}\n")
            f.write(f"Totaal: €{totaal}\n")
            if korting > 0:
                f.write(f"Korting: €{korting:.2f}\n")
                f.write(f"Eindbedrag: €{totaal_korting:.2f}\n")
            else:
                f.write(f"Eindbedrag: €{totaal_korting:.2f}\n")

        print(f"Bedankt voor je aankoop! Bonnetje opgeslagen als {bon_filename}")
        mandje.leeg_mandje()

    elif keuze == "0":
        print("Webshop afgesloten. Tot ziens!")
        break

    else:
        print("Ongeldige keuze, probeer opnieuw.")