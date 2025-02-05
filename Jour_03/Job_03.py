
# Création de la classe Tache : Le sujet ne demande pas d'attribut privé
class Tache:
    def __init__(self, titre, description):
        self.titre = titre
        self.description = description
        self.statut = "à faire"
 

    def set_statut(self, statut):
        if self.statut in ["à faire", "terminé"]:
            self.statut = statut
        else:
            print('Statut de la tâche mal renseigné, il ne peut être que "à faire" ou "terminé"')