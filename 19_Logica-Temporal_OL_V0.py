#Alejandra Rodriguez Guevara 21310127 6E1

#La lógica temporal es una extensión de la lógica formal que se utiliza para razonar sobre el tiempo y las secuencias temporales de eventos.

class Mundo:
    def __init__(self, nombre, relaciones=None):
        #Inicialización de la clase Mundo.
        self.nombre = nombre
        #Si no se proporcionan relaciones, lo inicializamos como un diccionario vacío.
        self.relaciones = relaciones if relaciones else {}

    def agregar_relacion(self, agente, mundo, tiempo):
        #Método para agregar una relación entre este mundo y un agente en un tiempo específico.
        if agente in self.relaciones:
            #Si el agente ya existe en las relaciones, agregamos este mundo y tiempo a su lista de relaciones.
            self.relaciones[agente].append((mundo, tiempo))
        else:
            #Si el agente no existe en las relaciones, creamos una nueva entrada en el diccionario.
            self.relaciones[agente] = [(mundo, tiempo)]

class Agente:
    def __init__(self, nombre):
        #Inicialización de la clase Agente.
        self.nombre = nombre

class ModeloTemporal:
    def __init__(self):
        #Inicialización de la clase ModeloTemporal.
        self.mundos = {} #Diccionario para almacenar los mundos.
        self.agentes = {} #Diccionario para almacenar los agentes.

    def agregar_mundo(self, nombre, relaciones=None):
        #Método para agregar un mundo al modelo temporal.
        mundo = Mundo(nombre, relaciones)
        self.mundos[nombre] = mundo #Agregamos el mundo al diccionario de mundos.
        return mundo

    def agregar_agente(self, nombre):
        #Método para agregar un agente al modelo temporal.
        agente = Agente(nombre)
        self.agentes[nombre] = agente #Agregamos el agente al diccionario de agentes.
        return agente

    def actualizar_relacion(self, agente, mundo_origen, mundo_destino, tiempo):
        #Método para actualizar la relación entre un agente y los mundos en un tiempo específico
        if mundo_origen in self.mundos and mundo_destino in self.mundos:
            #Verificamos que ambos mundos existan en el modelo temporal.
            self.mundos[mundo_origen].agregar_relacion(agente, mundo_destino, tiempo)
        else:
            #Si uno o ambos mundos no existen, mostramos un mensaje de error.
            print("Error: Uno o ambos mundos no existen.")

    def acceso_posible(self, agente, mundo_origen, mundo_destino, tiempo):
        #Método para verificar si un agente puede acceder de un mundo origen a un mundo destino en un tiempo específico.
        if mundo_origen in self.mundos and mundo_destino in self.mundos:
            #Verificamos que ambos mundos existan en el modelo temporal.
            if agente in self.mundos[mundo_origen].relaciones:
                for m, t in self.mundos[mundo_origen].relaciones[agente]:
                    #Iteramos sobre las relaciones del agente en el mundo origen.
                    if m == mundo_destino and t <= tiempo:
                        #Si se encuentra la relación y el tiempo es menor o igual al tiempo dado, devolvemos True.
                        return True
                return False
            else:
                return False #Si el agente no tiene relaciones en el mundo origen, devolvemos False.
        else:
            print("Error: Uno o ambos mundos no existen.") #Si uno o ambos mundos no existen, mostramos un mensaje de error.

#Creamos un modelo temporal.
modelo_temporal = ModeloTemporal()

#Agregamos mundos.
mundo1 = modelo_temporal.agregar_mundo("Mundo1")
mundo2 = modelo_temporal.agregar_mundo("Mundo2")
mundo3 = modelo_temporal.agregar_mundo("Mundo3")

#Agregamos agentes.
agente1 = modelo_temporal.agregar_agente("Agente1")
agente2 = modelo_temporal.agregar_agente("Agente2")

#Establecemos relaciones temporales.
modelo_temporal.actualizar_relacion(agente1, "Mundo1", "Mundo2", 1)
modelo_temporal.actualizar_relacion(agente1, "Mundo2", "Mundo3", 2)
modelo_temporal.actualizar_relacion(agente2, "Mundo1", "Mundo3", 3)

#Verificamos acceso posible en un tiempo específico.
print(modelo_temporal.acceso_posible(agente1, "Mundo1", "Mundo2", 0))  # False
print(modelo_temporal.acceso_posible(agente1, "Mundo1", "Mundo2", 1))  # True
print(modelo_temporal.acceso_posible(agente1, "Mundo1", "Mundo2", 2))  # True
print(modelo_temporal.acceso_posible(agente2, "Mundo1", "Mundo3", 2))  # False
print(modelo_temporal.acceso_posible(agente2, "Mundo1", "Mundo3", 3))  # True
print(modelo_temporal.acceso_posible(agente2, "Mundo1", "Mundo3", 4))  # True