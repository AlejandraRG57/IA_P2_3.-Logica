#Alejandra Rodriguez Guevara 21310127 6E1

#Las lógicas de orden superior son extensiones de la lógica de primer orden que permiten cuantificar sobre predicados y funciones, además de sobre variables individuales.

#Función que toma una función y un valor, y aplica la función al valor.
def aplicar_funcion(funcion, valor):
    return funcion(valor)

#Función que eleva un número al cuadrado.
def cuadrado(x):
    return x * x

#Función que devuelve la raíz cuadrada de un número.
def raiz_cuadrada(x):
    return x ** 0.5

#Función principal.
def main():
    numero = 9

    #Aplicamos la función cuadrado al número.
    resultado_cuadrado = aplicar_funcion(cuadrado, numero)
    print("Cuadrado de", numero, ":", resultado_cuadrado)

    #Aplicamos la función raiz_cuadrada al número.
    resultado_raiz = aplicar_funcion(raiz_cuadrada, numero)
    print("Raíz cuadrada de", numero, ":", resultado_raiz)

#Llamamos a la función principal.
if __name__ == "__main__":
    main()