#Déclaration de classe
class Operation:
    def __init__(self, nombre1, nombre2):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
    def addition(self):
        add_result = self.nombre1 + self.nombre2
        return add_result

# instanciation de classe
op_object= Operation(14, 87)

#Impression
print(op_object.addition())
