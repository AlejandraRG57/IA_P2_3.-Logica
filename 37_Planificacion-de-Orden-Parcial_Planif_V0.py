#Alejandra Rodriguez Guevara 21310127 6E1

#La planificación de orden parcial es un enfoque utilizado en inteligencia artificial para resolver problemas de planificación en los que 
#no es posible especificar un orden total para todas las acciones.

class Action:
    def __init__(self, name, preconditions, effects, order_before=None):
        #Inicializamos una acción con su nombre, precondiciones, efectos y una acción que debe ejecutarse antes.
        self.name = name
        self.preconditions = preconditions
        self.effects = effects
        self.order_before = order_before

    def is_applicable(self, state):
        #Verificamos si la acción es aplicable en un estado dado.
        return all(condition in state for condition in self.preconditions)

    def apply(self, state):
        #Aplicamos los efectos de la acción en un estado dado.
        if self.is_applicable(state):
            new_state = state.copy()
            new_state.update(self.effects)
            return new_state
        else:
            return None

def partial_order_planning(actions):
    #Realizamos la planificación de orden parcial.
    plan = []
    state = set()

    while actions:
        #Encontramos las acciones aplicables en el estado actual.
        applicable_actions = [action for action in actions if action.is_applicable(state)]
        if not applicable_actions:
            print("No se pudo encontrar una solución.")
            return None

        action = None
        #Escogemos una acción que no tenga restricciones de orden o cuyas acciones previas ya estén en el plan.
        for candidate_action in applicable_actions:
            if candidate_action.order_before is None or candidate_action.order_before in plan:
                action = candidate_action
                break

        if action is None:
            print("No se pudo encontrar una solución debido a restricciones de orden.")
            return None

        #Aplicamos la acción al estado y la remueve de las acciones disponibles.
        actions.remove(action)
        state = action.apply(state)
        plan.append(action.name)

    return plan

#Definición de acciones.
actions = [
    Action("Cortar verduras", {"Cuchillo"}, {"Verduras cortadas"}),
    Action("Cocinar carne", {"Carne"}, {"Carne cocinada"}),
    Action("Hervir agua", set(), {"Agua hervida"}),
    Action("Preparar salsa", {"Tomates", "Cebolla"}, {"Salsa lista"}, "Cortar verduras"),
    Action("Hervir pasta", {"Pasta", "Agua hervida"}, {"Pasta cocida"}, "Hervir agua"),
    Action("Servir comida", {"Verduras cortadas", "Carne cocinada", "Pasta cocida", "Salsa lista"}, {"Comida servida"}, "Cocinar carne")
]

#Planificación de orden parcial.
plan = partial_order_planning(actions)

#Mostramos el plan.
if plan:
    print("Plan encontrado:")
    for step, action in enumerate(plan):
        print(f"Paso {step+1}: {action}")