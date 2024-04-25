#Alejandra Rodriguez Guevara 21310127 6E1

#Una "Gramática Causal Definida" es un tipo específico de gramática formal utilizada en el campo de la inteligencia artificial y el modelado causal. 
#Las gramáticas causales definidas se utilizan para representar relaciones causales entre eventos o variables en un sistema.

#Definición de la gramática causal.
causal_grammar = {
    "TEMPERATURA < 0": "FORMACION_DE_HIELO",
    "TEMPERATURA > 0": "NO_HAY_FORMACION_DE_HIELO"
}

#Función para evaluar una relación causal dada una temperatura.
def evaluar_causalidad(temperatura):
    for condicion, resultado in causal_grammar.items():
        if eval(condicion.replace("TEMPERATURA", str(temperatura))):
            return resultado
    return "No se puede determinar la causalidad"

temperatura = -5  #Temperatura en grados Celsius.

resultado_causalidad = evaluar_causalidad(temperatura)
print(f"Para una temperatura de {temperatura}°C, la causalidad es: {resultado_causalidad}")