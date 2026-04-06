# les14_eindproject_takenplanner.py

import json
from pathlib import Path
from dataclasses import dataclass, asdict

# --- Taak class ---
@dataclass
class Taak:
    titel: str
    klaar: bool = False

    def markeer_klaar(self):
        self.klaar = True

    def to_dict(self):
        return asdict(self)

    @staticmethod
    def from_dict(data):
        return Taak(data["titel"], data["klaar"])


# --- Takenlijst class ---
class Takenlijst:
    def __init__(self, filename="taken.json"):
        self.taken = []
        self.filename = filename

    def voeg_toe(self, titel):
        if not titel.strip():
            print("Titel mag niet leeg zijn.")
            return
        self.taken.append(Taak(titel))
        print(f"Taak '{titel}' toegevoegd.")

    def toon(self):
        if not self.taken:
            print("Geen taken.")
            return
        print("\n--- Takenlijst ---")
        for i, taak in enumerate(self.taken, 1):
            status = "✅" if taak.klaar else "⬜"
            print(f"{i}. {status} {taak.titel}")

    def markeer_klaar(self, index):
        if 0 <= index < len(self.taken):
            self.taken[index].markeer_klaar()
            print(f"Taak '{self.taken[index].titel}' gemarkeerd als klaar.")
        else:
            print("Ongeldig nummer.")

    def verwijder(self, index):
        if 0 <= index < len(self.taken):
            removed = self.taken.pop(index)
            print(f"Taak '{removed.titel}' verwijderd.")
        else:
            print("Ongeldig nummer.")

    def save(self):
        data = [t.to_dict() for t in self.taken]
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=2)
        print("Taken opgeslagen.")

    def load(self):
        if not Path(self.filename).exists():
            return
        with open(self.filename) as f:
            data = json.load(f)
            self.taken = [Taak.from_dict(d) for d in data]


# --- Hulpfuncties ---
def vraag_int(prompt, min_val, max_val):
    try:
        waarde = int(input(prompt))
        if min_val <= waarde <= max_val:
            return waarde
        else:
            print(f"Voer een getal in tussen {min_val} en {max_val}.")
            return None
    except ValueError:
        print("Ongeldige invoer, voer een getal in.")
        return None


# --- Main menu ---
def main():
    lijst = Takenlijst()
    lijst.load()

    while True:
        print("\n--- Takenplanner ---")
        print("1: Toon taken")
        print("2: Voeg taak toe")
        print("3: Markeer taak als klaar")
        print("4: Verwijder taak")
        print("0: Stoppen (opslaan)")

        keuze = input("Kies: ").strip()
        if keuze == "1":
            lijst.toon()
        elif keuze == "2":
            titel = input("Titel van de taak: ").strip()
            lijst.voeg_toe(titel)
        elif keuze == "3":
            if not lijst.taken:
                print("Geen taken om te markeren.")
                continue
            lijst.toon()
            nummer = vraag_int("Welke taak wil je markeren? ", 1, len(lijst.taken))
            if nummer is not None:
                lijst.markeer_klaar(nummer-1)
        elif keuze == "4":
            if not lijst.taken:
                print("Geen taken om te verwijderen.")
                continue
            lijst.toon()
            nummer = vraag_int("Welke taak wil je verwijderen? ", 1, len(lijst.taken))
            if nummer is not None:
                lijst.verwijder(nummer-1)
        elif keuze == "0":
            lijst.save()
            print("Programma afgesloten.")
            break
        else:
            print("Ongeldige keuze.")


if __name__ == "__main__":
    main()