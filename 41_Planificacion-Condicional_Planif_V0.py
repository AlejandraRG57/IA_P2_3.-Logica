#Alejandra Rodriguez Guevara 21310127 6E1

#La planificación condicional es un enfoque en la planificación automatizada que considera la incertidumbre en el entorno 
#y toma decisiones basadas en condiciones que pueden ocurrir o no.

#Definición de la función de búsqueda en profundidad para planificar tareas condicionales.
def dfs(task, tasks, visited, schedule):
    #Marcamos la tarea actual como visitada.
    visited.add(task)
    #Iteramos sobre las dependencias de la tarea actual.
    for dependency in tasks[task]['dependencies']:
        #Si la dependencia no ha sido visitada, llamamos recursivamente a dfs para esa dependencia.
        if dependency not in visited:
            dfs(dependency, tasks, visited, schedule)
    #Verificamos si se cumplen todas las condiciones de la tarea actual.
    if all(condition() for condition in tasks[task]['conditions']):
        #Si se cumplen las condiciones, agregamos la tarea al plan de ejecución.
        schedule.append(task)

#Función para planificar tareas condicionales.
def conditional_schedule(tasks):
    #Conjunto para mantener un registro de tareas visitadas.
    visited = set()
    #Lista para almacenar el orden de ejecución de las tareas.
    schedule = []
    #Iteramos sobre todas las tareas disponibles.
    for task in tasks:
        #Si la tarea actual no ha sido visitada, llamamos a dfs para encontrar su orden de ejecución.
        if task not in visited:
            dfs(task, tasks, visited, schedule)
    return schedule

tasks = {
    'Tarea 1': {
        'dependencies': [], #Lista de dependencias de la tarea 1.
        'conditions': [lambda: True] #Lista de condiciones para ejecutar la tarea 1.
    },
    'Tarea 2': {
        'dependencies': ['Tarea 1'], #Lista de dependencias de la tarea 2.
        'conditions': [lambda: True] #Lista de condiciones para ejecutar la tarea 2.
    },
    'Tarea 3': {
        'dependencies': ['Tarea 1'], #Lista de dependencias de la tarea 3.
        'conditions': [lambda: False] #Lista de condiciones para ejecutar la tarea 3.
    },
    'Tarea 4': {
        'dependencies': ['Tarea 2', 'Tarea 3'], #Lista de dependencias de la tarea 4.
        'conditions': [lambda: True, lambda: True] #Lista de condiciones para ejecutar la tarea 4.
    },
    'Tarea 5': {
        'dependencies': ['Tarea 4'], #Lista de dependencias de la tarea 5.
        'conditions': [lambda: True] #Lista de condiciones para ejecutar la tarea 5.
    }
}

#Planificamos las tareas condicionales.
schedule = conditional_schedule(tasks)

#Imprimimos el orden de ejecución de las tareas condicionales.
print("Orden de ejecución de las tareas condicionales:")
for task in schedule:
    print(task)