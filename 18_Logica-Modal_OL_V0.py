#Alejandra Rodriguez Guevara 21310127 6E1

#La lógica modal es una extensión de la lógica proposicional o de primer orden que permite expresar y razonar sobre la modalidad.

class Mundo:
    def __init__(self, nombre, relaciones=None):
        #Inicialización de la clase Mundo.
        self.nombre = nombre
        #Si no se proporcionan relaciones, lo inicializamos como un diccionario vacío.
        self.relaciones = relaciones if relaciones else {}

    def agregar_relacion(self, agente, mundo):
        #Método para agregar una relación entre este mundo y un agente.
        if agente in self.relaciones:
            #Si el agente ya existe en las relaciones, agregamos este mundo a su lista de relaciones.
            self.relaciones[agente].append(mundo)
        else:
            #Si el agente no existe en las relaciones, creamos una nueva entrada en el diccionario.
            self.relaciones[agente] = [mundo]

class Agente:
    def __init__(self, nombre):
        #Inicialización de la clase Agente.
        self.nombre = nombre

class Modelo:
    def __init__(self):
        #Inicialización de la clase Modelo.
        self.mundos = {} #Diccionario para almacenar los mundos.
        self.agentes = {} #Diccionario para almacenar los agentes.

    def agregar_mundo(self, nombre, relaciones=None):
        #Método para agregar un mundo al modelo.
        mundo = Mundo(nombre, relaciones)
        self.mundos[nombre] = mundo #Agregamos el mundo al diccionario de mundos.
        return mundo

    def agregar_agente(self, nombre):
        #Método para agregar un agente al modelo.
        agente = Agente(nombre)
        self.agentes[nombre] = agente #Agregamos el agente al diccionario de agentes.
        return agente

    def actualizar_relacion(self, agente, mundo_origen, mundo_destino):
        #Método para actualizar la relación entre un agente y los mundos.
        if mundo_origen in self.mundos and mundo_destino in self.mundos:
            #Verificamos que ambos mundos existan en el modelo.
            self.mundos[mundo_origen].agregar_relacion(agente, mundo_destino)
        else:
            #Si uno o ambos mundos no existen, mostramos un mensaje de error.
            print("Error: Uno o ambos mundos no existen.")

    def acceso_posible(self, agente, mundo_origen, mundo_destino):
        #Método para verificar si un agente puede acceder de un mundo origen a un mundo destino.
        if mundo_origen in self.mundos and mundo_destino in self.mundos:
            #Verificamos que ambos mundos existan en el modelo.
            if agente in self.mundos[mundo_origen].relaciones:
                #Si el agente tiene relaciones en el mundo origen.
                return mundo_destino in self.mundos[mundo_origen].relaciones[agente]
                #Verificamos si el mundo destino está en las relaciones del agente en el mundo origen.
            else:
                return False #Si el agente no tiene relaciones en el mundo origen, devolvemos False.
        else:
            print("Error: Uno o ambos mundos no existen.") #Si uno o ambos mundos no existen, mostramos un mensaje de error.

#Creamos un modelo.
modelo = Modelo()

#Agregamos mundos.
mundo1 = modelo.agregar_mundo("Mundo1")
mundo2 = modelo.agregar_mundo("Mundo2")
mundo3 = modelo.agregar_mundo("Mundo3")

#Agregamos agentes.
agente1 = modelo.agregar_agente("Agente1")
agente2 = modelo.agregar_agente("Agente2")

#Establecemos relaciones.
modelo.actualizar_relacion(agente1, "Mundo1", "Mundo2")
modelo.actualizar_relacion(agente1, "Mundo2", "Mundo3")
modelo.actualizar_relacion(agente2, "Mundo1", "Mundo3")

#Verificamos acceso posible.
print(modelo.acceso_posible(agente1, "Mundo1", "Mundo2"))  # True
print(modelo.acceso_posible(agente1, "Mundo2", "Mundo1"))  # False
print(modelo.acceso_posible(agente2, "Mundo1", "Mundo3"))  # True
print(modelo.acceso_posible(agente2, "Mundo3", "Mundo1"))  # False
