class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self._titre = titre
        self._auteur = auteur
        self._nb_pages = nb_pages
        self._disponible = True
    
    @property                  # Utilisation despropriétés python pour l'encapsulation (similaire à get)
    def verification(self):
        return self._disponible
    
    @verification.setter      # Utilisation despropriétés python pour l'encapsulation (similaire à set
    def verification(self):
         return self._disponible
    def emprunter(self):
        if self.verification:
            self._disponible = False
            print("Livre emprunté")
        else:
            print("Le livre doit être diponible pour pouvoir l'emprunter")

l = Livre("GRT3", "UUYUY", 56) # Partie vérification
l.emprunter()

l.emprunter()

