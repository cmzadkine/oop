class Student:

    def __init__(self, naam, leeftijd):
        self.naam = naam
        self.leeftijd = leeftijd

    def begroet(self):
        print(f"Hallo, ik ben {self.naam}!")


# Stap 3 — lijst met studenten
studenten = [
    Student("Ali", 19),
    Student("Sara", 20),
    Student("Jan", 18),
]

# Stap 4 — loop en begroet()
for s in studenten:
    s.begroet()

print("------------------")

# Oefening deel 1 — tel hoeveel studenten 18+
aantal_18_plus = 0

for s in studenten:
    if s.leeftijd >= 18:
        aantal_18_plus += 1

print("Aantal studenten van 18 jaar of ouder:", aantal_18_plus)

print("------------------")

# Oefening deel 2 — gemiddelde leeftijd berekenen
totaal_leeftijd = 0

for s in studenten:
    totaal_leeftijd += s.leeftijd

gemiddelde = totaal_leeftijd / len(studenten)

print("Gemiddelde leeftijd:", gemiddelde)