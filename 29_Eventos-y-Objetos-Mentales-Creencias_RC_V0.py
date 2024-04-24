#Alejandra Rodriguez Guevara 21310127 6E1

#En el ámbito de la inteligencia artificial y la representación del conocimiento, las creencias son elementos fundamentales que reflejan 
#el estado cognitivo de un agente inteligente sobre el mundo que lo rodea.

class Creencias:
    def __init__(self):
        #Inicialización de la clase Creencias con un diccionario de afirmaciones.
        self.afirmaciones = {}

    def agregar_afirmacion(self, afirmacion, verdad=True):
        #Método para agregar una afirmación al conjunto de creencias.
        self.afirmaciones[afirmacion] = verdad

    def eliminar_afirmacion(self, afirmacion):
        #Método para eliminar una afirmación del conjunto de creencias.
        if afirmacion in self.afirmaciones:
            del self.afirmaciones[afirmacion]

    def obtener_verdad(self, afirmacion):
        #Método para obtener la verdad de una afirmación.
        return self.afirmaciones.get(afirmacion)

    def __str__(self):
        #Método para representar las creencias como una cadena de caracteres.
        return "\n".join([f"{afirmacion}: {verdad}" for afirmacion, verdad in self.afirmaciones.items()])

#Creamos las creencias iniciales.
creencias = Creencias()
creencias.agregar_afirmacion("Los pájaros vuelan")
creencias.agregar_afirmacion("Los pingüinos no vuelan", verdad=False)

#Mostramos las creencias.
print("Creencias iniciales:")
print(creencias)

#Modificamos las creencias.
creencias.agregar_afirmacion("Los peces nadan")
creencias.eliminar_afirmacion("Los pájaros vuelan")

#Mostramos las creencias actualizadas.
print("\nCreencias actualizadas:")
print(creencias)