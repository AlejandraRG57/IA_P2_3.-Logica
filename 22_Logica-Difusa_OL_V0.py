#Alejandra Rodriguez Guevara 21310127 6E1

#La lógica difusa es una extensión de la lógica clásica que permite manejar la incertidumbre y la imprecisión en el razonamiento al asignar grados de verdad en un continuo.

#Funciones de pertenencia para las variables lingüísticas.
def temperatura_fria(temperatura):
    #Función de pertenencia para temperatura fría.
    if temperatura <= 20:
        return 1
    elif 20 < temperatura < 25:
        return (25 - temperatura) / 5
    else:
        return 0

def temperatura_calida(temperatura):
    #Función de pertenencia para temperatura cálida.
    if 25 <= temperatura <= 30:
        return (temperatura - 25) / 5
    elif 30 < temperatura < 35:
        return (35 - temperatura) / 5
    else:
        return 0

def temperatura_calurosa(temperatura):
    #Función de pertenencia para temperatura calurosa.
    if temperatura >= 35:
        return 1
    elif 30 < temperatura < 35:
        return (temperatura - 30) / 5
    else:
        return 0

def velocidad_lenta(velocidad):
    #Función de pertenencia para velocidad lenta.
    if velocidad <= 20:
        return 1
    elif 20 < velocidad < 40:
        return (40 - velocidad) / 20
    else:
        return 0

def velocidad_media(velocidad):
    #Función de pertenencia para velocidad media.
    if 20 <= velocidad <= 60:
        return (velocidad - 20) / 40
    elif 60 < velocidad < 80:
        return (80 - velocidad) / 20
    else:
        return 0

def velocidad_rapida(velocidad):
    #Función de pertenencia para velocidad rápida.
    if velocidad >= 60:
        return 1
    elif 40 < velocidad < 60:
        return (velocidad - 40) / 20
    else:
        return 0

#Reglas del sistema difuso.
def calcular_velocidad(temperatura):
    #Reglas de inferencia difusa.
    velocidad_baja = min(temperatura_fria(temperatura), velocidad_lenta(20))
    velocidad_media_ = min(temperatura_calida(temperatura), velocidad_media(40))
    velocidad_alta = min(temperatura_calurosa(temperatura), velocidad_rapida(60))

    #Defuzzificación: centroide.
    numerador = velocidad_baja * 20 + velocidad_media_ * 60 + velocidad_alta * 100
    denominador = velocidad_baja + velocidad_media_ + velocidad_alta

    if denominador != 0:
        return numerador / denominador
    else:
        return 0 

#Prueba del sistema difuso.
temperatura_ambiente = 25
velocidad_ventilador = calcular_velocidad(temperatura_ambiente)
print("Temperatura ambiente:", temperatura_ambiente)
print("Velocidad del ventilador:", velocidad_ventilador)