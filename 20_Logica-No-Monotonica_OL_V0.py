#Alejandra Rodriguez Guevara 21310127 6E1

#La lógica no monotónica es una extensión de la lógica formal que permite razonar sobre situaciones en las que la adición de nuevas 
#premisas puede llevar a la retirada o revisión de conclusiones previamente alcanzadas.

#Definición de creencias iniciales
creencias = {"pájaros_vuelan": True, "pingüinos_vuelan": False}

#Reglas de inferencia.
def inferir_nueva_creencia(creencias):
    if creencias["pájaros_vuelan"] and not creencias["pingüinos_vuelan"]:
        return {"pingüinos_vuelan": True} #Inferir que los pingüinos vuelan.
    else:
        return {} #No se puede inferir nada nuevo.

#Función para actualizar creencias.
def actualizar_creencias(creencias):
    nuevas_creencias = inferir_nueva_creencia(creencias)
    creencias.update(nuevas_creencias)
    return creencias

#Creencias después de la actualización.
print("Creencias antes de la actualización:", creencias)
nuevas_creencias = actualizar_creencias(creencias)
print("Creencias después de la actualización:", nuevas_creencias)