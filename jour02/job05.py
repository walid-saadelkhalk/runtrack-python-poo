class Voiture:
    #constructeur
    def __init__ (self, marque, annee, kilometrage, en_marche = False, reservoir = 50):
        self.__marque = marque
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = en_marche
        self.__reservoir = reservoir

    #getters
    def get_marque(self):
        return self.__marque

    def get_annee(self):
        return self.__annee

    def get_kilometrage(self):
        return self.__kilometrage

    def get_en_marche(self):
        return self.__en_marche

    def get_reservoir(self):
        return self.__reservoir


    #setters
    def set_marque(self, new_marque):
        self.__marque = new_marque

    def set_annee(self, new_annee):
        self.__annee = new_annee

    def set_kilometrage(self, new_kilometrage):
        self.__kilometrage = new_kilometrage

    def set_en_marche(self, new_en_marche):
        self.__en_marche = new_en_marche

    def set_reservoir(self, new_reservoir):
        self.__reservoir = new_reservoir



    #autres methodes
    def demarrer(self):
        if self.__verifier_plein() == True:
            self.__en_marche = True
            return self.__en_marche
        else:
            print("reservoir vide")

    def arreter(self):
        if self.__en_marche == True:
            self.__en_marche = False
            return self.__en_marche

    def __verifier_plein(self):
        return self.__reservoir > 5


voiture1 = Voiture("Renault", 2005, 100000, True, 2)
print(f"la voiture {voiture1.get_marque()} de l'annee {voiture1.get_annee()} a {voiture1.get_kilometrage()} km au compteur")

voiture1.demarrer()
voiture1.arreter()

voiture1.set_marque("Peugeot")
voiture1.set_annee(2010)
voiture1.set_kilometrage(150000)
voiture1.set_en_marche(True)
voiture1.set_reservoir(10)
print(f"la voiture {voiture1.get_marque()} de l'annee {voiture1.get_annee()} a {voiture1.get_kilometrage()} km au compteur")
voiture1.demarrer()
voiture1.arreter()
print(voiture1.demarrer())