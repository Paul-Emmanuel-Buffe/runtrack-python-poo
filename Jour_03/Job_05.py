class Personnage:
    def __init__(self, nom, vie): #Initialise un personnage avec un nom et des points de vie.


        self.nom = nom
        self.vie = vie

    def attaquer(self, adversaire):
# Le personnage attaque l'adversaire, lui infligeant des dégâts.

        degats = 10  # Dégâts fixes pour simplifier
        adversaire.vie -= degats
        print(f"{self.nom} attaque {adversaire.nom} et lui inflige {degats} points de dégâts !")
        print(f"{adversaire.nom} a maintenant {adversaire.vie} points de vie.\n")

    def est_vivant(self): # Verification vie ou mort

        return self.vie > 0


class Jeu:
    def __init__(self):

        self.niveau = None

    def choisirNiveau(self): # Choix difficulté
       
        print("Choisissez un niveau de difficulté :")
        print("1. Facile")
        print("2. Normal")
        print("3. Difficile")
        choix = input("Entrez le numéro du niveau (1, 2 ou 3) : ")

        # Validation de l'entrée
        while choix not in ["1", "2", "3"]:
            print("Choix invalide. Veuillez entrer 1, 2 ou 3.")
            choix = input("Entrez le numéro du niveau (1, 2 ou 3) : ")

        self.niveau = int(choix)

    def lancerJeu(self):
        """
        Lance le jeu en fonction du niveau de difficulté choisi.
        """
        if self.niveau is None:
            print("Veuillez d'abord choisir un niveau de difficulté.")
            return

        #  points de vie en fonction du niveau
        if self.niveau == 1:
            vie_joueur = 100
            vie_ennemi = 50
        elif self.niveau == 2:
            vie_joueur = 80
            vie_ennemi = 80
        elif self.niveau == 3:
            vie_joueur = 50
            vie_ennemi = 100

        # Création persos
        joueur = Personnage("Joueur", vie_joueur)
        ennemi = Personnage("Ennemi", vie_ennemi)

        print("\nStart !")
        print(f"{joueur.nom} a {joueur.vie} points de vie.")
        print(f"{ennemi.nom} a {ennemi.vie} points de vie.\n")

        # combat
        while joueur.est_vivant() and ennemi.est_vivant():

            input("Appuyez sur Entrée pour attaquer...")
            joueur.attaquer(ennemi)


            if not ennemi.est_vivant():
                print(f"{ennemi.nom} est mort!")

            # ennemi
            print(f"C'est au tour de {ennemi.nom} d'attaquer...")
            ennemi.attaquer(joueur)


            if not joueur.est_vivant():
                print(f"{joueur.nom} a été vaincu !")
                break

        # résultat du combat
        if joueur.est_vivant():
            print(f"Félicitations, {joueur.nom} a gagné !")
        else:
            print(f"{ennemi.nom} a gagné.")



if __name__ == "__main__":
    jeu = Jeu()
    jeu.choisirNiveau()  
    jeu.lancerJeu()  