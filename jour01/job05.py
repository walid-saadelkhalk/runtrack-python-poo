class Point: 

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def afficherlesPoints(self):
        return self.x, self.y   

    def afficherX(self):
        return self.x

    def afficherY(self):
        return self.y

    def changerX(self):
        nouvelle_valeur_x = int(input("Entrez la nouvelle valeur de x: "))
        self.x = nouvelle_valeur_x

    def changerY(self):
        nouvelle_valeur_y = int(input("Entrez la nouvelle valeur de y: "))
        self.y = nouvelle_valeur_y

p1 = Point(2, 3)
print(f"p1: {p1.afficherlesPoints()}")
print(f"X: {p1.afficherX()}")
print(f"Y: {p1.afficherY()}")


p1.changerX()
p1.changerY()

print(f"nouveau p1 : {p1.afficherlesPoints()}")

