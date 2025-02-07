class Rectangle:
    def __init__(self, longueur, largeur):
        self._longueur = longueur
        self._largeur = largeur


    def perimetre (self):
        peri = 2 * (self._longueur+self._largeur)
        return peri
    
    def surface (self):
        surf = self._longueur * self._largeur
        return surf
    
    def get_longueur(self):
        return self._longueur
    
    def get_largeur(self):
        return self._largeur
    
    def set_longueur(self, nv_longueur):
        self._longueur = nv_longueur
        return self._longueur
    
    def set_largeur (self, nv_largeur):
        self._largeur = nv_largeur
        return self._largeur
    
class Paralepipede(Rectangle):
    def __init__(self, longueur, largeur,hauteur):
        super().__init__(longueur, largeur)
        self._hauteur = hauteur

    def volume(self):
        vol_par = self._longueur * self._largeur * self._hauteur
        return vol_par



# tests sur l'instance de Rectangle
rect1 = Rectangle(5, 8)
print(rect1.surface())

print(rect1.get_largeur())
print(rect1.get_longueur())

rect1.set_largeur(70)
print(rect1.surface())

rect1.set_longueur(23)
print(rect1.surface())

#Test sur l'instance de Paralépipède

rect2 = Paralepipede(4,6,10)
print(rect2.get_largeur())
print(rect2.get_longueur())

print(rect2.volume())