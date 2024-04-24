#Alejandra Rodriguez Guevara 21310127 6E1

#Fuzzy CLIPS es una extensión de CLIPS, un lenguaje de programación de reglas utilizado en sistemas expertos, que integra 
#uncionalidades de lógica difusa para el razonamiento y la toma de decisiones.

#Función para calcular la pertenencia a un conjunto difuso triangular.
def pertenencia_triangulo(x, a, b, c):
    if x <= a or x >= c:
        return 0
    elif a < x <= b:
        return (x - a) / (b - a)
    else:
        return (c - x) / (c - b)

#Definimos los parámetros del conjunto difuso triangular.
a = 20
b = 30
c = 40

#Calculamos la pertenencia de 25 al conjunto difuso triangular.
valor = 25
pertenencia = pertenencia_triangulo(valor, a, b, c)
print(f"Pertenencia de {valor} al conjunto difuso triangular: {pertenencia}")

#Calculamos la pertenencia de 35 al conjunto difuso triangular.
valor = 35
pertenencia = pertenencia_triangulo(valor, a, b, c)
print(f"Pertenencia de {valor} al conjunto difuso triangular: {pertenencia}")