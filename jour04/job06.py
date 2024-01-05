class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    #marque
    def get_marque(self):
        return self.marque

    def set_marque(self, marque):
        self.marque = marque

    #modele
    def get_modele(self):
        return self.modele

    def set_modele(self, modele):
        self.modele = modele

    #annee
    def get_annee(self):
        return self.annee

    def set_annee(self, annee):
        self.annee = annee

    #prix
    def get_prix(self):
        return self.prix

    def set_prix(self, prix):
        self.prix = prix

    #autres methodes
    def informationsVehicule(self):
        return "Marque : " + self.marque + "\nModel : " + self.modele + "\nAnnee : " + str(self.annee) + "\nPrix : " + str(self.prix)


class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, porte = 4):
        Vehicule.__init__(self, marque, modele, annee, prix)
        self.porte = porte

    #porte
    def get_porte(self):
        return self.porte

    def set_porte(self, porte):
        self.porte = porte

    #autres methodes
    def informationsVehicule(self):

        return "\n" + super().informationsVehicule() + "\nPorte : " + str(self.porte)
       

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roue = 2):
        Vehicule.__init__(self, marque, modele, annee, prix)
        self.roue = roue

    #roue
    def get_roue(self):
        return self.roue

    def set_roue(self, roue):
        self.roue = roue

    #autres methodes
    def informationsVehicule(self):
        return "\n" + super().informationsVehicule() + "\nRoue : " + str(self.roue)





vehicule1 = Vehicule("Peugeot", "208", 2019, 15000)
print(vehicule1.informationsVehicule())
vehicule1 = Voiture("Mercedes", "ClasseA", 2020, 18500)
print(vehicule1.informationsVehicule())
vehicule1 = Moto("Yamaha", "1200 Vmax", 1987, 4500)
print(vehicule1.informationsVehicule())