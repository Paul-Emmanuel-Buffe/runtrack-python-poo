import random

class CompteBancaire:
    def __init__(self, num_compte, nom, prenom,solde):
        self._num_compte = num_compte
        self._nom = nom
        self._prenom = prenom
        self._solde = solde
        self._decouvert = True

    def afficher_compte(self): # permet de visualiser les infos du compte
        return f"N° de compte : {self._num_compte}\nNom : {self._nom}\nPrénom : {self._prenom}"
    
    def afficherSolde(self): # permet d'afficher le solde
        return f"Solde: {self._solde}"
    
    def versement(self): # méthode pour le versement
        mt_versement = float(input("Montant du versement : "))
        self._solde = self._solde + mt_versement
        print(f'Versement de {mt_versement} € effectué sur le compte N° {self._num_compte}')
    
    def retrait(self): # méthode pour le retrait
        mt_retrait = float(input("Montant du retrait : "))
        if self._decouvert == True :
            self._solde = self._solde - mt_retrait  
            print(f"Votre virement d'un montant de {mt_retrait} € a bien été pris en compte.")       
        else: 
            if mt_retrait < self._solde : # condition pour que le retrait s'effectue
                self._solde = self._solde - mt_retrait
                print(f"Votre virement d'un montant de {mt_retrait} € a bien été pris en compte.")
            else:
                print(f"Le solde de votre compte n'est pas suffisant pour effectuer cette opération.")

    def agios(self):
        if self._solde < 0 :
            self._solde -= 50
            print(f'Le montant de vos agios sont de 50 €')

 
# Virement compte extèrieur    
    def virement(self, compte_destinataire):
        mt_virement = float(input('Montant souhaité du virement : '))
        ref_virement = random.randint(1, 10000)
        
        if self._decouvert and mt_virement > self._solde:
            self._solde -= mt_virement  
            compte_destinataire._solde += mt_virement
            print(f"Votre virement d'un montant de {mt_virement} € a bien été pris en compte, sous la ref N°{ref_virement}.\nNous vous indiquons que le solde de votre compte est négatif.")       
        else: 
            if mt_virement < self._solde : # condition pour que le retrait s'effectue
                self._solde = self._solde - mt_virement
                print(f"Votre virement d'un montant de {mt_virement} € a bien été pris en compte, sous la ref N°{ref_virement}.")
            else:
                print(f"Le solde de votre compte n'est pas suffisant pour effectuer cette opération.")



# Création du, premier compte
paul = CompteBancaire(809998,"Buffe", "Paul-Emmanuel", 1000)
print(paul.afficher_compte())

# salve de vérification avant implémenattion de la méthode Agios
paul.versement()
print(paul.afficherSolde())
paul.retrait()
print(paul.afficherSolde())
paul.agios()

# test de virement compte extèrieur
pierre = CompteBancaire(90,"Cornac", "Pierre", -450)
paul.virement(pierre)
print(pierre.afficherSolde())


