# déclaration de la classe
class Point:
    def __init__(self, x, y): #Constructeur
        self.x = x
        self.y = y

    def afficherLesPoints(self): # Méthode pour l'affichage du tuple de coordonnées
        print((self.x, self.y))

    def afficherx (self): # Comme son nom l'indique
        print(f'x = {self.x}')

    def affichery (self): # Comme son nom l'indique
        print(f'y = {self.y}')

    def changerx(self): # Changer la valeur de  x
        self.x = float(input("Donne une valeur à x : ")) 

    
point = Point(4 , 8)
point.afficherLesPoints() # Test de la méthode afficherLesPoints

point2 = Point(67,69)
point2.afficherx() # Test de la méthode afficherx

point3 = Point(6,9)
point3.affichery() # Test de la méthode affichery

point4 = Point(56, 900) # Test de la méthode changerx
point4.changerx()
point4.afficherLesPoints()

point5 = Point(867, 900) # Test de la méthode changery
point5.changerx()
point5.afficherLesPoints()




