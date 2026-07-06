"""
main.py
-------
CLI-menu voor het Restaurant Reserveringssysteem.
Hier gebeurt alleen input/output; de logica zit in services/manager.py.
"""

from services.storage import ReserveringStorage
from services.manager import ReserveringManager


def vraag_int(prompt: str) -> int:
    """Blijft vragen totdat de gebruiker een geldig getal invoert."""
    while True:
        waarde = input(prompt).strip()
        try:
            return int(waarde)
        except ValueError:
            print("⚠️  Voer alsjeblieft een geldig getal in.")


def toon_menu() -> None:
    print("\n=== Restaurant Reserveringssysteem ===")
    print("1. Toon reserveringen")
    print("2. Voeg reservering toe")
    print("3. Verwijder reservering")
    print("4. Zoek reservering op naam")
    print("5. Filter reserveringen op datum")
    print("6. Stoppen")


def toon_reserveringen(reserveringen) -> None:
    if not reserveringen:
        print("Er zijn nog geen reserveringen.")
        return
    for i, r in enumerate(reserveringen):
        print(f"[{i}] {r}")


def voeg_reservering_toe(manager: ReserveringManager) -> None:
    naam = input("Naam: ").strip()
    datum = input("Datum (YYYY-MM-DD): ").strip()
    tijd = input("Tijd (HH:MM): ").strip()
    aantal = input("Aantal personen: ").strip()

    gelukt = manager.voeg_toe(naam, datum, tijd, aantal)
    if gelukt:
        print("✅ Reservering toegevoegd!")
    else:
        print("❌ Reservering NIET toegevoegd. Controleer je invoer "
              "(alle velden verplicht, aantal > 0, en check max capaciteit "
              f"van {30} personen per tijdslot).")


def verwijder_reservering(manager: ReserveringManager) -> None:
    toon_reserveringen(manager.alles())
    if not manager.alles():
        return
    index = vraag_int("Welke reservering wil je verwijderen? (nummer): ")
    if manager.verwijder(index):
        print("✅ Reservering verwijderd.")
    else:
        print("❌ Ongeldig nummer, niets verwijderd.")


def zoek_reservering(manager: ReserveringManager) -> None:
    zoekterm = input("Zoek op naam: ").strip()
    resultaten = manager.zoek_op_naam(zoekterm)
    toon_reserveringen(resultaten)


def filter_reservering(manager: ReserveringManager) -> None:
    datum = input("Filter op datum (YYYY-MM-DD): ").strip()
    resultaten = manager.filter_op_datum(datum)
    toon_reserveringen(resultaten)


def main() -> None:
    storage = ReserveringStorage("reserveringen.json")
    manager = ReserveringManager(storage)

    while True:
        toon_menu()
        keuze = input("Kies een optie (1-6): ").strip()

        if keuze == "1":
            toon_reserveringen(manager.alles())
        elif keuze == "2":
            voeg_reservering_toe(manager)
        elif keuze == "3":
            verwijder_reservering(manager)
        elif keuze == "4":
            zoek_reservering(manager)
        elif keuze == "5":
            filter_reservering(manager)
        elif keuze == "6":
            print("Tot ziens! 👋")
            break
        else:
            print("⚠️  Ongeldige keuze, probeer opnieuw.")


if __name__ == "__main__":
    main()
