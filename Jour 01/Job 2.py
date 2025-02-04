#Déclaration de classe
class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2

# instanciation de classe
op_object= Operation(14, 87)

#Impression
print(f"Le nombre1 est  {op_object.nombre1}.")
print(f"Le nombre1 est  {op_object.nombre2}.")