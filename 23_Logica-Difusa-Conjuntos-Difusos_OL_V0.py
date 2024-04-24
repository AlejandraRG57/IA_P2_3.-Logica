#Alejandra Rodriguez Guevara 21310127 6E1

#Los conjuntos difusos son una extensión de los conjuntos clásicos que permiten representar la incertidumbre 
#y la imprecisión al asignar grados de membresía a los elementos de un conjunto en lugar de una pertenencia binaria.

class ConjuntoDifuso:
    def __init__(self, nombre, funcion_pertenencia):
        #Inicialización de la clase ConjuntoDifuso con un nombre y una función de pertenencia.
        self.nombre = nombre
        self.funcion_pertenencia = funcion_pertenencia

    def pertenencia(self, x):
        #Método para calcular el grado de pertenencia de un valor x al conjunto difuso.
        return self.funcion_pertenencia(x)


#Funciones de pertenencia comunes.
def triangulo(x, a, b, c):
    #Función de pertenencia triangular.
    if a <= x <= b:
        return (x - a) / (b - a)
    elif b < x <= c:
        return (c - x) / (c - b)
    else:
        return 0.0


def trapezoidal(x, a, b, c, d):
    #Función de pertenencia trapezoidal.
    if a <= x <= b:
        return (x - a) / (b - a)
    elif b < x <= c:
        return 1.0
    elif c < x <= d:
        return (d - x) / (d - c)
    else:
        return 0.0


#Definición de conjuntos difusos.
temperatura = ConjuntoDifuso("Temperatura", lambda x: triangulo(x, 15, 20, 25))
humedad = ConjuntoDifuso("Humedad", lambda x: trapezoidal(x, 40, 50, 70, 80))

x = 22
print(f"Pertenencia a {temperatura.nombre} a {x} grados: {temperatura.pertenencia(x)}")
print(f"Pertenencia a {humedad.nombre} a {x}% de humedad: {humedad.pertenencia(x)}")