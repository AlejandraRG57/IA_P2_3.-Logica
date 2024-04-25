#Alejandra Rodriguez Guevara 21310127 6E1

#La vigilancia de ejecución y replanificación es un proceso utilizado en la planificación automatizada y los sistemas de control 
#para monitorear la ejecución de un plan y realizar ajustes dinámicos en respuesta a cambios en el entorno o fallos en la ejecución del plan inicial.

import time

#Función para ejecutar un plan de acciones.
def execute_plan(plan):
    print("Ejecutando plan:")
    #Iteramos sobre cada acción en el plan.
    for action in plan:
        print(f"Ejecutando acción: {action}")
        time.sleep(1)  #Simulamos el tiempo de ejecución de cada acción.

#Función para monitorear la ejecución del plan.
def monitor_execution(plan):
    print("Monitoreando la ejecución del plan...")
    #Simulamos la monitorización.
    time.sleep(5)
    print("¡Se ha detectado un cambio en el entorno!")
    return True  #Simulamos que se detecta un cambio en el entorno.

#Función para replanificar el plan.
def replan(plan):
    print("Replanificando el plan...")
    #Simulamos la replanificación.
    new_plan = ['Nueva acción 1', 'Nueva acción 2', 'Nueva acción 3']
    return new_plan

#Generamos un plan inicial.
initial_plan = ['Acción 1', 'Acción 2', 'Acción 3']

#Ejecutamos el plan inicial.
execute_plan(initial_plan)

#Monitoreamos la ejecución del plan y detectamos cambios.
change_detected = monitor_execution(initial_plan)

#Si se detecta un cambio, replanificamos el plan y ejecutamos el nuevo plan.
if change_detected:
    new_plan = replan(initial_plan)
    execute_plan(new_plan)
else:
    print("No se detectaron cambios. Finalizando la ejecución.")