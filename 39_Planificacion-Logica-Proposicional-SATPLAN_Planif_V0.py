#Alejandra Rodriguez Guevara 21310127 6E1

#SATPLAN es un algoritmo de planificación basado en la satisfacibilidad booleana (SAT), que se utiliza para resolver problemas de planificación 
#en los que se modela la planificación como un problema de satisfacibilidad proposicional.

import pycosat

def create_formula():
    #Estados iniciales y objetivos.
    initial_states = ["C(A, X)", "S(A, Y)"]
    goal_states = ["S(A, Y)"]

    #Acciones.
    actions = ["C(A, X)", "S(A, Y)", "M(A, X, Y)"]

    #Creamos cláusulas para la fórmula booleana.
    clauses = []
    for action in actions:
        clauses.append([actions.index(action) + 1]) #Cada acción es verdadera o falsa.
        for state in initial_states:
            clauses.append([-(actions.index(action) + 1), initial_states.index(state) + 1]) #Si la acción es falsa, el estado no cambia.
        for state in goal_states:
            clauses.append([actions.index(action) + 1, goal_states.index(state) + 1]) #Si la acción es verdadera, el estado objetivo se cumple.

    return clauses, actions #Retornamos también la lista de acciones.

def solve_satplan():
    formula, actions = create_formula() #Obtenemos la fórmula y las acciones.
    solution = pycosat.solve(formula)

    if solution is None: #Verificamos si no se encontró una solución.
        print("No se encontró un plan válido.")
    else:
        plan = [actions[action - 1] for action in solution if action > 0] #Reconstruimos el plan usando las acciones.
        print(f"Plan válido encontrado: {plan}")

if __name__ == "__main__":
    solve_satplan()