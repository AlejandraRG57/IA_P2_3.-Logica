#Alejandra Rodriguez Guevara 21310127 6E1

#Equivalencia: Dos proposiciones son equivalentes si tienen el mismo valor de verdad para todas las posibles combinaciones de valores de verdad de sus variables proposicionales.
#Validez: Un argumento es válido si, y solo si, todas las interpretaciones en las que todas las premisas son verdaderas también hacen que la conclusión sea verdadera.
#Satisfacibilidad: Una fórmula proposicional es satisfacible si existe al menos una interpretación de las variables proposicionales que hace que la fórmula sea verdadera.

def implies_to_or(p, q):
    #La implicación (P -> Q) se puede representar como (¬P ∨ Q).
    return "(NOT " + p.strip() + ") OR " + q.strip()

def equivalent(formula1, formula2):
    #Convertimos la fórmula 1 a una forma estándar.
    if "Implies" in formula1:
        standard_formula1 = implies_to_or(*map(str.strip, formula1.split("Implies")))
    else:
        standard_formula1 = formula1

    #Convertimos la fórmula 2 a una forma estándar.
    if "Implies" in formula2:
        standard_formula2 = implies_to_or(*map(str.strip, formula2.split("Implies")))
    else:
        standard_formula2 = formula2

    #Verificamos si las fórmulas estándar son equivalentes.
    return standard_formula1 == standard_formula2

#Fórmula 1: P AND Q.
formula_1 = "P AND Q"

#Fórmula 2: P OR Q.
formula_2 = "P OR Q"

#Fórmula 3: Implies(P, Q).
formula_3 = "Implies(P, Q)"

#Verificamos si las fórmulas 1 y 2 son equivalentes.
equivalence_check = equivalent(formula_1, formula_2)
print("¿Las fórmulas 1 y 2 son equivalentes?", equivalence_check)

#Verificamos si las fórmulas 1 y 3 son equivalentes.
equivalence_check = equivalent(formula_1, formula_3)
print("¿Las fórmulas 1 y 3 son equivalentes?", equivalence_check)

#Verificamos si las fórmulas 2 y 3 son equivalentes.
equivalence_check = equivalent(formula_2, formula_3)
print("¿Las fórmulas 2 y 3 son equivalentes?", equivalence_check)