#Alejandra Rodriguez Guevara 21310127 6E1

#La unificación es un proceso fundamental en la inferencia lógica que se utiliza para encontrar asignaciones de variables que hagan que dos expresiones lógicas sean iguales.

#Función para unificar dos términos x e y con una sustitución theta.
def unify(x, y, theta):
    if theta is None: #Si theta es None, devolvemos None.
        return None
    elif x == y: #Si x e y son iguales, devolvemos theta.
        return theta
    elif isinstance(x, str) and is_variable(x): #Si x es una variable.
        return unify_var(x, y, theta) #Llamamos a la función para unificar una variable.
    elif isinstance(y, str) and is_variable(y): #Si y es una variable.
        return unify_var(y, x, theta) #Llamamos a la función para unificar una variable.
    elif isinstance(x, list) and isinstance(y, list): #Si x e y son listas.
        if len(x) != len(y): #Si las listas tienen diferentes longitudes, devolvemos None.
            return None
        else:
            #Unificamos recursivamente los elementos de las listas.
            return unify(x[1:], y[1:], unify(x[0], y[0], theta))
    else:
        return None  #En cualquier otro caso, devolvemos None.

#Función para unificar una variable con un término x.
def unify_var(var, x, theta):
    if var in theta: #Si la variable ya está en theta.
        return unify(theta[var], x, theta) #Unificamos el valor de la variable con x.
    elif x in theta: #Si x ya está en theta.
        return unify(var, theta[x], theta) #Unificamos la variable con el valor de x en theta.
    else:
        theta[var] = x #Agregamos la variable con su valor a theta.
        return theta

#Función para verificar si x es una variable.
def is_variable(x):
    return isinstance(x, str) and x.islower() #Una variable es una cadena en minúsculas.

theta = unify(["?x", "?y", "?z"], ["a", "b", "c"], {}) #Unificamos las listas.
print(theta)  #Imprimimos el resultado de la unificación.
#Salida estimada: {'?x': 'a', '?y': 'b', '?z': 'c'}