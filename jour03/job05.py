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
        pv_personnage.set_vie(pv_personnage.get_vie() - random.randint(5, 10))
        print(f"{self.__nom} attaque {pv_personnage.get_nom()}")
        print(f"{pv_personnage.get_nom()} a {pv_personnage.get_vie()} pv")


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
                sukuna = Personnage("Sukuna", 50)
                print("Niveau facile.")
            elif self.niveau == 2:
                gojo = Personnage("Gojo", 100)
                sukuna = Personnage("Sukuna", 75)
                print("Niveau moyen.")
            elif self.niveau == 3:
                gojo = Personnage("Gojo", 100)
                sukuna = Personnage("Sukuna", 120)
                print("Niveau difficile.")


    # Lancer jeu
    def lancerJeu(self):
        gojo = Personnage("Gojo", self.choisirNiveau())
        sukuna = Personnage("Sukuna", self.choisirNiveau())
        print(f"Vous affrontez Sukuna au niveau {self.niveau}.")

        while gojo.get_vie() > 0 and sukuna.get_vie() > 0:
            gojo.attaquer(sukuna)
            if sukuna.get_vie() <= 0:
                print(f"{sukuna.get_nom()} a ete vaincu ! Vous avez gagne.")
                break

            sukuna.attaquer(gojo)
            if gojo.get_vie() <= 0:
                print(f"{gojo.get_nom()} a ete vaincu ! Vous avez perdu.")
                break

            print(f"{gojo.get_nom()} Vie : {gojo.get_vie()} \n {sukuna.get_nom()} Vie : {sukuna.get_vie()}")



jeu = Jeu()

jeu.choisirNiveau()
jeu.lancerJeu()
