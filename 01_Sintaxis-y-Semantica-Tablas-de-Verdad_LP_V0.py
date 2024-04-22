#Alejandra Rodriguez Guevara 21310127 6E1

#Las tablas de verdad son herramientas utilizadas en lógica y matemáticas para representar el resultado de todas las 
#combinaciones posibles de valores de verdad para un conjunto de proposiciones.

import itertools

#Función para generar las variables de una expresión lógica.
def generate_variables(expression):
    return sorted(set(char for char in expression if char.isalpha()))

#Función para evaluar una expresión lógica dada un conjunto de valores de variables.
def evaluate(expression, values):
    stack = []
    for char in expression:
        if char.isalpha():
            stack.append(values[char])
        elif char == '¬':
            if stack:
                stack.append(not stack.pop())
            else:
                return False #Si la pila está vacía, devolvemos False.
        elif char == '∧':
            if len(stack) >= 2: #Verificamos si hay suficientes elementos en la pila.
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(operand1 and operand2)
            else:
                return False
        elif char == '∨':
            if len(stack) >= 2: #Verificamos si hay suficientes elementos en la pila.
                operand2 = stack.pop()
                operand1 = stack.pop()
                stack.append(operand1 or operand2)
            else:
                return False
    return stack[0]

#Función para generar todas las combinaciones de valores de variables.
def generate_variable_combinations(variables):
    return list(itertools.product([False, True], repeat=len(variables)))

#Función para generar la tabla de verdad para una expresión lógica.
def truth_table(expression):
    variables = generate_variables(expression)
    combinations = generate_variable_combinations(variables)
    table = []

    for combo in combinations:
        values = dict(zip(variables, combo))
        result = evaluate(expression, values)
        table.append({**values, 'Result': result})

    return table

#Función para imprimir la tabla de verdad de manera legible.
def print_truth_table(table):
    header = list(table[0].keys())
    print(' | '.join(header))
    print('-' * (len(header) * 5))
    for row in table:
        print(' | '.join(str(row[var]) for var in header))

if __name__ == "__main__":
    expression = "(P ∧ Q) ∨ (¬P)"
    table = truth_table(expression)
    print_truth_table(table)