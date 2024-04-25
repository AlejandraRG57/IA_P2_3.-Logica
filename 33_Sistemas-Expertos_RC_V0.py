#Alejandra Rodriguez Guevara 21310127 6E1

#Los sistemas expertos son sistemas de inteligencia artificial que emulan la capacidad de un experto humano para tomar decisiones en un dominio específico. 

class SistemaExperto:
    def __init__(self, base_conocimiento):
        #Inicialización de la clase SistemaExperto con una base de conocimiento.
        self.base_conocimiento = base_conocimiento

    def consultar(self, pregunta):
        #Método para consultar el sistema experto con una pregunta.
        for regla in self.base_conocimiento:
            #Iteramos sobre cada regla en la base de conocimiento.
            if regla['condicion'](pregunta):
                #Verificamos si la pregunta cumple la condición de la regla actual.
                return regla['respuesta']
                #Si la pregunta cumple la condición, devolvemos la respuesta asociada.
        return "Lo siento, no tengo suficiente información para responder a esa pregunta."
        #Si ninguna regla se cumple, devolvemos un mensaje indicando falta de información.

#Definimos la base de conocimiento.
base_conocimiento = [
    {
        'condicion': lambda x: x == 'síntoma1',
        'respuesta': 'Diagnóstico 1'
    },
    {
        'condicion': lambda x: x == 'síntoma2',
        'respuesta': 'Diagnóstico 2'
    },
    #Añadimos más reglas según sea necesario.
]

#Creamos el sistema experto.
sistema_experto = SistemaExperto(base_conocimiento)

#Consultamos el sistema experto con un síntoma.
resultado = sistema_experto.consultar('síntoma1')
print("Diagnóstico:", resultado)