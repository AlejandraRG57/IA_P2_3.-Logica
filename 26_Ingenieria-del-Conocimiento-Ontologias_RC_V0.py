#Alejandra Rodriguez Guevara 21310127 6E1

#La ingeniería del conocimiento aborda cómo representar y manipular el conocimiento de manera efectiva en sistemas computacionales.

#Definición de la clase Ontología.
class Ontologia:
    def __init__(self):
        self.clases = {} #Diccionario para almacenar las clases de la ontología.

    #Método para agregar una clase a la ontología.
    def agregar_clase(self, nombre_clase, super_clase=None):
        if super_clase:
            if super_clase not in self.clases:
                raise ValueError("La superclase no está definida en la ontología.")
            self.clases[nombre_clase] = super_clase
        else:
            self.clases[nombre_clase] = None

    #Método para obtener la superclase de una clase.
    def obtener_super_clase(self, nombre_clase):
        if nombre_clase in self.clases:
            return self.clases[nombre_clase]
        else:
            raise ValueError("La clase no está definida en la ontología.")

#Creamos una instancia de la ontología.
ontologia = Ontologia()

#Agregamos algunas clases a la ontología.
ontologia.agregar_clase("Animal")
ontologia.agregar_clase("Mamifero", "Animal")
ontologia.agregar_clase("Perro", "Mamifero")
ontologia.agregar_clase("Gato", "Mamifero")

#Obtenemos la superclase de una clase.
print(ontologia.obtener_super_clase("Perro"))  #Salida: Mamifero.