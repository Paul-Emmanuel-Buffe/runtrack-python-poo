class Joueur:
    def __init__(self, nom, numéro, position):
        self.nom = nom
        self.numéro = numéro
        self.position = position
        self.nombre_buts_marqués = 0
        self.passes_décisives_effectuées = 0
        self.cartons_jaunes_reçus = 0
        self.cartons_rouges_reçus = 0

    def marquerUnBut(self):
        self.nombre_buts_marqués += 1

    def effectuerUnePasseDecisive(self):
        self.passes_décisives_effectuées += 1

    def recevoirUnCartonJaune(self):
        self.cartons_jaunes_reçus += 1

    def recevoirUnCartonRouge(self):
        self.cartons_rouges_reçus += 1

    def afficherStatistiques(self):
        print(f"Statistiques de {self.nom} (Numéro {self.numéro}, {self.position}):")
        print(f"  Buts marqués: {self.nombre_buts_marqués}")
        print(f"  Passes décisives: {self.passes_décisives_effectuées}")
        print(f"  Cartons jaunes: {self.cartons_jaunes_reçus}")
        print(f"  Cartons rouges: {self.cartons_rouges_reçus}")
        print()

class Equipe:
    def __init__(self, nom):
        self.nom = nom
        self.joueurs = []

    def ajouterJoueur(self, joueur):
        self.joueurs.append(joueur)

    def AfficherStatistiquesJoueurs(self):
        print(f"Statistiques des joueurs de l'équipe {self.nom}:")
        for joueur in self.joueurs:
            joueur.afficherStatistiques()

    def mettreAJourStatistiquesJoueur(self, nom_joueur, buts=0, passes=0, jaunes=0, rouges=0):
        for joueur in self.joueurs:
            if joueur.nom == nom_joueur:
                joueur.nombre_buts_marqués += buts
                joueur.passes_décisives_effectuées += passes
                joueur.cartons_jaunes_reçus += jaunes
                joueur.cartons_rouges_reçus += rouges
                break

# Création des joueurs
joueur1 = Joueur("Lionel Messi", 10, "Attaquant")
joueur2 = Joueur("Sergio Ramos", 4, "Défenseur")
joueur3 = Joueur("Zidane",2,"Milieu")
joueur4 = Joueur("Paul-Emmanuel Buffe", 1, "Gardien")

# Création des équipes
equipe1 = Equipe("Paris Saint-Germain")
equipe2 = Equipe("OM")

# Ajout des joueurs aux équipes
equipe1.ajouterJoueur(joueur1)
equipe1.ajouterJoueur(joueur2)
equipe2.ajouterJoueur(joueur3)
equipe2.ajouterJoueur(joueur4)

# Affichage des statistiques initiales
equipe1.AfficherStatistiquesJoueurs()
equipe2.AfficherStatistiquesJoueurs()

# Simulation d'un match
joueur1.marquerUnBut()
joueur3.effectuerUnePasseDecisive()
joueur2.recevoirUnCartonJaune()
joueur4.recevoirUnCartonRouge()

# Affichage des statistiques après le match
print("Après le match:")
equipe1.AfficherStatistiquesJoueurs()
equipe2.AfficherStatistiquesJoueurs()