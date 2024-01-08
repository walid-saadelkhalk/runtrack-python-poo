import random

class Carte: 
    def __init__(self):
        self.valeur = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Valet", "Dame", "Roi", "As"]
        self.couleur = ["Coeur", "Carreau", "Pique", "Trefle"]

    def tas_de_cartes(self):
        paquet = []
        for i in self.valeur:
            for j in self.couleur:
                paquet.append(i + " de " + j)
        return paquet




class Jeu(Carte):
    def __init__(self, paquet):
        self.paquet = paquet
        self.player = []
        self.points = 0

    def tirer_cartes(self):
        carte_tiree = random.choice(self.paquet)
        self.paquet.remove(carte_tiree)
        return carte_tiree

    def calcul_de_points(self, partie=None):
        points = 0
        partie_a_calculer = self.player if partie is None else partie
        for carte in partie_a_calculer:
            valeur_carte = carte.split(" ")[0]
            if valeur_carte.isdigit() or valeur_carte == "10":
                points += int(valeur_carte)
            elif valeur_carte in ["Valet", "Dame", "Roi"]:
                points += 10
            elif valeur_carte == "As" and points < 11:
                points += 11
            elif valeur_carte == "As" and points >= 11:
                points += 1
        return points




class Joueur(Jeu):
    def __init__(self, paquet):
        Jeu.__init__(self, paquet)
        self.croupier = []


    #joueur
    def se_faire_plumer(self):
        self.player = [self.tirer_cartes(), self.tirer_cartes()]
        print("Vous avez : ", self.player)

        while self.calcul_de_points() < 21:
            reponse = input("Voulez-vous une autre carte ? (oui/non) ")
            if reponse.lower() == "oui":
                self.player.append(self.tirer_cartes())
                print("Vous avez :", self.player)
            elif reponse.lower() == "non":
                break
            else:
                return "Veuillez entrer une réponse valide"

        points = self.calcul_de_points()
        print(f"Vous avez {points} points")

        if points > 21:
            return "Vous avez perdu !"
        elif points == 21:
            return "Vous avez gagné !"

        return points



    #croupier
    def casino(self):
        self.croupier = [self.tirer_cartes(), self.tirer_cartes()]

        while self.calcul_de_points(self.croupier) < 17:
            self.croupier.append(self.tirer_cartes())
            print("Le croupier a :", self.croupier)
            

            print(f"Le croupier a {self.calcul_de_points(self.croupier)} points")

            if self.calcul_de_points(self.croupier) > 21:
                break 

        return self.calcul_de_points(self.croupier)



    #affrontement joueur/croupier
    def affronter(self):
        result_plumer = self.se_faire_plumer()
        result_casino = self.casino()

        if isinstance(result_plumer, int) and isinstance(result_casino, int):
            if result_plumer > 21 and result_casino > 21:
                return "Vous avez perdu !"
            elif result_plumer > 21 and result_casino <= 21:
                return "Le croupier a gagné !"
            elif result_plumer <= 21 and result_casino > 21:
                return "Vous avez gagné !"
            elif result_plumer > result_casino:
                return "Vous avez gagné !"
            elif result_plumer < result_casino:
                return "Le croupier a gagné !"
            else:
                return "Égalité !"
        else:
            return result_plumer




paquet = Carte().tas_de_cartes()

joueur1 = Joueur(paquet)
print(joueur1.affronter())
