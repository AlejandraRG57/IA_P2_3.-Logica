#Alejandra Rodriguez Guevara 21310127 6E1

#El backtracking es un algoritmo de búsqueda que se utiliza en problemas de decisión y optimización, particularmente en 
#aquellos que involucran un espacio de búsqueda grande y que se pueden modelar como un árbol de decisión.

#Función de backtrack para encontrar todas las permutaciones de una lista de elementos.
def backtrack(remaining, path, results):
    if not remaining:
        results.append(path)  #Agregamos la permutación actual al resultado.
    else:
        for i in range(len(remaining)):  #Iteramos sobre los elementos restantes.
            new_path = path + [remaining[i]]  #Agregamos el elemento actual al camino.
            new_remaining = remaining[:i] + remaining[i+1:]  #Eliminamos el elemento actual de los restantes.
            backtrack(new_remaining, new_path, results)  #Llamamos recursivamente con los nuevos valores.

#Función para encontrar todas las permutaciones de una lista de elementos.
def find_permutations(elements):
    permutations = []  #Lista para almacenar las permutaciones encontradas.
    backtrack(elements, [], permutations)  #Llamamos a la función de retroceso para encontrar las permutaciones.
    return permutations  #Devolvemos la lista de permutaciones encontradas.

elements = [1, 2, 3]
permutations = find_permutations(elements)
print("Permutaciones:", permutations)  #Imprimimos las permutaciones encontradas.