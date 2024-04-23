#Alejandra Rodriguez Guevara 21310127 6E1

#Prolog es un lenguaje de programación lógica basado en reglas. Permite la representación de conocimiento mediante hechos y reglas lógicas.
#Las reglas se definen en forma de cláusulas de Horn. Se utiliza principalmente para la resolución de problemas basada en lógica, como el 
#procesamiento del lenguaje natural, la inteligencia artificial simbólica y los sistemas expertos.

#CLIPS es un sistema experto desarrollado por la NASA que se utiliza para construir sistemas basados en reglas. Utiliza un lenguaje de 
#programación específico para definir reglas y hechos. Permite la representación de conocimiento mediante reglas de producción, que son 
#disparadas cuando se cumplen ciertas condiciones. CLIPS es ampliamente utilizado en aplicaciones de ingeniería del conocimiento, sistemas 
#expertos, diagnóstico y planificación.

def print_symbol_info(language, symbols):
    #Imprimimos el encabezado con el nombre del lenguaje.
    print(f"{'='*20} {language} {'='*20}")
    
    #Imprimimos la tabla de símbolos con las columnas "Símbolo" y "Descripción".
    print("{:<15} {:<15}".format("Símbolo", "Descripción"))
    
    #Imprimimos una línea divisoria.
    print("-" * 35)
    
    #Iteramos sobre los símbolos y descripciones e imprimimos cada par en una fila de la tabla.
    for symbol, description in symbols.items():
        print("{:<15} {:<15}".format(symbol, description))
    
    #Imprimimos una línea en blanco para separar las secciones de los diferentes lenguajes.
    print("\n")

#Símbolos y descripciones para Prolog.
prolog_symbols = {
    ":-": "Definición de regla",
    "?-": "Consulta",
    ",": "Conjunción lógica",
    ";": "Disyunción lógica",
    "not": "Negación lógica",
    "true": "Valor verdadero",
    "false": "Valor falso"
}

#Símbolos y descripciones para CLIPS.
clips_symbols = {
    "(defrule)": "Definición de regla",
    "(assert)": "Insertar un hecho en la base de hechos",
    "(retract)": "Retirar un hecho de la base de hechos",
    "(modify)": "Modificar un hecho en la base de hechos",
    "(bind)": "Asignar un valor a una variable",
}

#Imprimimos la información de los símbolos para Prolog y CLIPS.
print_symbol_info("Prolog", prolog_symbols)
print_symbol_info("CLIPS", clips_symbols)