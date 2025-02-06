
# Création de la classe Tache : Le sujet ne demande pas d'attribut privé
class Tache:
    def __init__(self,liste):
        self.titre = input("Veuillez indiquer la tache à plannifier : ")
        self.description = input("veuillez décrire la tache à plannifier : ")
        self.statut = "à faire"
        self.liste = liste # Ici se fait le lien avec l'instance de ListeTaches

    def creat_dicto (self): #Création de la tache sous forme de dictionnaire.
        titre = self.titre
        description = self.description
        statut = self.statut
        dicto ={"titre": titre , "description" : description, "statut" : statut}
        self.liste.ajouter_tache(dicto)
        print("Cette tâche à bien était ajoutée à votre liste des tâches")
     
class ListeTaches:
        def __init__ (self):
            self.taches = []
        
        def ajouter_tache(self,dicto):
            self.taches.append(dicto)

        def supprimer_tache(self):
            index = int(input("Indiquez l'index de la taches à supprimer :"))
            self.taches.pop(index)
        
        def change_statut(self):
            index = int(input("Indiquez l'index de la tache que vous souhaitez enregistée comme terminé:"))
            self.taches[index]["statut"] = "terminé"
        
        def get_liste (self):
            for element in self.taches:
                print(element)
        def filtrer_liste (self):
            new_liste = []
            for element in self.taches:
                if element["statut"] == "terminé":
                    new_liste.append(element)
                    return new_liste

        
             
# instanciation d'une liste des taches
ma_liste = ListeTaches()

ma_tache = Tache(ma_liste) # Instanciation de la tache
ma_tache.creat_dicto() # enregistrement de la tache

#Serie d'enregistement de taches pour constituer la liste
ma_tache = Tache(ma_liste) # Instanciation de la tache
ma_tache.creat_dicto()
ma_tache = Tache(ma_liste) # Instanciation de la tache
ma_tache.creat_dicto()
ma_tache = Tache(ma_liste) # Instanciation de la tache
ma_tache.creat_dicto()
ma_tache = Tache(ma_liste) # Instanciation de la tache
ma_tache.creat_dicto()
ma_tache = Tache(ma_liste) # Instanciation de la tache
ma_tache.creat_dicto()

print(ma_liste.get_liste())

ma_liste.supprimer_tache() #SUPPRESSION D'UNE TACHE PAR SON INDEX
print(ma_liste.get_liste())

ma_liste.change_statut() # Modification du statut d'une tache dans la liste
print(ma_liste.get_liste())

print(ma_liste.filtrer_liste()) # Affichage de la liste avec taches terminées