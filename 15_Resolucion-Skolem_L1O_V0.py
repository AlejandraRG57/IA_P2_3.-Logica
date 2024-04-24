#Alejandra Rodriguez Guevara 21310127 6E1

#La resolución Skolem es una variante de la resolución en lógica de primer orden que se utiliza para eliminar los cuantificadores existenciales en una fórmula lógica. 

class Skolem:
    def __init__(self, f):
        self.f = f

    def eliminate_existential(self):
        #Buscamos cuantificadores existenciales.
        for q in self.f:
            if q[0] == 'E':
                variable = q[1]
                #Introducimos una nueva función Skolem.
                self.f.remove(q)
                self.f.append('F' + variable)
                #Reemplazamos todas las instancias de la variable con la función Skolem.
                for i in range(len(self.f)):
                    self.f[i] = self.f[i].replace(variable, 'F' + variable)

    def print_formula(self):
        print(''.join(self.f))


if __name__ == "__main__":
    f = ['ExFx', 'Px', 'Qy', 'Rz']
    skolem = Skolem(f)
    skolem.eliminate_existential()  #Eliminamos cuantificadores existenciales.
    skolem.print_formula()  #Imprimimos la fórmula transformada.