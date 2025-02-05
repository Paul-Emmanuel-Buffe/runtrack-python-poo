class Ville :
    def __init__(self,nom, nb_habitants):
        self._nom = nom
        self._nb_habitants = int(nb_habitants)
    
    def get_nb_habitants_ville(self): # permet de retourner le nombre d'habitants mis à jour
        return f"Mise à jour de la population de la ville de {self._nom} : {self._nb_habitants}"
    
    # méthode spéciale Python pour définir la représentation de l'objet sous forme de string
    def __str__(self):
        return f"Population de la ville de {self._nom} est de {self._nb_habitants} d'habitants."

class Personne :
    def __init__ (self, nom, age,ville):
        self._nom = nom
        self._age = age
        self._ville = ville

    def ajouterPopulation(self): # ajoute l'instance de Personne à l'instance de la classe ville 
        self._ville._nb_habitants += 1


# Instanciation des villes
paris = Ville("Paris", 1000000)
marseille = Ville ("Marseille", 861635)
print(paris)
print(marseille)

# Instanciation et utilisation de la méthode ajouterPersonne
J = Personne("John",45,paris)
J.ajouterPopulation()

M = Personne("Mytille", 4, marseille) # l'instance de Ville est renseignée en paramètre et non str
M.ajouterPopulation()

C = Personne("Chloé", 18, marseille) # l'instance de Ville est renseignée en paramètre et non str
C.ajouterPopulation()

print(paris.get_nb_habitants_ville())
print(marseille.get_nb_habitants_ville())









        

        
