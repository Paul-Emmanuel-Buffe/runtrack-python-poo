# déclaration de la classe
class Animal:
    def __init__(self, age): #Constructeur
        self.age = age

    def viellir (self):
        self.age +=1
        return self.age
    
    def nommer (self, name):
        self.name= name
        return self.name

chien = Animal(0)
print(f"L'age du chien est {chien.age} ans")#Affichage de l'age du chien

chien.viellir()
print(f"L'age du chien est {chien.age} ans") #test de fonction vieillir


nom_chien = chien.nommer('Brurus')
print(f'Le chien se nomme {nom_chien}')
