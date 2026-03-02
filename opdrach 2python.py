class Student:
    def __init__(self, naam, leeftijd, opleiding):
        self.naam = naam
        self.leeftijd = leeftijd
        self.opleiding = opleiding

    def begroet(self):
        print(f"Hallo, ik ben {self.naam}, ik ben {self.leeftijd} jaar en ik volg de opleiding {self.opleiding}.")


# Student 1
student1 = Student("Ali", 19, "Software Developer")
student1.begroet()

# Student 2
student2 = Student("Sara", 21, "Cyber Security")
student2.begroet()