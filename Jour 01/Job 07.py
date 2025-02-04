#déclaration de la classe
class Personnage:
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def move_right(self): # déplacement vers la droite dans une matrice de 5 X 5
        if self.x >=0 and self.x<5:
            self.x +=1
        else:
            print('On a un problème')

    
    def move_left(self): # déplacement vers la gauche dans une matrice de 5 X 5
        if self.x >0 and self.x<=5:
            self.x -=1
        else:
            print('On a un problème')

    
    def move_up(self): # déplacement vers le Haut dans une matrice de 5 X 5
        if  self.y>=0 and self.y<5:
            self.y +=1
        else:
            print('On a un problème')
    
    def move_down(self): # déplacement vers le bas dans une matrice de 5 X 5
        if self.y > 0 and self.y<=5:
            self.y -=1
        else:
            print('On a un problème')

    def position(self):
        return self.x, self.y # retourne la position d'un personnage
    
pnj = Personnage(0,0) #instance de la classe Personnage

# série de déplacements
pnj.move_right()
pnj.move_right()
pnj.move_up()
pnj.move_right()
pnj.move_down()

print(pnj.position()) # impression de la position en fin des déplacements






