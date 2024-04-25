#Alejandra Rodriguez Guevara 21310127 6E1

#La planificación continua y multiagente es un enfoque en la planificación automatizada que aborda problemas donde múltiples agentes deben 
#coordinar sus acciones para lograr objetivos comunes en entornos dinámicos y continuos.

import random
import time

#Definición de la clase Agente.
class Agente:
    def __init__(self, nombre):
        self.nombre = nombre

    #Método para planificar una acción aleatoria.
    def planificar_accion(self):
        return random.choice(['Acción 1', 'Acción 2', 'Acción 3'])

    #Método para ejecutar una acción.
    def ejecutar_accion(self, accion):
        print(f"{self.nombre} ejecuta la acción: {accion}")
        time.sleep(1)  #Simulamos el tiempo de ejecución de la acción.

    #Método para monitorear el entorno.
    def monitorizar_entorno(self):
        #Simulamos la monitorización del entorno.
        cambio_detectado = random.choice([True, False])
        if cambio_detectado:
            print(f"{self.nombre} detecta un cambio en el entorno.")
        return cambio_detectado

#Función para la planificación continua.
def planificacion_continua(agents):
    while True:
        #Planificamos acciones para cada agente.
        for agent in agents:
            accion = agent.planificar_accion() #Planificamos una acción.
            agent.ejecutar_accion(accion) #Ejecutamos la acción planificada.

        #Monitorizamos el entorno y replanificamos si es necesario.
        cambio_detectado = any(agent.monitorizar_entorno() for agent in agents)
        if cambio_detectado:
            print("Replanificando acciones...")

        time.sleep(2) #Esperamos antes de la siguiente iteración.

#Creamos instancias de agentes.
agente1 = Agente("Agente 1")
agente2 = Agente("Agente 2")

#Iniciamos planificación continua con los agentes creados.
planificacion_continua([agente1, agente2])