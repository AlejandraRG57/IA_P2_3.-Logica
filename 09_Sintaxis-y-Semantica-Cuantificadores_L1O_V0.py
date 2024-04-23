#Alejandra Rodriguez Guevara 21310127 6E1

#En la lógica de primer orden, los cuantificadores son elementos fundamentales que permiten expresar afirmaciones sobre la cantidad de objetos que satisfacen ciertas propiedades.

#Definimos el dominio de elementos.
personas = ["Juan", "María", "Pedro", "Ana"]

#Definimos los predicados.
es_mujer = ["María", "Ana"]
es_hombre = ["Juan", "Pedro"]

#Cuantificador universal: Para todo elemento del dominio, si es mujer, entonces es inteligente.
for persona in personas:
    if persona in es_mujer:
        print(persona + " es inteligente")

#Cuantificador existencial: Existe al menos un hombre que es alto.
for hombre in es_hombre:
    if hombre == "Pedro":
        print(hombre + " es alto")
        break
else:
    print("No hay hombres altos")

#Cuantificador existencial negado: No hay mujeres altas.
for mujer in es_mujer:
    if mujer == "Ana":
        print(mujer + " no es alta")
        break
else:
    print("Todas las mujeres son altas")