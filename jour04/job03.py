class Rectangle:
    def __init__(self, longueur, largeur):
        self._longueur = longueur
        self._largeur = largeur

    #longueur
    def get_longueur(self):
        return self._longueur

    def set_longueur(self, longueur):
        self._longueur = longueur

    #largeur
    def get_largeur(self):
        return self._largeur

    def set_largeur(self, largeur):
        self._largeur = largeur


    #autres methodes
    def perimetre(self):
        return (self._longueur + self._largeur) * 2

    def surface(self):
        return self._longueur * self._largeur

class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        Rectangle.__init__(self, longueur, largeur)
        self._hauteur = hauteur

    #hauteur
    def get_hauteur(self):
        return self._hauteur

    def set_hauteur(self, hauteur):
        self._hauteur = hauteur

    #autres methodes

    def volume(self):
        return self._longueur * self._largeur * self._hauteur

rectangle1 = Rectangle(5, 10)
print(rectangle1.perimetre())
print(rectangle1.surface())

parallelepipede1 = Parallelepipede(5, 10, 15)
print(parallelepipede1.volume())

