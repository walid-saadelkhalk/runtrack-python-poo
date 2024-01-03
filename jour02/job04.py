class Student: 
    #constructeur
    def __init__(self, nom, prenom, nie, credits = 0):
        self.__nom = nom
        self.__prenom = prenom
        self.__nie = nie
        self.__credits = credits
        self.__level = self.__studentEval()


    #getters
    def get_nom(self):
        return self.__nom

    def get_prenom(self):
        return self.__prenom

    def get_nie(self):
        return self.__nie

    def get_credits(self):
        return self.__credits

    def get_level(self):
        return self.__level


    #setters
    def set_nom(self, new_nom):
        self.__nom = new_nom

    def set_prenom(self, new_prenom):
        self.__prenom = new_prenom

    def set_nie(self, new_nie):
        self.__nie = new_nie

    def set_credits(self, new_credits):
        self.__credits = new_credits

    def set_level(self, new_level):
        self.__level = new_level


    #autres methodes
    def add_credits(self, ajout_credits):
        if ajout_credits > 0 and type(ajout_credits) == int:
            self.__credits = self.get_credits() + ajout_credits 
            self.__level = self.__studentEval()
            return self.__credits
        else:
            print("Erreur: nombre de crédits négatif et/ ou non entier")

    def __studentEval (self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80 and self.__credits < 90:
            return "Très bien" 
        elif self.__credits >= 70 and self.__credits < 80:
            return "Bien"
        elif self.__credits >= 60 and self.__credits < 70:
            return "Passable"
        else:
            return "Insuffisant"

    def studendInfo(self):
        print(f"Nom = {self.get_nom()}\nPrenom = {self.get_prenom()}\nId = {self.get_nie()}\nNiveau: {self.get_level()}")



john = Student("Doe", "John", 145)
print(f"Le nombre de credits de {john.get_prenom()} {john.get_nom()} est de {john.get_credits()} points")
john.add_credits(10)
john.studendInfo()
print(f"Le nombre de credits de {john.get_prenom()} {john.get_nom()} est de {john.get_credits()} points")
john.add_credits(-10)

john.studendInfo()
print(f"Le nombre de credits de {john.get_prenom()} {john.get_nom()} est de {john.get_credits()} points")
john.add_credits(50)
john.studendInfo()
print(f"Le nombre de credits de {john.get_prenom()} {john.get_nom()} est de {john.get_credits()} points")
john.add_credits(10)
john.studendInfo()
print(f"Le nombre de credits de {john.get_prenom()} {john.get_nom()} est de {john.get_credits()} points")
john.add_credits(10)
john.studendInfo()
print(f"Le nombre de credits de {john.get_prenom()} {john.get_nom()} est de {john.get_credits()} points")
john.add_credits(10)
john.studendInfo()
print(f"Le nombre de credits de {john.get_prenom()} {john.get_nom()} est de {john.get_credits()} points")
