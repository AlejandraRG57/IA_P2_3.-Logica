#Alejandra Rodriguez Guevara 21310127 6E1

#STRIPS es un método clásico de planificación en inteligencia artificial que se centra en la planificación de acciones para lograr un estado objetivo desde un estado inicial.
#ADL es un lenguaje de descripción de acciones que extiende los enfoques de planificación más simples, permitiendo una representación más expresiva de las acciones y los efectos 
#que tienen sobre el mundo.

class Action:
    def __init__(self, name, preconditions, effects):
        #Definición de una acción con nombre, precondiciones y efectos.
        self.name = name
        self.preconditions = preconditions
        self.effects = effects

def apply_action(state, action):
    #Aplicamos una acción al estado actual.
    #Verificamos si las precondiciones de la acción se cumplen en el estado actual.
    if all(cond in state for cond in action.preconditions):
        #Agregamos los efectos positivos y eliminamos los efectos negativos.
        state.update(action.effects['add'])
        state.difference_update(action.effects['delete'])

def main():
    #Estado inicial.
    initial_state = {'En(Avión, Barcelona)', 'Clear(Tren)'}
    
    #Definición de acciones.
    actions = [
        Action('CargarAvión', {'Clear(Avión)'}, {'add': {'On(Avión, Tren)'}, 'delete': {'Clear(Avión)'}}),
    ]

    # Objetivo.
    goal = {'En(Avión, Tren)'}
    
    #Planificación hacia adelante.
    current_state = initial_state.copy()
    plan = []
    while not all(cond in current_state for cond in goal):
        #Encontramos las acciones aplicables en el estado actual.
        applicable_actions = [action for action in actions if all(cond in current_state for cond in action.preconditions)]
        if not applicable_actions:
            print("No se puede alcanzar el objetivo.")
            break
        chosen_action = applicable_actions[0]  #Elegimos la primera acción aplicable.
        apply_action(current_state, chosen_action)
        plan.append(chosen_action.name)

    print("Plan encontrado:")
    print(plan)

if __name__ == "__main__":
    main()