class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self._titre = titre
        self._auteur = auteur
        self._nb_pages = nb_pages

# méthodes avec tous les accesseurs pour afficher les attributs
    def get_titre(self):
        print(self._titre)
    def get_auteur(self):
        print(self._auteur)
    def get_nb_pages(self):
        print(self._nb_pages)
    
# méthodes avec les mutateurs
    def set_titre(self, nouveau_titre):
        self._titre = nouveau_titre
        return self._titre
    def set_auteur(self, nouvel_auteur):
        self._auteur = nouvel_auteur
        return self._auteur
    
    def set_nb_pages(self, nv_nb_pages): # mutateur avec une condition et un message d'erreur
        if isinstance(nv_nb_pages,int):
                self._nb_pages = nv_nb_pages
        else:
            print("MESSAGE ERREUR !!!!")


l = Livre("DRAGON", "YULLIA DREVET", 56) # Vérification de l'exercice
l.set_nb_pages(67.9)

