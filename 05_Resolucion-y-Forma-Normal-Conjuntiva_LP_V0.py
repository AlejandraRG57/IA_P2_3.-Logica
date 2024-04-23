#Alejandra Rodriguez Guevara 21310127 6E1

#La resolución y la forma normal conjuntiva (FNC) son conceptos fundamentales en lógica proposicional y se utilizan en la inferencia lógica y la demostración de teoremas. 
#La transformación de una fórmula proposicional en FNC implica aplicar reglas de equivalencia lógica y distribución, y puede implicar la introducción de variables auxiliares 
#si es necesario. 

#Función para eliminar implicaciones.
def remove_implication(formula):
    return formula.replace("->", "|").replace("<->", "&") #Reemplazamos el operador de implicación "->" por "|" y el operador de doble implicación "<->" por "&".

#Función para distribuir las conjunciones sobre las disyunciones.
def distribute_conjunctions(formula):
    conjunctions = formula.split("&") #Dividimos la fórmula en sus conjunciones.
    distributed = []

    for conj in conjunctions: #Para cada conjunción, dividimos en disyunciones.
        disjunctions = conj.split("|")
        distributed.append(disjunctions)

    distributed_formula = [] #Creamos la fórmula distribuida.

    for disjunction_group in zip(*distributed):
        distributed_formula.append("({})".format("&".join(disjunction_group)))

    return "|".join(distributed_formula)

#Función principal para convertir la fórmula en FNC.
def to_fnc(formula):
    formula = remove_implication(formula)#Eliminamos las implicaciones de la fórmula.

    fnc_formula = distribute_conjunctions(formula) #Distribuimos las conjunciones sobre las disyunciones.

    return fnc_formula

formula = "((P | Q)) & ((Q -> R))"
fnc = to_fnc(formula) #Convertimos la fórmula en FNC.
print("Fórmula en FNC:", fnc)