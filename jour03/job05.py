import random

class Personnage:
    # Constructeur
    def __init__(self, nom, vie=100):
        self.__nom = nom
        self.__vie = vie

    # Nom
    def get_nom(self):
        return self.__nom

    def set_nom(self, nom):
        self.__nom = nom

    # Vie
    def get_vie(self):
        return self.__vie

    def set_vie(self, vie):
        self.__vie = max(vie, 0)

    # Autres méthodes
    def attaquer(self, pv_personnage):
        affiche_degats = random.randint(1, 10)  
        pv_personnage.set_vie(pv_personnage.get_vie() - affiche_degats)
        return affiche_degats
    




class Jeu:
    # Constructeur
    def __init__(self):
        self.niveau = 1

    # Niveau
    def choisirNiveau(self):
        self.niveau = int(input("Choisissez le niveau de difficulte (1, 2, 3): "))
        while self.niveau < 1 or self.niveau > 3:
            print("Niveau incorrect.")
            self.niveau = int(input("Choisissez le niveau de difficulte (1, 2, 3): "))
        if self.niveau == 1:
            gojo = Personnage("Gojo", 100)
            sukuna = Personnage("Sukuna", 75)
            print("Niveau facile.")
        elif self.niveau == 2:
            gojo = Personnage("Gojo", 100)
            sukuna = Personnage("Sukuna", 100)
            print("Niveau moyen.")
        elif self.niveau == 3:
            gojo = Personnage("Gojo", 100)
            sukuna = Personnage("Sukuna", 125)
            print("Niveau difficile.")
        return gojo, sukuna

    # Lancer jeu
    def lancerJeu(self):
        gojo, sukuna = self.choisirNiveau()
        print(f"Vous affrontez Sukuna au niveau {self.niveau}.\nLa vie de {gojo.get_nom()} est a {gojo.get_vie()} pv \nLa vie de {sukuna.get_nom()} est a {sukuna.get_vie()} pv\n")

        while gojo.get_vie() > 0 and sukuna.get_vie() > 0:
            degats_gojo = gojo.attaquer(sukuna)
            if sukuna.get_vie() <= 0:
                print(f"{sukuna.get_nom()} a ete vaincu ! Vous avez gagne.")
                break

            degats_sukuna = sukuna.attaquer(gojo)
            if gojo.get_vie() <= 0:
                print(f"{gojo.get_nom()} a ete vaincu ! Vous avez perdu.")
                break

            print(f"L'attaque de Sukuna a fait {degats_sukuna} pv de degats a Gojo: la vie de {gojo.get_nom()} est a {gojo.get_vie()} pv \n\nL'attaque de Gojo a fait {degats_gojo} pv de degats a Sukuna: la vie de {sukuna.get_nom()} est a {sukuna.get_vie()} pv\n")


jeu = Jeu()
jeu.lancerJeu()
