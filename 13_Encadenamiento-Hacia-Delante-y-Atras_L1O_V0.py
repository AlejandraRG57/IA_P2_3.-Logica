#Alejandra Rodriguez Guevara 21310127 6E1

#El encadenamiento hacia adelante y hacia atrás son dos estrategias utilizadas en sistemas de inferencia para alcanzar metas 
#o conclusiones a partir de un conjunto de reglas y hechos iniciales.

print("//////////////////////////////////////////")
print("-> Encadenamiento hacia adelante (Forward Chaining)")

#Clase para la base de conocimientos.
class BaseConocimientos:
    def __init__(self):
        self.hechos = set() #Conjunto para almacenar hechos.

    def agregar_hecho(self, hecho):
        self.hechos.add(hecho) #Método para agregar hechos a la base de conocimientos.

    def aplicar_regla(self, regla, consecuente):
        if all(antecedente in self.hechos for antecedente in regla):
            self.agregar_hecho(consecuente)
            print(f"Se agregó el hecho: {consecuente}")

if __name__ == "__main__":
    base = BaseConocimientos()

    #Hechos iniciales.
    base.agregar_hecho("conejo (Bugs Bunny)")

    #Aplicamos las reglas.
    base.aplicar_regla(["conejo (Bugs Bunny)"], "mamifero (Bugs Bunny)")
    base.aplicar_regla(["mamifero (Bugs Bunny)"], "animal (Bugs Bunny)")

    #Consultamos.
    if "animal (Bugs Bunny)" in base.hechos:
        print("Bugs Bunny es un animal.")

print("//////////////////////////////////////////")
print("-> Encadenamiento hacia atrás (Backward Chaining)")

#Función para buscar evidencia hacia atrás.
def buscar_evidencia(hipotesis, base):
    if hipotesis in base.hechos:
        return True
    for regla, consecuente in base.reglas.items():
        if hipotesis in consecuente:
            if all(buscar_evidencia(antecedente, base) for antecedente in regla):
                return True
    return False

#Clase para la base de conocimientos.
class BaseConocimientos:
    def __init__(self):
        self.hechos = set() #Conjunto para almacenar hechos.
        self.reglas = {} #Diccionario para almacenar reglas.

    def agregar_hecho(self, hecho):
        self.hechos.add(hecho) #Método para agregar hechos a la base de conocimientos.

    def agregar_regla(self, regla, consecuente):
        self.reglas[tuple(regla)] = consecuente #Método para agregar reglas a la base de conocimientos.


if __name__ == "__main__":
    base = BaseConocimientos()

    #Hechos iniciales.
    base.agregar_hecho("conejo (Bugs Bunny)")

    #Reglas.
    base.agregar_regla(["conejo (x)"], "mamifero (x)")
    base.agregar_regla(["mamifero (x)"], "animal (x)")

    #Consultamos.
    hipotesis = "animal (Bugs Bunny)"
    if buscar_evidencia(hipotesis, base):
        print(f"{hipotesis} es verdadero.")
    else:
        print(f"No se puede demostrar {hipotesis}.")