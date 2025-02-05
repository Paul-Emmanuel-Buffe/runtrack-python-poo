class Voiture:
    def __init__(self, marque, modele, annee, kilometres):
        self._marque= marque
        self._modele = modele
        self._annee = annee
        self._kilometres = kilometres
        self._en_marche = False
        self._reservoir = 50
# Accesseurs
    def get_marque(self):
        return self._marque
    def get_modele(self):
        return self._modele
    def get_annee(self):
        return self._annee
    def get_kilometres(self):
        return self._kilometres
    
# Mutateurs
    def set_marque(self,nv_marque):
        self._marque = nv_marque
    def set_modele(self, nv_modele):
        self._modele = nv_modele
    def set_annee(self, nv_annee):
        self._annee = nv_annee
    def set_kilometres(self, nv_kilometres):
        self._kilometres = nv_kilometres
    def set_reservoir(self):       # Ajout de cette methode pour la fluidité du test plus bas
        nv_reservoir = float(input('Donner un nouvelle valeur à self._reservoir :'))
        self._reservoir = nv_reservoir

# Methodes
    def verifier_plein(self):
        return self._reservoir
    
    def demarrer (self):
        if self._reservoir > 5:
            if self._en_marche == False:
                self._en_marche = True
                print("La voiture démarre")
        else:
            print("Pas assez de carburant.")
    
    def arreter (self):
        if self._en_marche == True:
            self._en_marche = False


car = Voiture("Toyota", "Prius", "2024","5670") #
car.demarrer()

car.set_reservoir() # Utilisation de la méthode pour passer le réservoir en dessous de 5
car.demarrer()