#Alejandra Rodriguez Guevara 21310127 6E1

#En el contexto de sistemas expertos y diagnóstico, las reglas de diagnóstico y causales son herramientas fundamentales para identificar 
#y explicar relaciones entre síntomas y posibles causas de un problema. 

#Definimos las reglas.
reglas = {
    "fiebre": {"diagnostico": "gripe", "causa": None},
    "tos": {"diagnostico": "resfriado", "causa": None},
    "dolor de garganta": {"diagnostico": "resfriado", "causa": None},
    "dolor de cabeza": {"diagnostico": "gripe", "causa": None},
    "erupción cutánea": {"diagnostico": None, "causa": "alergia a un alimento"}
}

#Función para realizar un diagnóstico.
def diagnosticar(sintomas):
    diagnosticos = []
    causas = []
    for sintoma in sintomas:
        if sintoma in reglas:
            if reglas[sintoma]["diagnostico"]:
                diagnosticos.append(reglas[sintoma]["diagnostico"])
            if reglas[sintoma]["causa"]:
                causas.append(reglas[sintoma]["causa"])
    if diagnosticos:
        return "Diagnóstico: " + ", ".join(diagnosticos)
    elif causas:
        return "Causa: " + ", ".join(causas)
    else:
        return "No se puede diagnosticar con los síntomas proporcionados"

sintomas_paciente = ["fiebre", "tos", "dolor de garganta"]
resultado_diagnostico = diagnosticar(sintomas_paciente)
print(resultado_diagnostico)