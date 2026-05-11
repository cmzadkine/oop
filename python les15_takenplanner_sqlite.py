import sqlite3


# database verbinden / maken
def connect_db():

    return sqlite3.connect("taken.db")


# tabel maken
def init_db():

    conn = connect_db()

    conn.execute("""

        CREATE TABLE IF NOT EXISTS taken (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            titel TEXT NOT NULL,

            klaar INTEGER NOT NULL DEFAULT 0

        )

    """)

    conn.close()


# taak toevoegen
def add_taak(titel):

    conn = connect_db()

    conn.execute(
        "INSERT INTO taken (titel, klaar) VALUES (?, 0)",
        (titel,)
    )

    conn.commit()

    conn.close()


# taken ophalen
def get_taken():

    conn = connect_db()

    rows = conn.execute(
        "SELECT id, titel, klaar FROM taken"
    ).fetchall()

    conn.close()

    return rows


# taak markeren als klaar
def markeer_klaar(taak_id):

    conn = connect_db()

    conn.execute(
        "UPDATE taken SET klaar = 1 WHERE id = ?",
        (taak_id,)
    )

    conn.commit()

    conn.close()


# taak verwijderen
def verwijder_taak(taak_id):

    conn = connect_db()

    conn.execute(
        "DELETE FROM taken WHERE id = ?",
        (taak_id,)
    )

    conn.commit()

    conn.close()


# taken tonen
def toon_taken():

    taken = get_taken()

    if not taken:

        print("(geen taken)")

        return

    for taak_id, titel, klaar in taken:

        status = "✅" if klaar == 1 else "⬜"

        print(f"{taak_id}. {status} {titel}")


# hoofdprogramma
def main():

    init_db()

    while True:

        print("\n=== takenplanner (sqlite) ===")

        print("1) toon taken")

        print("2) voeg taak toe")

        print("3) markeer taak als klaar")

        print("4) verwijder taak")

        print("0) stoppen")

        keuze = input("kies: ").strip()

        # taken tonen
        if keuze == "1":

            toon_taken()

        # taak toevoegen
        elif keuze == "2":

            titel = input("taak titel: ").strip()

            if titel == "":

                print("titel mag niet leeg zijn.")

            else:

                add_taak(titel)

                print("taak toegevoegd!")

        # taak klaar zetten
        elif keuze == "3":

            toon_taken()

            taak_id = input("welke id klaar zetten: ").strip()

            if taak_id.isdigit():

                markeer_klaar(int(taak_id))

                print("taak gemarkeerd als klaar!")

            else:

                print("ongeldig id.")

        # taak verwijderen
        elif keuze == "4":

            toon_taken()

            taak_id = input("welke id verwijderen: ").strip()

            if taak_id.isdigit():

                verwijder_taak(int(taak_id))

                print("taak verwijderd!")

            else:

                print("ongeldig id.")

        # stoppen
        elif keuze == "0":

            print("tot ziens!")

            break

        else:

            print("ongeldige keuze.")


# startpunt
if __name__ == "__main__":

    main()