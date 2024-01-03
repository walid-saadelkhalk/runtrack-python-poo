class Livre: 
    def __init__(self, auteur, titre, page, disponible = True):
        self.__auteur = auteur
        self.__titre = titre
        self.__page = page
        self.__disponible = disponible

    def get_auteur(self):
        return self.__auteur

    def get_titre(self):
        return self.__titre

    def get_page(self):
        return self.__page

    def get_disponible(self):
        return self.__disponible

    def set_auteur(self, new_auteur):
        self.__auteur = new_auteur

    def set_titre(self, new_titre):
        self.__titre = new_titre


    def set_page(self, new_page):
        
        if new_page > 0 and type(new_page) == int:
            self.__page = new_page
            return self.__page
        else:
            print("Erreur: nombre de pages négatif et/ ou non entier")

    def set_disponible(self, new_disponible):
        self.__disponible = new_disponible


    def verification(self):
        if self.__disponible == True:
            return True
        return False


    def emprunter(self):
        if self.verification():
            self.set_disponible(False)
        else:
            print("Le livre n'est pas disponible")

    def rendre(self):
        if self.verification() == False:
            self.set_disponible(True)
            return "Le livre n'a pas été rendu" 
        else:
            print("Le livre est de nouveau disponible")


livre1 = Livre("Victor Hugo", "Les Misérables", 1488)
livre1.emprunter()
print(f"le livre {livre1.get_titre()} de {livre1.get_auteur()} contient {livre1.get_page()} pages")



livre1.set_auteur("Kishimoto")
livre1.set_titre("Naruto")
livre1.set_page(1000)
livre1.set_disponible(False)
print(f"le livre {livre1.get_titre()} de {livre1.get_auteur()} contient {livre1.get_page()} pages")
livre1.emprunter()

livre1.set_auteur("Sun Tzu")
livre1.set_titre("L'art de la guerre")
livre1.set_page(100)
livre1.set_disponible(True)
print(f"le livre {livre1.get_titre()} de {livre1.get_auteur()} contient {livre1.get_page()} pages")
livre1.rendre()


