#Alejandra Rodriguez Guevara 21310127 6E1

#Los algoritmos de búsqueda local son técnicas heurísticas utilizadas para encontrar soluciones aproximadas a problemas de optimización 
#combinatoria en los que el objetivo es encontrar la mejor solución posible dentro de un conjunto finito de posibles soluciones.

import random

#Función objetivo.
def funcion_objetivo(x):
    return -(x ** 2)  #Negativo del cuadrado para maximizar.

#Algoritmo de Búsqueda Local (Hill Climbing).
def busqueda_local(funcion_objetivo, x_inicial, paso=0.1, iteraciones=100):
    x_actual = x_inicial
    valor_actual = funcion_objetivo(x_actual)

    for _ in range(iteraciones):
        #Generamos una solución vecina.
        x_vecino = x_actual + random.uniform(-paso, paso)
        valor_vecino = funcion_objetivo(x_vecino)

        #Actualizamos la solución actual si el vecino es mejor.
        if valor_vecino > valor_actual:
            x_actual = x_vecino
            valor_actual = valor_vecino

    return x_actual, valor_actual

#Punto de inicio aleatorio.
x_inicial = random.uniform(-10, 10)

#Ejecutamos la búsqueda local.
solucion, valor_maximo = busqueda_local(funcion_objetivo, x_inicial)

#Imprimir resultados.
print("Solución encontrada:", solucion)
print("Valor máximo encontrado:", valor_maximo)