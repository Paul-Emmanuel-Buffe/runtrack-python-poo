class Personne:
    def __init__(self, age):
        self.age = 14

    def afficherAge (self):
         print(self.age)

    def bonjour (self):
        print("Hello")

    def modifier_age (self):
        self.age = int(input("Quel age ? : "))

class Eleve (Personne):
    def __init__(self, age):
        super().__init__(age)
   
    def aller_cours (self):
        print("Je vais en cours")

    def afficher_age (self):
        print(f"J'ai {self.age} ans.")

class Professeur (Personne):

    def __init__ (self, matière_enseignée):
        self._matière_enseignée = matière_enseignée

    def enseigner (self):
        print("Le cours va commencer")


# Début des essais
paul = Eleve(Personne)
paul.bonjour()
paul.aller_cours()
paul.modifier_age()
paul.afficher_age()

pierre = Professeur(Personne)
pierre.bonjour()
pierre.modifier_age()
pierre.enseigner()