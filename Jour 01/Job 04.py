# déclaration de la classe "Personne"
class Personne:
    # Constructeur
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
    def sePresenter(self): # Méthode se présenter qui retourne le prénom et le nom dans une chaine de caractère
        return self.prenom, self.nom
         
# Tests  
paul = Personne('Buffe', 'Paul')
marie = Personne('Dremier', 'Marie')
christophe = Personne('Colomb','Christophe')

prenom, nom = paul.SePresenter()
print(f'Je suis {prenom} {nom}')
prenom, nom = marie.SePresenter()
print(f'Je suis {prenom} {nom}')
prenom, nom = christophe.SePresenter()
print(f'Je suis {prenom} {nom}')