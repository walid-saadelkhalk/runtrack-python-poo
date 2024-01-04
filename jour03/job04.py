class Joueur:
    def __init__(self, nom, numero, position, nb_but = 0, nb_passes_de = 0, nb_carton_jaune = 0, nb_carton_rouge = 0):
        #constructeur
        self.__nom = nom
        self.__numero = numero
        self.__position = position
        self.__nb_but = nb_but
        self.__nb_passes_de = nb_passes_de
        self.__nb_carton_jaune = nb_carton_jaune
        self.__nb_carton_rouge = nb_carton_rouge


        #nom joueur
    def get_nom(self):
        return self.__nom

    def set_nom(self, nom):
        self.__nom = nom

        #numero joueur
    def get_numero(self):
        return self.__numero

    def set_numero(self, numero):
        self.__numero = numero

        #position joueur
    def get_position(self):
        return self.__position

    def set_position(self, position):
        self.__position = position

        #nb_but joueur
    def get_nb_but(self):
        return self.__nb_but

    def set_nb_but(self, nb_but):
        self.__nb_but = nb_but

        #nb_passes_de joueur
    def get_nb_passes_de(self):
        return self.__nb_passes_de

    def set_nb_passes_de(self, nb_passes_de):
        self.__nb_passes_de = nb_passes_de

        #nb_carton_jaune joueur 
    def get_nb_carton_jaune(self):
        return self.__nb_carton_jaune

    def set_nb_carton_jaune(self, nb_carton_jaune):
        self.__nb_carton_jaune = nb_carton_jaune

        #nb_carton_rouge joueur

    def get_nb_carton_rouge(self):
        return self.__nb_carton_rouge

    def set_nb_carton_rouge(self, nb_carton_rouge):
        self.__nb_carton_rouge = nb_carton_rouge



    #autres methodes
    def marquerUnBut(self):
        self.__nb_but += 1
        return f"but marque par {self.__nom}"

    def effectuerUnePasseDecisive(self):
        self.__nb_passes_de += 1
        return f"passe decisive de {self.__nom}"

    def recevoirUnCartonJaune(self):
        self.__nb_carton_jaune += 1
        return f"carton jaune pour {self.__nom}"

    def recevoirUnCartonRouge(self):
        self.__nb_carton_rouge += 1
        return f"carton rouge pour {self.__nom}"

    def afficherStatistiques(self):
        return f"statistiques de {self.__nom}:\nbut(s): {self.__nb_but}\npasse(s) decisive(s): {self.__nb_passes_de}\ncarton(s) jaune(s): {self.__nb_carton_jaune}\ncarton(s) rouge(s): {self.__nb_carton_rouge}"


class Equipe:
    #constructeur
    def __init__(self, nom_equipe):
        self.__nom_equipe = nom_equipe
        self.__liste_joueurs = []

    #nom_equipe
    def get_nom_equipe(self):
        return self.__nom_equipe

    def set_nom_equipe(self, nom_equipe):
        self.__nom_equipe = nom_equipe

    #liste_joueurs
    def get_liste_joueurs(self):
        return [joueur.get_nom() for joueur in self.__liste_joueurs]

    def set_liste_joueurs(self, liste_joueurs):
        self.__liste_joueurs = liste_joueurs


    #autres methodes

    def ajouterJoueur(self, add_joueur):
        self.__liste_joueurs.append(add_joueur)
        print(f"\njoueur ajoute: {add_joueur.get_nom()}")

    def afficherStatistiquesJoueurs(self):
        for add_joueur in self.__liste_joueurs:
            print(f"\njoueur: {add_joueur.get_nom()}\nbut(s): {add_joueur.get_nb_but()}\npasse(s) decisive(s): {add_joueur.get_nb_passes_de()}\ncarton(s) jaune(s): {add_joueur.get_nb_carton_jaune()}\ncarton(s) rouge(s): {add_joueur.get_nb_carton_rouge()}\n")

    def mettreAJourStatistiquesJoueur(self, add_joueur, statut):
        if statut == "but":
            add_joueur.marquerUnBut()
        elif statut == "passe decisive":
            add_joueur.effectuerUnePasseDecisive()
        elif statut == "carton jaune":
            add_joueur.recevoirUnCartonJaune()
        elif statut == "carton rouge":
            add_joueur.recevoirUnCartonRouge()
        else:
            return f"erreur"

#om
equipe1 = Equipe("OM")

joueur1 = Joueur("Payet", 15, "attaquant", 1500, 10, 0, 1)
joueur2 = Joueur("Robben", 7, "attaquant", 2500, 3500, 1, 0)
joueur3 = Joueur("Ronaldo", 10, "gardien", 3000, 2999, 0, 0)

joueur1.afficherStatistiques()
joueur2.afficherStatistiques()
joueur3.afficherStatistiques()

joueur1.recevoirUnCartonJaune()
joueur2.effectuerUnePasseDecisive()
joueur3.marquerUnBut()
print(joueur1.afficherStatistiques())
print(joueur2.afficherStatistiques())
print(joueur3.afficherStatistiques())

equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur2)
equipe1.ajouterJoueur(joueur3)
print(equipe1.get_liste_joueurs())
equipe1.afficherStatistiquesJoueurs()

equipe1.mettreAJourStatistiquesJoueur(joueur1, "carton jaune")
equipe1.mettreAJourStatistiquesJoueur(joueur2, "passe decisive")
equipe1.mettreAJourStatistiquesJoueur(joueur3, "but")
print(joueur1.afficherStatistiques())
print(joueur2.afficherStatistiques())
print(joueur3.afficherStatistiques())


#psg
equipe2 = Equipe("PSG")

joueur4 = Joueur("Neymar", 10, "attaquant", 15, 10, 2, 35)
joueur5 = Joueur("Messi", 30, "attaquant", 0, 0, 235, 1028)
joueur6 = Joueur("Marquinos", 7, "attaquant", 10, 5, 1, 2)


joueur4.afficherStatistiques()
joueur5.afficherStatistiques()
joueur6.afficherStatistiques()

joueur4.marquerUnBut()
joueur5.recevoirUnCartonRouge()
joueur6.effectuerUnePasseDecisive()
print(joueur4.afficherStatistiques())
print(joueur5.afficherStatistiques())
print(joueur6.afficherStatistiques())

equipe2.ajouterJoueur(joueur4)
equipe2.ajouterJoueur(joueur5)
equipe2.ajouterJoueur(joueur6)
print(equipe2.get_liste_joueurs())
equipe2.afficherStatistiquesJoueurs()

equipe2.mettreAJourStatistiquesJoueur(joueur4, "but")
equipe2.mettreAJourStatistiquesJoueur(joueur5, "carton rouge")
equipe2.mettreAJourStatistiquesJoueur(joueur6, "passe decisive")
print(joueur4.afficherStatistiques())
print(joueur5.afficherStatistiques())
print(joueur6.afficherStatistiques())

