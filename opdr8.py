# Parent class
class Persoon:
    def __init__(self, naam):
        self.naam = naam

    def voorstel(self):
        print(f"Ik ben {self.naam}.")


# Child class Student
class Student(Persoon):
    def __init__(self, naam, leeftijd, opleiding):
        super().__init__(naam)  # roept __init__ van Persoon aan
        self.leeftijd = leeftijd
        self.opleiding = opleiding

    # Override van voorstel()
    def voorstel(self):
        print(f"Ik ben {self.naam}, {self.leeftijd} jaar, opleiding: {self.opleiding}.")


# Child class Docent
class Docent(Persoon):
    def __init__(self, naam, vak):
        super().__init__(naam)  # naam instellen via Persoon
        self.vak = vak

    # Override van voorstel()
    def voorstel(self):
        print(f"Ik ben {self.naam} en ik geef {self.vak}.")


# ---------------- TESTCODE ----------------

s1 = Student("Sara", 20, "Software Development")
d1 = Docent("Ali", "Python")

s1.voorstel()
d1.voorstel()