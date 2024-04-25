#Alejandra Rodriguez Guevara 21310127 6E1

#El modelo probabilista racional es un enfoque en la teoría de la decisión que busca describir cómo los agentes racionales toman decisiones en entornos inciertos o probabilísticos.

import random

def decision_paraguas(probabilidad_lluvia, umbral):
    #Función para tomar la decisión de llevar un paraguas o no.
    if probabilidad_lluvia >= umbral:
        return "Llevar un paraguas"
    else:
        return "No llevar un paraguas"

#Probabilidad de lluvia (0% - 100%).
probabilidad_lluvia = random.uniform(0, 1)
print("Probabilidad de lluvia:", probabilidad_lluvia)

#Umbral de decisión (0% - 100%).
umbral = 0.5

#Tomamos la decisión.
decision = decision_paraguas(probabilidad_lluvia, umbral)
print("Decisión:", decision)