class Produit:
    def __init__(self, name,price_ht):
        self.name = name
        self.price_ht = price_ht
        self.tva = 0.2
    def calculPrixTtc(self): #calcule le prix TTC à partir du HT
        self.price_ttc = self.price_ht +(self.price_ht * self.tva)
        return self.price_ttc
    def afficher(self): # liste et retourne chaque infos produit
        name_product = self.name
        product_ht = self.price_ht
        tva = self.tva
        product_ttc = self.calculPrixTtc()
        return name_product,product_ht,tva,product_ttc
    def change_name(self): # Change le nom produit
        self.name = input("Veuillez entrer un nom de produit : ")
    def change_price(self): # change le prix produit
        self.price_ht = float(input("Indiquez le prix hors taxes du produit : "))
    

p = Produit("Fromage", 6)
print(p.calculPrixTtc()) # affichage du prix TTC du produit p

brioche = Produit("Brioche", 4.9) # affichage du prix TTC du produit brioche
print(brioche.calculPrixTtc())

# Dernière partie du job = > changer le nom et le prix de produits et leurs prix TTC
p = Produit("Fromage", 6)

p.change_name() # Changement du nom et du prix
p.change_price()

nom, produit_ht, taux_tva, produit_ttc =p.afficher() # assignation des valeurs aux variables utilisables
print(f"Le prix du {nom} est de {produit_ttc} € TTC.") # affichage


