#Alejandra Rodriguez Guevara 21310127 6E1

#Una taxonomía es una estructura jerárquica que organiza y clasifica los conceptos en un dominio de conocimiento en categorías y subcategorías. 

class Categoria:
    def __init__(self, nombre, super_categoria=None):
        #Inicialización de la clase Categoría con un nombre y una lista de subcategorías.
        self.nombre = nombre
        self.subcategorias = []
        #Si se proporciona una super categoría, agregamos esta categoría como subcategoría de la super categoría.
        if super_categoria:
            super_categoria.agregar_subcategoria(self)

    def agregar_subcategoria(self, subcategoria):
        #Método para agregar una subcategoría a esta categoría.
        self.subcategorias.append(subcategoria)

    def __str__(self):
        #Método para representar la categoría como una cadena de caracteres.
        return self.nombre

class Objeto:
    def __init__(self, nombre, categoria):
        #Inicialización de la clase Objeto con un nombre y una categoría.
        self.nombre = nombre
        self.categoria = categoria

    def __str__(self):
        #Método para representar el objeto como una cadena de caracteres.
        return f"{self.nombre} ({self.categoria})"

#Creamos algunas categorías.
animal = Categoria("Animal")
mamifero = Categoria("Mamífero", animal)
ave = Categoria("Ave", animal)
perro = Categoria("Perro", mamifero)
gato = Categoria("Gato", mamifero)
loro = Categoria("Loro", ave)

#Creamos algunos objetos.
obj1 = Objeto("Labrador", perro)
obj2 = Objeto("Siames", gato)
obj3 = Objeto("Canario", loro)

#Mostramos la jerarquía de categorías y algunos objetos.
print("Categorías:")
print(animal)
for subcat in animal.subcategorias:
    print(f"- {subcat}")
    for subsubcat in subcat.subcategorias:
        print(f"  - {subsubcat}")

print("\nObjetos:")
print(obj1)
print(obj2)
print(obj3)