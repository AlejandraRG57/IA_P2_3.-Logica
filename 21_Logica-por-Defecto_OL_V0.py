#Alejandra Rodriguez Guevara 21310127 6E1

#La lógica por defecto es una forma de lógica no monotónica que permite representar el conocimiento de manera flexible, 
#permitiendo que algunas conclusiones sean retiradas o revisadas bajo ciertas circunstancias. 

#Definición de creencias iniciales.
creencias = {
    'pájaros_vuelan': True,
    'pingüinos_vuelan': False
}

#Reglas por defecto.
reglas_por_defecto = {
    'pájaros_vuelan': True #Por defecto, se asume que los pájaros vuelan.
}

#Función para actualizar las creencias utilizando la lógica por defecto.
def actualizar_creencias(conocimiento, reglas_por_defecto):
    for clave, valor in reglas_por_defecto.items():
        if clave not in conocimiento:
            conocimiento[clave] = valor
    return conocimiento

#Creencias antes de la actualización.
print("Creencias antes de la actualización:", creencias)

#Actualizamos las creencias utilizando la lógica por defecto.
creencias_actualizadas = actualizar_creencias(creencias, reglas_por_defecto)

#Creencias después de la actualización.
print("Creencias después de la actualización:", creencias_actualizadas)