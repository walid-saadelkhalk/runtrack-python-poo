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
        # Assurer que la vie ne devient pas négative
        self.__vie = max(vie, 0)

    # Autres méthodes
    def attaquer(self, pv_personnage):
        pv_personnage.set_vie(pv_personnage.get_vie() - 10)
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

    # Lancer jeu
    def lancerJeu(self):
        joueur = Personnage("Gojo", 100 * self.niveau)
        ennemi = Personnage("Sukuna", 99 * self.niveau)

        print(f"Vous affrontez Sukuna au niveau {self.niveau}.")

        while joueur.get_vie() > 0 and ennemi.get_vie() > 0:
            joueur.attaquer(ennemi)
            if ennemi.get_vie() <= 0:
                print(f"{ennemi.get_nom()} a ete vaincu ! Vous avez gagne.")
                break

            ennemi.attaquer(joueur)
            if joueur.get_vie() <= 0:
                print(f"{joueur.get_nom()} a ete vaincu ! Vous avez perdu.")
                break

            print(f"{joueur.get_nom()} Vie : {joueur.get_vie()} \n {ennemi.get_nom()} Vie : {ennemi.get_vie()}")



jeu = Jeu()

jeu.choisirNiveau()
jeu.lancerJeu()
