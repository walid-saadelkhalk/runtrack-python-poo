class Personne:

    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return self.prenom + " " + self.nom

john = Personne("Doe", "John")
jean = Personne("Dupont", "Jean")

print(f"je suis {john.SePresenter()}")
print(f"je suis {jean.SePresenter()}")


