#Alejandra Rodriguez Guevara 21310127 6E1

#Los agentes lógicos son una clase de agentes inteligentes que toman decisiones basadas en la lógica formal. 
#Estos agentes utilizan el razonamiento lógico para procesar información, inferir conclusiones y tomar acciones en su entorno.

class SistemaExperto:
    def __init__(self):
        self.base_conocimiento = {}  #Base de conocimiento del sistema.

    def agregar_hecho(self, hecho, valor):
        self.base_conocimiento[hecho] = valor  #Agregamos un hecho a la base de conocimiento.

    def inferir(self, reglas):
        for regla in reglas:
            premisas, conclusion = regla
            if all(self.base_conocimiento.get(p, False) for p in premisas):
                return conclusion  #Retornamos la conclusión de la primera regla que se cumpla.
        return "No se puede llegar a una conclusión"  #Si ninguna regla se cumple, retornamos un mensaje de error.

sistema = SistemaExperto()

#Definimos los hechos.
sistema.agregar_hecho("llueve", True)
sistema.agregar_hecho("trafico", True)

#Definimos las reglas.
reglas = [
    (["llueve"], "usar paraguas"),
    (["trafico"], "tomar ruta alternativa"),
    (["llueve", "trafico"], "quedarse en casa"),
]

decision = sistema.inferir(reglas)
print("Decisión:", decision)  #Imprimimos la decisión tomada por el sistema experto.