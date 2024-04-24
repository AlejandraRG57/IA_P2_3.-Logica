#Alejandra Rodriguez Guevara 21310127 6E1

#La inferencia difusa es el proceso de realizar razonamientos y tomar decisiones basadas en la lógica difusa.

#Funciones de pertenencia para temperatura y humedad.
def membresia_temperatura(temperatura):
    #Función de pertenencia para la temperatura.
    if temperatura <= 50:
        return temperatura / 50
    elif 50 < temperatura <= 100:
        return (100 - temperatura) / 50
    else:
        return 0

def membresia_humedad(humedad):
    #Función de pertenencia para la humedad.
    if humedad <= 50:
        return humedad / 50
    elif 50 < humedad <= 100:
        return (100 - humedad) / 50
    else:
        return 0

#Inferencia difusa.
def inferencia_difusa(temperatura, humedad):
    #Función de inferencia difusa que calcula la velocidad del ventilador.
    pertenencia_temperatura = membresia_temperatura(temperatura)
    pertenencia_humedad = membresia_humedad(humedad)

    velocidad_ventilador = min(pertenencia_temperatura, pertenencia_humedad)
    #La velocidad del ventilador se determina como el mínimo de las pertenencias de temperatura y humedad.
    return velocidad_ventilador

temperatura_ambiente = 30
humedad_ambiente = 70

velocidad_ventilador = inferencia_difusa(temperatura_ambiente, humedad_ambiente)
print("Velocidad del ventilador:", velocidad_ventilador)