from abc import ABC

class Forme (ABC):
    def aire (self):
        return 0
    
class Cercle(Forme):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    
    def aire(self):
        return  3.14159*(self.radius * self.radius)

class Rectangle(Forme):
    def __init__(self, longueur, largeur):
        super().__init__()
        self.longueur = longueur
        self.largeur = largeur
    
    def aire(self):
        return self.longueur * self.largeur
    
rect = Rectangle(40,5)
print(rect.aire())

cerc= Cercle(8)
print(cerc.aire())