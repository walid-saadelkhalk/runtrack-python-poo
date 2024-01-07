class Tache:
    # Constructeur
    def __init__(self, titre, description, statut = "A faire"):
        self.__titre = titre
        self.__description = description
        self.__statut = statut

    #titre
    def get_titre(self):
        return self.__titre

    def set_titre(self, titre):
        self.__titre = titre

    #description
    def get_description(self):
        return self.__description

    def set_description(self, description):
        self.__description = description

    #statut
    def get_statut(self):
        return self.__statut

    def set_statut(self, statut):
        self.__statut = statut


class ListDeTaches:
    #Constructeur
    def __init__(self):
        self.__taches_liste = []

    #taches_liste
    def get_taches_liste(self):
        return self.__taches_liste

    def set_taches_liste(self):
        self.__taches_liste = taches_liste

    #autres methodes

    def ajouterTache(self, objet_tache):
        self.__taches_liste.append(objet_tache)
        print(f"\ntache ajoutee: {objet_tache.get_titre()}")

    def supprimerTache(self, supp_tache):
        self.__taches_liste.remove(supp_tache)
        print(f"\ntache supprimee: {supp_tache.get_titre()}")

    def marquerCommeFinie(self, fini_tache):
        fini_tache.set_statut("terminer")
        print(f"\ntache marquee comme finie: {fini_tache.get_titre()}")

    def afficherTaches(self):
        for fini_tache in self.__taches_liste:
            print(f"\ntache: {fini_tache.get_titre()}\ndescription: {fini_tache.get_description()}\nstatut: {fini_tache.get_statut()}\n")
            return [fini_tache.get_titre() for fini_tache in self.__taches_liste]

    def filtrerListe(self, statut):
        for fini_tache in self.__taches_liste:
            if fini_tache.get_statut() == statut:
                print(f"\ntache: {fini_tache.get_titre()}\ndescription: {fini_tache.get_description()}\nstatut: {fini_tache.get_statut()}\n")



maison = Tache("faire le menage", "nettoyer la cuisine")
travail = Tache("finir le rapport", "envoyer le rapport a mon chef")
courses = Tache("acheter du lait", "2 bouteilles de lait")

liste_taches = ListDeTaches()

print(f"titre: {maison.get_titre()}\ndescription: {maison.get_description()}\nstatut: {maison.get_statut()}")
print(f"titre: {travail.get_titre()}\ndescription: {travail.get_description()}\nstatut: {travail.get_statut()}")
print(f"titre: {courses.get_titre()}\ndescription: {courses.get_description()}\nstatut: {courses.get_statut()}")
liste_taches.ajouterTache(maison)
liste_taches.ajouterTache(travail)
liste_taches.ajouterTache(courses)
liste_taches.afficherTaches()


liste_taches.supprimerTache(travail)
liste_taches.marquerCommeFinie(maison)
liste_taches.afficherTaches()

liste_taches.ajouterTache(travail)


liste_taches.filtrerListe("A faire")


