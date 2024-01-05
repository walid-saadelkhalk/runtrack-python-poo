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

class Cercle(Forme):
    def __init__(self, radius):
        Forme.__init__(self)
        self.radius = radius

    #radius
    def get_radius(self):
        return self.radius

    def set_radius(self, radius):
        self.radius = radius

    def aire(self):
        return self.radius * self.radius * 3.14

rectangle1 = Rectangle(5, 10)
print(rectangle1.aire())

cercle1 = Cercle(5)
print(cercle1.aire())


