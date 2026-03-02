class Student:
    def __init__(self, naam, leeftijd):
        self.naam = naam
        self.leeftijd = leeftijd

    def is_volwassen(self):
        return self.leeftijd >= 18


# Stap 2: drie student-objecten maken
s1 = Student("Ali", 19)
s2 = Student("Sara", 20)
s3 = Student("Jan", 17)

# Stap 3: studenten in een lijst zetten
studenten = [s1, s2, s3]

# Stap 6: teller voor 18+
aantal_volwassen = 0

# Stap 4 en 5: for-loop gebruiken
for student in studenten:
    print("Naam:", student.naam)
    print("Leeftijd:", student.leeftijd)
    print("Volwassen:", student.is_volwassen())
    print("------------------")

    if student.is_volwassen():
        aantal_volwassen += 1

# Stap 6: totaal printen
print("Aantal studenten van 18 jaar of ouder:", aantal_volwassen)