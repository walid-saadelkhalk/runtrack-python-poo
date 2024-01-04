class Ville:
    # Constructeur
    def __init__(self, nom_ville, nombre_habitants):
        self.__nom_ville = nom_ville
        self.__nombre_habitants = nombre_habitants

    #getter
    def get_nom_ville(self):
        return self.__nom_ville

    def get_nombre_habitants(self):
        return self.__nombre_habitants

    #setter
    def set_nom_ville(self, nom_ville):
        self.__nom_ville = nom_ville

    def set_nombre_habitants(self, nombre_habitants):
        self.__nombre_habitants = nombre_habitants




class Personne:
    # Constructeur
    def __init__(self, nom, age, objet_ville):
        self.__nom = nom
        self.__age = age
        self.__ville = objet_ville

    #getter
    def get_nom(self):
        return self.__nom

    def get_age(self):
        return self.__age

    def get_ville(self):
        return self.__ville

    #setter

    def set_nom(self, nom):
        self.__nom = nom

    def set_age(self, age):
        self.__age = age

    def set_ville(self, objet_ville):
        self.__ville = objet_ville


    def ajouterPopulation(self, objet_ville):
        objet_ville.set_nombre_habitants(objet_ville.get_nombre_habitants() + 1)
        print(f"Mise a jour de la population de la ville de {objet_ville.get_nom_ville()} : {objet_ville.get_nombre_habitants()} habitants")

paris = Ville("Paris", 1000000)
print(f"population de la ville de {paris.get_nom_ville()} : {paris.get_nombre_habitants()} habitants")

marseille = Ville("Marseille", 861635)
print(f"population de la ville de {marseille.get_nom_ville()} : {marseille.get_nombre_habitants()} habitants")

personne1 = Personne("John", 45, paris)
personne2 = Personne("Myrtille", 4, paris)
personne3 = Personne("Chloe", 18, marseille)

personne1.ajouterPopulation(paris)
personne2.ajouterPopulation(paris)
personne3.ajouterPopulation(marseille)


