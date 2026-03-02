class Student:
    def __init__(self, naam, leeftijd):
        self.naam = naam
        self._leeftijd = leeftijd  # protected (conventie)

    # Getter
    def get_leeftijd(self):
        return self._leeftijd

    # Setter met validatie
    def set_leeftijd(self, nieuwe_leeftijd):
        if nieuwe_leeftijd < 0:
            print("Leeftijd mag niet negatief zijn!")
            return
        if nieuwe_leeftijd > 130:
            print("Leeftijd is niet realistisch!")
            return

        self._leeftijd = nieuwe_leeftijd

    # Oefening 2 — verjaar methode
    def verjaar(self):
        huidige_leeftijd = self.get_leeftijd()
        nieuwe_leeftijd = huidige_leeftijd + 1
        self.set_leeftijd(nieuwe_leeftijd)


# ---------------- TESTCODE ----------------

s1 = Student("Ali", 19)

# Huidige leeftijd
print("Leeftijd:", s1.get_leeftijd())

# Geldige wijziging
s1.set_leeftijd(20)
print("Nieuwe leeftijd:", s1.get_leeftijd())

# Ongeldige wijziging (negatief)
s1.set_leeftijd(-5)
print("Na foute invoer:", s1.get_leeftijd())

# Ongeldige wijziging (boven 130)
s1.set_leeftijd(200)
print("Na onrealistische invoer:", s1.get_leeftijd())

# Verjaardag testen
s1.verjaar()
print("Na verjaar():", s1.get_leeftijd())