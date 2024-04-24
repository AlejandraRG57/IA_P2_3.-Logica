#Alejandra Rodriguez Guevara 21310127 6E1

#En el contexto de la inteligencia artificial y la representación del conocimiento, los marcos son estructuras que permiten organizar y representar
#información sobre objetos, situaciones, eventos o conceptos complejos de manera jerárquica. 

class Marco:
    def __init__(self, nombre, atributos=None):
        #Inicialización de la clase Marco con un nombre y un diccionario de atributos.
        self.nombre = nombre
        #Si no se proporcionan atributos, se inicializa como un diccionario vacío.
        self.atributos = atributos if atributos else {}

    def agregar_atributo(self, nombre, valor):
        #Método para agregar un atributo al marco.
        self.atributos[nombre] = valor

    def obtener_atributo(self, nombre):
        #Método para obtener el valor de un atributo dado su nombre.
        return self.atributos.get(nombre)

    def __str__(self):
        #Método para representar el marco como una cadena de caracteres.
        return f"Marco: {self.nombre}\nAtributos: {self.atributos}"

#Creamos algunos marcos.
marco_persona = Marco("Persona", {"nombre": "Juan", "edad": 30, "genero": "masculino"})
marco_vehiculo = Marco("Vehículo", {"marca": "Toyota", "modelo": "Corolla", "año": 2020})
marco_evento = Marco("Evento", {"nombre": "Conferencia", "fecha": "2024-05-15", "lugar": "Ciudad X"})

#Agregamos atributos adicionales.
marco_persona.agregar_atributo("profesion", "Ingeniero")
marco_vehiculo.agregar_atributo("color", "Azul")
marco_evento.agregar_atributo("hora", "10:00")

#Mostramos los marcos.
print(marco_persona)
print(marco_vehiculo)
print(marco_evento)