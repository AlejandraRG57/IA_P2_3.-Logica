#Alejandra Rodriguez Guevara 21310127 6E1

#GRAPHPLAN es conocido por su eficiencia en la resolución de problemas de planificación, especialmente para problemas de tamaño moderado a grande.
#La estructura jerárquica del grafo de planificación y las técnicas de búsqueda eficientes contribuyen a su rendimiento.

class GraphPlan:
    def __init__(self):
        self.graph = {} #Diccionario para almacenar las relaciones entre acciones y estados.

    def add_action(self, action, preconditions, effects):
        self.graph[action] = {'preconditions': preconditions, 'effects': effects}

    def is_valid_plan(self, plan):
        current_state = set() #Estado inicial vacío.
        for action in plan:
            if not all(precondition in current_state for precondition in self.graph[action]['preconditions']):
                return False
            current_state.update(self.graph[action]['effects'])
        return True

if __name__ == "__main__":
    planner = GraphPlan()

    #Agregamos acciones y sus precondiciones y efectos.
    planner.add_action("A", preconditions={"P"}, effects={"Q"})
    planner.add_action("B", preconditions={"Q"}, effects={"R"})
    planner.add_action("C", preconditions={"R"}, effects={"P"})

    valid_plan = ["A", "B", "C"]
    print(f"¿El plan {valid_plan} es válido? {planner.is_valid_plan(valid_plan)}")

    invalid_plan = ["B", "A", "C"]
    print(f"¿El plan {invalid_plan} es válido? {planner.is_valid_plan(invalid_plan)}")