
class Rectangle:
    def __init__(self, longueur, largeur):
        self._longueur = longueur # attribut privé
        self._largeur = largeur # attribut privé

    def get_longueur(self): # accesseur 
        return self._longueur
    
    def get_largeur(self): # accesseur
        return self._largeur
    
    def set_longueur(self, nouvelle_longueur): # mutateur
        self._longueur = nouvelle_longueur

    def set_largeur(self, nouvelle_largeur): # mutateur
        self._largeur = nouvelle_largeur

# Instance de Rectangle
rectangle = Rectangle(10,5)
longueur = rectangle.get_longueur() # utilisation de l'accesseur 
print(longueur)
largeur = rectangle.get_largeur()# Utilisation de l'accesseur 
print(largeur)

# changement de la longueur et de la largeur avec l'utiolisation de u mutateur
rectangle.set_longueur(1000)
rectangle.set_largeur(4000)
longueur = rectangle.get_longueur()
print(longueur)
largeur = rectangle.get_largeur()
print(largeur)