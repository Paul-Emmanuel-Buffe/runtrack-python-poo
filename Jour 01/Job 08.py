# déclaration de la classe
class Cercle:
    def __init__(self, rayon):
        self.rayon = rayon

    def changerRayon (self): #changer rayon
        self.rayon = float(input("Donnez une valeur au rayon de votre cercle, en centimètres : "))
        return self.rayon
    def ciconference (self): # calcul circonférence
        C = 2*(3.1416 * self.rayon)
        return C
    def diametre (self) : # calcul diametre
        D = 2 * self.rayon
        return D

    def aire (self): # calcul aire
        return 3.1416 * (self.rayon * self.rayon)
    
    def afficherInfos (self): # affichage       
        aire = self.aire()
        print(f"L'aire de ce cercle est de {aire} cm.")
        diametre = self.diametre()
        print(f"Le diamètre de ce cercle est de {diametre} cm.")
        circonference = self.ciconference()
        print (f"La circonférence de ce cercle est de {circonference} cm.")

# Entrez la valeur 4
cercle1 = Cercle(0)
cercle1.changerRayon()
cercle1.afficherInfos()

# Entrez la valeur 7
cercle2 = Cercle(0)
cercle1.changerRayon()
cercle1.afficherInfos()
