from abc import ABC # permet la création de classe abstraites

class Vehicule(ABC):
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def InformationsVehicule(self):
        print(f"Marque :  {self.marque}\nModèle: {self.modele}\nAnnée: {self.annee}\nPrix: {self.prix}")

class Voiture (Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.portes = 4 # ajout d'un attribut par rapport à la classe mère
    
    def InformationsVehicule(self): 
        print(f"Marque :  {self.marque}\nModèle: {self.modele}\nAnnée: {self.annee}\nPrix: {self.prix}\nPortes: {self.portes}")

class Moto (Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.roues = 2 # ajout d'un attribut par rapport à la classe mère
    
    def InformationsVehicule(self): 
        print(f"Marque :  {self.marque}\nModèle: {self.modele}\nAnnée: {self.annee}\nPrix: {self.prix}\nRoues: {self.roues}")

# Vérif Class Véhicule
car = Vehicule("MG", "Rt", "1990","50000 €")
car.InformationsVehicule()
# Vérif classe Voiture
car2 = Voiture("Renault", "Mégane", "2020", "20000 €")
car2.InformationsVehicule()

# Vérifs classe moto
moto = Moto("Yamaha", "Vmax", "2002", "5000 €")
moto.InformationsVehicule()