class Student:
    def __init__(self, nom, prenom, num_etudiant):
          self._nom = nom
          self._prenom = prenom
          self._num_etudiant = num_etudiant
          self._credit = 0

# Setter pour le crédit    
    def add_credit(self):
        ajout_euros=float(input("De combien voulez-vous créditer cet étudiant ? : "))
        if ajout_euros > 0: 
            self._credit += ajout_euros
            return self._credit

# Getter pour les infos
    def get_nom(self):
         return self._nom
    def get_prenom(self):
        return self._prenom
    def get_num_etudiant(self):
         return self._num_etudiant

# Création de l'attibut privé level    
    def student_eval(self):
        if self._credit>=90:
              self._level = 'Excellent'
        elif self._credit <90 and self._credit >=80:
              self._level = 'Très Bien'
        elif self._credit <80 and self._credit >=70:
              self._level = 'Bien'
        elif self._credit <70 and self._credit >=60:
              self._level = 'Passable'
        else:
              self._level = 'Insuffisant'
        return self._level
    
# Fiche student pour affichage    
    def infos_student(self):
        prenom = self._prenom
        nom = self._nom
        id = self._num_etudiant
        niveau = self.student_eval()
        return prenom, nom, id, niveau

         
# test de add_credit       
etudiant1 = Student("Doe", "John", "145")
etudiant1.add_credit()
etudiant1.add_credit()
print(f'Le nombre de crédit de {etudiant1.get_prenom()} {etudiant1.get_nom()} est de {etudiant1.add_credit()}')

# test infos_student
prenom, nom, id, niveau = etudiant1.infos_student()

print(f'Prenom : {prenom}')
print(f'Nom : {nom}')
print(f'Id : {id}')
print(f'Niveau: {niveau}')





