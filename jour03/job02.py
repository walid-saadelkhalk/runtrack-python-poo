class CompteBancaire:
    # Constructeur
    def __init__(self, num_compte, nom, prenom, solde, decouvert = True):
        self.__num_compte = num_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    #getter
    def get_num_compte(self):
        return self.__num_compte

    def get_nom(self):
        return self.__nom

    def get_prenom(self):
        return self.__prenom

    def get_solde(self):
        return self.__solde

    def get_decouvert(self):
        return self.__decouvert


    #setter
    def set_num_compte(self, num_compte):
        self.__num_compte = num_compte

    def set_nom(self, nom):
        self.__nom = nom

    def set_prenom(self, prenom):
        self.__prenom = prenom

    def set_solde(self, solde):
        self.__solde = solde

    def set_decouvert(self, decouvert):
        self.__decouvert = decouvert



    #autres methodes
    def afficher(self):
        return f"compte: {self.__num_compte}\nclient: {self.__prenom} {self.__nom}"

    def afficherSolde(self):
        return f"solde: {self.__solde} euros"

    def versement(self, montant):
        self.__solde += montant
        return f"versement: {montant} euros"


    def retrait(self, montant_retire, decouvert):
        if decouvert == False and montant_retire > self.__solde:
            return f"retrait: impossible. solde insuffisant"
        else:
            self.__solde -= montant_retire
            return f"retrait: {montant_retire} euros"

    def agios(self):
        if self.__solde < 0:
            self.__solde += self.__solde * 0.10
            return f"agios: 10% du solde"
        else:
            return f"agios: pas d'agios"
    
    def virement(self, reference, compte, montant):
        if self.get_decouvert() == False and montant > self.get_solde():
            return f"virement: impossible. solde insuffisant"

        elif self.get_decouvert() == True and montant > self.get_solde():
            self.set_solde(self.get_solde() - montant)
            compte.set_solde(compte.get_solde() + montant)
            self.agios()
            return f"virement: {montant} euros"

        elif self.get_decouvert() == True and montant < self.get_solde():
            self.set_solde(self.get_solde() - montant)
            compte.set_solde(compte.get_solde() + montant)
            return f"virement: {montant} euros effectue"
        


client1 = CompteBancaire(123456, "Dupont", "Jean", 10000)
client1.set_decouvert(True)   
print(client1.afficher())
print(client1.afficherSolde())
print(client1.versement(200))
print(client1.afficherSolde())
print(client1.retrait(500, client1.get_decouvert()))
print(client1.afficherSolde())
print(client1.retrait(2000, client1.get_decouvert()))
print(client1.afficherSolde())

client2 = CompteBancaire(789101, "Durand", "Marie", -2000)
client2.set_decouvert(True)
print(client2.afficher())
print(client2.afficherSolde())
print(client1.virement(123456, client2, 2001))
print(client2.afficherSolde())
