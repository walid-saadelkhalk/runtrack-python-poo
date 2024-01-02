class Cercle:
    def __init__(self, rayon = 0):
        self.rayon = rayon

    def changerRayon(self):
        changement_rayon = int(input("Entrez le nouveau rayon: "))
        self.rayon = changement_rayon
        

    def afficherInfos(self):
        print(f"le rayon est: {self.rayon}")
        

    def circonference(self):
        circonference_cercle = self.rayon * 2 * 3.14
        print(f"le perimetre est: {self.rayon * 2 * 3.14}")

    def aire(self):
        aire_cercle = self.rayon * self.rayon * 3.14
        print(f"la surface est: {self.rayon * self.rayon * 3.14}")

    def diametre(self):
        diametre_cercle = self.rayon * 2
        print(f"le diametre est: {self.rayon * 2}")

cercle_1 = Cercle()
cercle_1.changerRayon()
cercle_1.afficherInfos()
cercle_1.circonference()
cercle_1.aire()
cercle_1.diametre()

cercle_2 = Cercle()
cercle_2.changerRayon()
cercle_2.afficherInfos()
cercle_2.circonference()
cercle_2.aire()
cercle_2.diametre()


