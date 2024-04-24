#Alejandra Rodriguez Guevara 21310127 6E1

#Las reglas, las redes semánticas y la lógica descriptiva son diferentes formalismos utilizados en inteligencia artificial y representación del conocimiento. 

print("//////////////////////////////////////////")
print("-> Reglas")

class Regla:
    def __init__(self, antecedente, consecuente):
        #Inicialización de la clase Regla con un antecedente y un consecuente.
        self.antecedente = antecedente
        self.consecuente = consecuente

    def evaluar(self, conocimiento):
        #Método para evaluar si se cumple la regla con respecto al conocimiento dado.
        if self.antecedente in conocimiento:
            print(f"Se cumple la regla: {self.antecedente} -> {self.consecuente}")
            conocimiento.add(self.consecuente)
            return True
        else:
            return False

#Usamos la regla.
conocimiento = {"llueve"}
regla = Regla("llueve", "suelo_mojado")
regla.evaluar(conocimiento)
print("Conocimiento actualizado:", conocimiento)
print("//////////////////////////////////////////")
print("-> Redes Semánticas")

class Nodo:
    def __init__(self, nombre):
        #Inicialización de la clase Nodo con un nombre y una lista de vecinos.
        self.nombre = nombre
        self.vecinos = []

    def agregar_vecino(self, vecino):
        #Método para agregar un nodo vecino.
        self.vecinos.append(vecino)

    def __str__(self):
        #Método para representar el nodo como una cadena de caracteres.
        return f"Nodo: {self.nombre}, Vecinos: {[vecino.nombre for vecino in self.vecinos]}"

#Creamos de una red semántica simple.
nodo1 = Nodo("A")
nodo2 = Nodo("B")
nodo3 = Nodo("C")
nodo1.agregar_vecino(nodo2)
nodo1.agregar_vecino(nodo3)
print(nodo1)
print("//////////////////////////////////////////")
print("-> Lógica Descriptiva")

#Lógica Descriptiva.
class LógicaDescriptiva:
    def __init__(self, concepto, propiedades):
        #Inicialización de la clase LógicaDescriptiva con un concepto y un conjunto de propiedades.
        self.concepto = concepto
        self.propiedades = propiedades

    def verificar(self, objeto):
        #Método para verificar si un objeto cumple con las propiedades del concepto.
        for propiedad, valor in self.propiedades.items():
            if propiedad not in objeto or objeto[propiedad] != valor:
                return False
        return True

#Ejemplo de uso de la lógica descriptiva.
objeto = {"color": "rojo", "tamaño": "grande"}
regla = LógicaDescriptiva("manzana", {"color": "rojo", "tamaño": "grande"})
print("El objeto es una manzana?" if regla.verificar(objeto) else "El objeto no es una manzana")
print("//////////////////////////////////////////")