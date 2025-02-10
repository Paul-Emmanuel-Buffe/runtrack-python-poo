class Part:
    def __init__(self, name, material):
        self.name = name
        self.material = material

    def change_material(self, new_material):
        self.material = new_material
    
    def __str__(self):
        return f'Nom : {self.name}\nMatériaux : {self.material}'
    
class Ship:
    def __init__(self, name):
        self.name = name
        self.__parts = {}  # dictionnaires des pièces
        self.history = []  # Historique

    def display_state(self):
        # affichage du dicto
        return {key: str(value) for key, value in self.__parts.items()}
    
    def add_parts(self, part):
        self.__parts[part.name] = part
        self.history.append(f"Ajout de la pièce : {part.name}")

    def replace_part(self, part, new_part_name, new_material):
        if part.name in self.__parts:
            del self.__parts[part.name]
            new_part_object = Part(new_part_name, new_material)
            self.add_parts(new_part_object)
            self.history.append(f"Remplacement de {part.name} par {new_part_name} en {new_material}")
    
    def change_part(self, part_name, new_material):
        if part_name in self.__parts:
            part = self.__parts[part_name]  # objet Part 
            old_material = part.material
            part.change_material(new_material)  # Changement du matériau
            self.history.append(f"Changement du matériau de {part_name} : {old_material} -> {new_material}")
        else:
            print("La référence n'est pas présente")

    def display_history(self):  # Affichage de l'historique
        for action in self.history:
            print(action)

class RacingShip(Ship):
    def __init__(self, name, max_speed):
        super().__init__(name)
        self.max_speed = max_speed
    
    def display_speed(self):  #  vitesse
        print(f"Vitesse maximale du navire {self.name} : {self.max_speed} km/h")

def menu(racing_ship):
    while True:
        print("\n1. Afficher l'état du bateau")
        print("2. Remplacer une pièce")
        print("3. Modifier le matériau d'une pièce")
        print("4. Afficher l'historique des modifications")
        print("5. Afficher la vitesse maximale")
        print("6. Quitter")
        
        choice = input("Choisissez une option (1-6): ")
        
        if choice == "1":
            print(racing_ship.display_state())
        elif choice == "2":
            part_name = input("Nom de la pièce à remplacer: ")
            new_name = input("Nom de la nouvelle pièce: ")
            new_material = input("Matériau de la nouvelle pièce: ")
            if part_name in racing_ship._Ship__parts:
                part_to_replace = racing_ship._Ship__parts[part_name]
                racing_ship.replace_part(part_to_replace, new_name, new_material)
            else:
                print("Pièce non trouvée.")
        elif choice == "3":
            part_name = input("Nom de la pièce à modifier: ")
            new_material = input("Nouveau matériau: ")
            racing_ship.change_part(part_name, new_material)
        elif choice == "4":
            racing_ship.display_history()
        elif choice == "5":
            racing_ship.display_speed()
        elif choice == "6":
            print("Au revoir!")
            break
        else:
            print("Option invalide. Essayez encore.")

# Création d'un bateau
racing_ship = RacingShip("Vitesse", 150)

# création des pièces
coque = Part("Coque", "Pin")
proue = Part("Proue", "Chêne")
mat = Part("Mât", "Olivier et bronze")
gouvernail = Part("Gouvernail", "Chêne et cuivre")
voile1 = Part("Voile 1", "Lin")
voile2 = Part("Voile 2", "Chanvre")

# ajout des pièces 
racing_ship.add_parts(coque)
racing_ship.add_parts(proue)
racing_ship.add_parts(mat)
racing_ship.add_parts(gouvernail)
racing_ship.add_parts(voile1)
racing_ship.add_parts(voile2)

# Lancer le menu interactif
menu(racing_ship)




                                
                               
                        

# Instance De Ship:
bateau = Ship("bateau_thesee")

coque = Part("Coque", "Pin")# instance de pièce du bateau
bateau.add_parts(coque)

proue = Part("Proue", "Chêne")# instance de pièce du bateau
bateau.add_parts(proue)

mat= Part("Mât", "Olivier et bronze")# instance de pièce du bateau
bateau.add_parts(mat)

gouvernail = Part("Gouvernail", "Chêne et cuivre")# instance de pièce du bateau
bateau.add_parts(gouvernail)

voile1 = Part("Voile 1", "Lin")
bateau.add_parts(voile1)

voile2 = Part("Voile 2", "Chanvre")
bateau.add_parts(voile2)

print(bateau.display_state()) # Affichage de la liste des pièces après construction du bateau

#Remplacement d'une pièce
bateau.replace_part(voile1, "voile1", "Lin")
print(bateau.display_state())


bateau.change_part("Proue", "Chêne")
print(bateau.display_state())









    

