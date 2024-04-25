#Alejandra Rodriguez Guevara 21310127 6E1

#El espacio de estados es un modelo abstracto que representa todas las configuraciones posibles de un sistema o problema.

class Estado:
    def __init__(self, bloques):
        #Inicializamos el estado con una lista de bloques.
        self.bloques = bloques

    def __repr__(self):
        #Representación de cadena del estado.
        return f"{self.bloques}"

#Función para generar todos los posibles movimientos entre bloques.
def generar_movimientos(bloques):
    movimientos = []
    #Iteramos sobre todos los pares de bloques.
    for bloque1 in bloques:
        for bloque2 in bloques:
            if bloque1 != bloque2:
                #Agregamos el par de bloques como un movimiento válido.
                movimientos.append((bloque1, bloque2))
    return movimientos

#Definimos el estado inicial.
estado_inicial = Estado({"A", "B", "C"})

#Generamos y mostramos los posibles movimientos entre bloques.
print("Movimientos generados:")
for movimiento in generar_movimientos(estado_inicial.bloques):
    print(movimiento)