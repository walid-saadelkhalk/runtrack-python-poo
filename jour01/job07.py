class Personnage:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def gauche(self):
        self.x -= 1
        print(f"le perso se dépalce à la case {self.x} en abscisse")
    def droite(self):
        self.x += 1
        print(f"le perso se dépalce à la case {self.x} en abscisse")

    def haut(self):
        self.y += 1
        print(f"le perso se dépalce à la case {self.y} en ordonnée")
    
    def bas(self):  
        self.y -= 1
        print(f"le perso se dépalce à la case {self.y} en ordonnée")

    def position(self):
        print(f"({self.x}, {self.y})")


perso = Personnage( 3, 5)
perso.gauche()
perso.droite()
perso.haut()
perso.bas()
perso.position()

situation = (perso.x, perso.y)
tuple(situation)
print(tuple(situation))

