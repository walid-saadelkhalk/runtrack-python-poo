class Forme: 
    def aire(self):
        return 0

class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        Forme.__init__(self)
        self.longueur = longueur
        self.largeur = largeur

    #longueur
    def get_longueur(self):
        return self.longueur

    def set_longueur(self, longueur):
        self.longueur = longueur

    #largeur
    def get_largeur(self):
        return self.largeur

    def set_largeur(self, largeur):
        self.largeur = largeur

    def aire(self):
        return self.longueur * self.largeur

rectangle1 = Rectangle(5, 10)
print(rectangle1.aire())
