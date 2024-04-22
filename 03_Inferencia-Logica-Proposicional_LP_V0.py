#Alejandra Rodriguez Guevara 21310127 6E1

#La inferencia lógica proposicional se refiere al proceso de deducir nuevas proposiciones o conclusiones a partir de un conjunto
#dado de proposiciones iniciales, utilizando reglas y principios de la lógica proposicional.

def evaluate(expression, values):
    stack = []
    tokens = expression.split()
    for token in tokens:
        if token in values:
            stack.append(values[token])
        elif token == "AND":
            if len(stack) >= 2:  #Verificamos si hay suficientes operandos en la pila
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(operand1 and operand2)
            else:
                return False  #No hay suficientes operandos
        elif token == "OR":
            if len(stack) >= 2:  #Verificamos si hay suficientes operandos en la pila
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(operand1 or operand2)
            else:
                return False  #No hay suficientes operandos
        elif token == "NOT":
            if len(stack) >= 1:  #Verificamos si hay suficientes operandos en la pila
                operand = stack.pop()
                stack.append(not operand)
            else:
                return False  #No hay suficientes operandos
        else:
            stack.append(token)
    if len(stack) == 1:  #Verificamos si quedó un único valor en la pila
        return stack[0]
    else:
        return False  #La expresión no está bien formada

def modus_ponens(premise_1, premise_2, conclusion):
    if evaluate(premise_1, {"P": True}) and evaluate(premise_2, {"P": True}):
        return evaluate(conclusion, {"P": True})
    else:
        return False

premise_1 = "P"
premise_2 = "P AND Q"
conclusion = "Q"
result = modus_ponens(premise_1, premise_2, conclusion)
print("Resultado de Modus Ponens:", result)