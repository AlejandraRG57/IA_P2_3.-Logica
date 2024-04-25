#Alejandra Rodriguez Guevara 21310127 6E1

#La ambigüedad es un concepto que se encuentra en diversos ámbitos del lenguaje, la comunicación y la lógica. 
#Se refiere a situaciones en las que una expresión puede tener más de un significado o interpretación.

def tratar_ambiguedad(oracion):
    #Representamos las dos interpretaciones como proposiciones lógicas.
    banco_financiero = "Enfocado en las finanzas"
    banco_geografico = "Enfocado en la ubicacion"

    #Verificamos si la palabra "banco" está presente en la oración.
    if "banco" in oracion.lower():
        if "financiero" in oracion.lower():
            print(banco_financiero)
        elif "geográfico" in oracion.lower():
            print(banco_geografico)
        else:
            print("No se puede determinar la interpretación exacta.")
    else:
        print("La palabra 'banco' no está en la oración.")

if __name__ == "__main__":
    oracion_ejemplo = "El banco es una estructura cerca del río en un ambiente geográfico"
    tratar_ambiguedad(oracion_ejemplo)