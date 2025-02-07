from abc import ABC # permet la création de classe abstraites

class Forme (ABC): # Classe Générique
    def aire (self):
        return 0
          
class Cercle(Forme): # Classe Cercle qui hérite de Forme et surcharge aire()
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    
    def aire(self):
        return  3.14159*(self.radius * self.radius)

class Rectangle(Forme): # Classe Rectangle qui hérite de Forme et surcharge aire()
    def __init__(self, longueur, largeur):
        super().__init__()
        self.longueur = longueur
        self.largeur = largeur
    
    def aire(self):
        return self.longueur * self.largeur


# Partie  déroulement des vérifs
rect = Rectangle(40,5)
print(rect.aire())

cerc= Cercle(8)
print(cerc.aire())