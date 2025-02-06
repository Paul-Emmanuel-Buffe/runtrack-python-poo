class Commande:
    def __init__(self, numero_commande):
        # Attributs privés
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}  # Dictionnaire pour stocker les plats avec leur prix et statut
        self.__statut = "en cours"  # statut initial de la commande

    # Get pour obtenir le num de commande
    def get_numero_commande(self):
        return self.__numero_commande

    # Getter pour obtenir le statut
    def get_statut(self):
        return self.__statut

    #  ajouter un plat à la commande
    def ajouter_plat(self, nom_plat, prix_plat):
        if self.__statut == "en cours":
            self.__plats_commandes[nom_plat] = {"prix": prix_plat, "statut": "en cours"}
            print(f"Plat ajouté : {nom_plat} - {prix_plat}€")
        else:
            print("Impossible d'ajouter un plat, la commande est déjà terminée ou annulée.")

    # annuler une commande
    def annuler_commande(self):
        if self.__statut == "en cours":
            self.__statut = "annulée"
            print("La commande a été annulée.")
        else:
            print("Impossible d'annuler la commande. Elle est déjà terminée ou annulée.")

    # calculer le total de la commande HT
    def calculer_total(self):
        total = sum(plat["prix"] for plat in self.__plats_commandes.values())
        return total

    # calculer la TVA 
    def calculer_tva(self):
        total = self.calculer_total()
        tva = total * 0.20  # 20% de TVA
        return tva

    #  la commande avec la somme à payer
    def afficher_commande(self):
        print(f"Commande n° {self.__numero_commande}")
        print(f"Statut de la commande : {self.__statut}")
        if self.__plats_commandes:
            print("Plats commandés :")
            for plat, details in self.__plats_commandes.items():
                print(f"{plat}: {details['prix']}€ (Statut: {details['statut']})")
            total = self.calculer_total()
            tva = self.calculer_tva()
            print(f"Total sans TVA : {total}€")
            print(f"TVA (20%) : {tva}€")
            print(f"Total à payer (avec TVA) : {total + tva}€")
        else:
            print("Aucun plat n'a été commandé.")
            
# Test

# Création d'une commande
commande1 = Commande(12345)

# + plats à la commande
commande1.ajouter_plat("Tarte",  5)
commande1.ajouter_plat("Couscous", 12)

# afichage  commande 
commande1.afficher_commande()

# Annulation commande
commande1.annuler_commande()


