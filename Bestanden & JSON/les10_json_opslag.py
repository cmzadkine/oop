# les10_json_opslag.py

import json
from pathlib import Path


class Product:
    def __init__(self, naam, prijs, voorraad):
        self.naam = naam
        self.prijs = prijs
        self._voorraad = voorraad

    def to_dict(self):
        return {
            "naam": self.naam,
            "prijs": self.prijs,
            "voorraad": self._voorraad
        }

    @staticmethod
    def from_dict(data):
        return Product(
            data["naam"],
            data["prijs"],
            data["voorraad"]
        )


def save_producten(producten, filename):
    data = [p.to_dict() for p in producten]
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)


def load_producten(filename):
    if not Path(filename).exists():
        return []
    with open(filename) as f:
        data = json.load(f)
    return [Product.from_dict(d) for d in data]


def vraag_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ongeldige invoer, probeer opnieuw.")


def vraag_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ongeldige invoer, probeer opnieuw.")


def toon_producten(producten):
    if not producten:
        print("Geen producten beschikbaar.")
        return

    print("\n--- Producten ---")
    for i, p in enumerate(producten, 1):
        print(f"{i}. {p.naam} | €{p.prijs} | voorraad: {p._voorraad}")


def main():
    filename = "producten.json"
    producten = load_producten(filename)

    # Eerste keer → standaard producten
    if not producten:
        producten = [
            Product("Muis", 25, 10),
            Product("Toetsenbord", 50, 5)
        ]

    while True:
        print("\n--- MENU ---")
        print("1: Toon producten")
        print("2: Product toevoegen")
        print("3: Opslaan")
        print("0: Stoppen")

        keuze = vraag_int("Kies: ")

        if keuze == 1:
            toon_producten(producten)

        elif keuze == 2:
            naam = input("Naam: ")
            prijs = vraag_float("Prijs: ")
            voorraad = vraag_int("Voorraad: ")

            nieuw_product = Product(naam, prijs, voorraad)
            producten.append(nieuw_product)

            print("Product toegevoegd!")

        elif keuze == 3:
            save_producten(producten, filename)
            print("Opgeslagen!")

        elif keuze == 0:
            save_producten(producten, filename)
            print("Programma gestopt en opgeslagen.")
            break

        else:
            print("Ongeldige keuze.")


if __name__ == "__main__":
    main()