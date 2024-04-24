#Alejandra Rodriguez Guevara 21310127 6E1

#La lógica por defecto y la lógica no monotónica son dos enfoques que permiten razonar sobre la incertidumbre y el 
#cambio en el conocimiento de manera más flexible que la lógica clásica.

class SistemaRazonamiento:
    def __init__(self):
        self.hechos = set()
        self.reglas_por_defecto = {
            "pájaros_vuelan": True, #Asumimos que los pájaros vuelan.
            "pingüinos_vuelan": False #Asumimos que los pingüinos no vuelan.
        }

    def agregar_hecho(self, hecho):
        self.hechos.add(hecho)

    def razonar(self, pregunta):
        if pregunta in self.hechos: #Si el hecho ya está presente, no se realiza razonamiento adicional.
            return True
        elif pregunta in self.reglas_por_defecto: #Si hay una regla por defecto para la pregunta, se asume verdadero.
            print(f"Se asume que {pregunta} es {self.reglas_por_defecto[pregunta]} por defecto")
            return self.reglas_por_defecto[pregunta]
        else:
            print(f"No se puede determinar si {pregunta} es verdadero o falso")
            return None

sistema = SistemaRazonamiento()
sistema.agregar_hecho("pájaros_vuelan")
print(sistema.razonar("pájaros_vuelan")) #True, ya que el hecho está presente.
print(sistema.razonar("pingüinos_vuelan")) #False, según la regla por defecto.
print(sistema.razonar("ballenas_vuelan")) #None, no hay información suficiente para determinar si es verdadero o falso.