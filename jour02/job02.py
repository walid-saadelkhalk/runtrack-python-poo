class Livre: 
    def __init__(self, auteur, titre, page):
        self.__auteur = auteur
        self.__titre = titre
        self.__page = page

    def get_auteur(self):
        return self.__auteur

    def get_titre(self):
        return self.__titre

    def get_page(self):
        return self.__page

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


livre1 = Livre("Victor Hugo", "Les Misérables", 1488)
print(f"le livre {livre1.get_titre()} de {livre1.get_auteur()} contient {livre1.get_page()} pages")

livre1.set_auteur("Kishimoto")
livre1.set_titre("Naruto")
livre1.set_page(1000.7)
livre1.set_page(-1000)
livre1.set_page(1000)
print(f"le livre {livre1.get_titre()} de {livre1.get_auteur()} contient {livre1.get_page()} pages")
