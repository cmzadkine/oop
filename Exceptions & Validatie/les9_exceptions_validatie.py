# les9_exceptions_validatie.py

def vraag_int(prompt):
    while True:
        try:
            waarde = int(input(prompt))
            return waarde
        except ValueError:
            print("Ongeldige invoer, probeer opnieuw.")


def delen(a, b):
    if b == 0:
        raise ZeroDivisionError("Delen door 0 mag niet")
    return a / b


def main():
    while True:
        print("\n--- MENU ---")
        print("1: Optellen")
        print("2: Delen")
        print("0: Stoppen")

        try:
            keuze = vraag_int("Kies: ")

            if keuze == 0:
                print("Programma gestopt.")
                break

            elif keuze == 1:
                a = vraag_int("Geef eerste getal: ")
                b = vraag_int("Geef tweede getal: ")
                print(f"Resultaat: {a + b}")

            elif keuze == 2:
                a = vraag_int("Geef eerste getal: ")
                b = vraag_int("Geef tweede getal: ")
                resultaat = delen(a, b)
                print(f"Resultaat: {resultaat}")

            else:
                print("Ongeldige keuze.")

        except ZeroDivisionError as e:
            print(f"Fout: {e}")

        finally:
            print("Terug naar menu...")


if __name__ == "__main__":
    main()