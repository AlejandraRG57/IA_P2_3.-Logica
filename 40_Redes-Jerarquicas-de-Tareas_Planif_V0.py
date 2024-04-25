#Alejandra Rodriguez Guevara 21310127 6E1

#Una red jerárquica de tareas es una representación visual de un proyecto o proceso, donde las tareas se organizan en una estructura jerárquica que muestra la relación entre ellas.

#Definición de la función de búsqueda en profundidad.
def dfs(task, tasks, visited, schedule):
    #Marcamos la tarea actual como visitada.
    visited.add(task)
    #Iteramos sobre las dependencias de la tarea actual.
    for dependency in tasks[task]:
        #Si la dependencia no ha sido visitada, llamamos recursivamente a dfs para esa dependencia.
        if dependency not in visited:
            dfs(dependency, tasks, visited, schedule)
    #Después de visitar todas las dependencias, agregamos la tarea actual a la lista de planificación.
    schedule.append(task)

#Función para planificar las tareas.
def schedule_tasks(tasks):
    #Conjunto para mantener un registro de tareas visitadas.
    visited = set()
    #Lista para almacenar el orden de ejecución de las tareas.
    schedule = []
    #Iteramos sobre todas las tareas disponibles.
    for task in tasks:
        #Si la tarea actual no ha sido visitada, llamamos a dfs para encontrar su orden de ejecución.
        if task not in visited:
            dfs(task, tasks, visited, schedule)
    #Invertimos el orden de la lista de planificación para obtener el orden correcto de ejecución.
    schedule.reverse()
    return schedule

tasks = {
    'Tarea 1': [],
    'Tarea 2': ['Tarea 1'],
    'Tarea 3': ['Tarea 1'],
    'Tarea 4': ['Tarea 2', 'Tarea 3'],
    'Tarea 5': ['Tarea 4'],
    'Tarea 6': ['Tarea 4'],
    'Tarea 7': ['Tarea 5', 'Tarea 6']
}

#Planificamos las tareas.
schedule = schedule_tasks(tasks)

#Imprimimos el orden de ejecución de las tareas.
print("Orden de ejecución de las tareas:")
for task in schedule:
    print(task)