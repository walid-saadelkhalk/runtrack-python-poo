class Personne:
#constructeur
    def __init__(self, age = 14):
        self.age = age

#age
    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    #autres methodes
    def afficherAge(self):
        return f"age: {self.age} ans"

    def bonjour(self):
        return "Hello"

    def modifierAge(self):
        age = int(input("Entrez l'age a modifier:"))
        self.age = age
        return f"nouvel age: {self.age} ans"

class Eleve(Personne):
    def __init__(self, age = 14):
        Personne.__init__(self, age)

    def allerEnCours(self):
        return "Je vais en cours"

    def afficherAge(self):
        return f"J'ai {self.age} ans"

class Professeur(Personne):
    def __init__(self, matiere_Enseignee, age = 14):
        Personne.__init__(self, age)
        self.matiere_Enseignee = matiere_Enseignee

    #matiere enseignee
    def get_matiere_Enseignee(self):
        return self._matiere_Enseignee

    def set_matiere_Enseignee(self, matiere_Enseignee):
        self._matiere_Enseignee = matiere_Enseignee

    #autres methodes
    def enseigner(self):
        return "Le cours va commencer"    


prof1 = Professeur("Maths")
prof1.set_age(40)
print(prof1.afficherAge())
print(prof1.bonjour())
print(prof1.enseigner())

eleve1 = Eleve()
print(eleve1.bonjour())
print(eleve1.allerEnCours())
print(eleve1.modifierAge())
print(eleve1.afficherAge())


        