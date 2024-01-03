class Produit:
    def __init__(self, nom = "", prixHT = 0, TVA = 0):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA
    
    def CalculerPrixTTC(self):
        return self.prixHT + self.prixHT * self.TVA / 100

    def afficher(self):
        return f" le produit {self.nom} a un prix HT {self.prixHT}$. Pour une TVA de {self.TVA}% le prix coutera au final {self.CalculerPrixTTC()}$"

    def modificationNom(self):
        nom_modifie = input("Entrez le nouveau nom du produit: ")
        self.nom = nom_modifie

    def modificationPrixHT(self):
        prixHT_modifie = int(input("Entrez le nouveau prix HT: "))
        self.prixHT = prixHT_modifie

produit1 = Produit("Iphone", 1190, 20)
produit1.afficher()
print(produit1.afficher())

produit2 = Produit("Sneakers", 1000, 20)
produit2.afficher()
print(produit2.afficher())

produit3 = Produit("T-shirt", 100, 20)
produit3.afficher()
print(produit3.afficher())

produit4 = Produit("Ordinateur", 750, 20)
produit4.afficher()
print(produit4.afficher())





produit_modifie = Produit()
produit_modifie.modificationNom()
produit_modifie.modificationPrixHT()
print (produit_modifie.afficher())
