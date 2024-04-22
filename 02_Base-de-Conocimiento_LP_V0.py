#Alejandra Rodriguez Guevara 21310127 6E1

#Una base de conocimiento es un repositorio organizado de información estructurada y semántica, diseñado para almacenar, gestionar y acceder a conocimientos de manera eficiente.

#Definimos la base de conocimiento.
base_conocimiento = {
    "P": "Hoy es lunes",
    "Q": "Está lloviendo",
    "R": "Es un día festivo",
    "regla_1": "(P and Q) or R",
    "regla_2": "(not P) or (not Q)"
}

#Accedemos a la base de conocimiento.
print("¿Qué significa P?", base_conocimiento["P"])
print("¿Cuál es la regla 1?", base_conocimiento["regla_1"])