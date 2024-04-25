#Alejandra Rodriguez Guevara 21310127 6E1

#La incertidumbre se refiere a la falta de conocimiento completo o la imposibilidad de determinar con certeza el resultado de un evento o la veracidad de una afirmación.
#Los factores de certeza son medidas o indicadores que proporcionan información sobre la confiabilidad o certeza de una afirmación, hipótesis o conclusión.

class SistemaIncertidumbre:
    def __init__(self):
        #Inicialización de la clase SistemaIncertidumbre con un diccionario para almacenar los hechos y su certeza.
        self.hechos = {}

    def agregar_hecho(self, hecho, certeza):
        #Método para agregar un hecho con su nivel de certeza al sistema.
        self.hechos[hecho] = certeza

    def consultar_hecho(self, hecho):
        #Método para consultar el nivel de certeza de un hecho en el sistema.
        if hecho in self.hechos:
            return self.hechos[hecho]
        else:
            return None #Devolvemos None si el hecho no está presente en el sistema.

sistema = SistemaIncertidumbre()
sistema.agregar_hecho("lluvia", 0.8) #Se está bastante seguro de que está lloviendo.
sistema.agregar_hecho("sol", 0.5) #Se está menos seguro de que esté soleado.
sistema.agregar_hecho("nieve", 0.2) #Se tiene poca certeza de que esté nevando.

#Consultamos el nivel de certeza de diferentes hechos.
print("Certeza de lluvia:", sistema.consultar_hecho("lluvia"))
print("Certeza de sol:", sistema.consultar_hecho("sol"))
print("Certeza de nieve:", sistema.consultar_hecho("nieve"))
print("Certeza de viento:", sistema.consultar_hecho("viento"))