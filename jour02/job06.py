class Commande:

    # constructeur
    def __init__(self, numero, plat, statut="en cours"):
        self.__numero = numero
        self.__plat = plat
        self.__commande = {}
        self.__statut = statut



    # getters
    def get_numero(self):
        return self.__numero

    def get_plat(self):
        return self.__plat

    def get_statut(self):
        return self.__statut


    # setters
    def set_numero(self, new_numero):
        self.__numero = new_numero

    def set_plat(self, new_plat):
        self.__plat = new_plat

    def set_statut(self, new_statut):
        self.__statut = new_statut



    # autres methodes
    def ajouter_plat(self, plat, prix_plat):
        if plat not in self.__commande:
            self.__commande[plat] = {'prix': prix_plat, 'statut': 'En cours'}
            return f"plat ajoute : {plat} ({prix_plat} $)"
        else:
            self.__commande[plat]['prix'] = prix_plat
            return f"Le plat {plat} est deja dans la commande. Modifier le prix."

    def annuler_commande(self):
        self.__commande.clear()
        self.__statut = "annulee"
        return "La commande a ete annulee."

    def __calculer_total(self):
        total = sum(plat['prix'] for plat in self.__commande.values())
        return total

    def afficher_commande(self):
        result = [f"commande numero {self.__numero}"]
        for plat, details_commande in self.__commande.items():
            result.append(f"{plat} ({details_commande['prix']} $). Statut: {details_commande['statut']}")
        result.append(f"total a payer: {self.__calculer_total()} $")
        result.append(f"statut de la commande: {self.__statut}")
        return "\n".join(result)

    def calcul_tva(self, taux_tva):
        tva = self.__calculer_total() * (taux_tva / 100)
        return tva




commande1 = Commande(1, "tajine")
print(commande1.ajouter_plat("tajine", 50))
print(commande1.ajouter_plat("lasagne", 30))
print(commande1.afficher_commande())

tva_calculee = commande1.calcul_tva(20)
print(f"TVA a payer: {tva_calculee} $")

print(commande1.annuler_commande())
print(commande1.afficher_commande())
