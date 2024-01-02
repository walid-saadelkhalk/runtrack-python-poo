class Animal:
    def __init__(self, age = 0, prenom=""):
        self.age = age
        self.prenom = prenom

    def year(self):
        print(f"L'age de l'animal {self.age} ans")

    def vieillir(self):
        self.age += 1
        print(f"L'age de l'animal {self.age} ans")

    def nommer(self):
        print(f"L'animal se nomme {self.prenom}")


chien = Animal(5, "Rex")

chien.year()
chien.vieillir()
chien.nommer()