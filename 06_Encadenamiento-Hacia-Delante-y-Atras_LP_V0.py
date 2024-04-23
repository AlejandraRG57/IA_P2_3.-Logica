#Alejandra Rodriguez Guevara 21310127 6E1

#El encadenamiento hacia adelante y hacia atrás son estrategias utilizadas en sistemas de inferencia basados en reglas para determinar si una afirmación 
#es verdadera o no, utilizando un conjunto de reglas y hechos iniciales.

#En el encadenamiento hacia adelante, se parte de los hechos iniciales y se aplican las reglas de inferencia para generar nuevas afirmaciones hasta que ya no se pueden inferir más.
#En el encadenamiento hacia atrás, se parte de la afirmación que se desea demostrar y se intenta buscar qué hechos o reglas pueden justificar esa afirmación.

#Definimos de la clase Rule.
class Rule:
    def __init__(self, condition, result):
        self.condition = condition  #Condiciones de la regla.
        self.result = result        #Resultado de la regla.

#Definimos de la clase ForwardChaining.
class ForwardChaining:
    def __init__(self, rules):
        self.rules = rules  #Lista de reglas.
        self.facts = set()  #Conjunto de hechos.

    #Método para agregar un nuevo hecho al conjunto de hechos.
    def add_fact(self, fact):
        self.facts.add(fact)
        self.update()  #Actualizamos el conjunto de hechos.

    #Método para actualizar el conjunto de hechos aplicando encadenamiento hacia adelante.
    def update(self):
        while True:
            new_facts = set()  #Conjunto para nuevos hechos deducidos.
            for rule in self.rules:
                #Verificamos si todas las condiciones de una regla están presentes en el conjunto de hechos.
                if all(cond in self.facts for cond in rule.condition) and rule.result not in self.facts:
                    new_facts.add(rule.result)  #Agregamos el resultado de la regla como nuevo hecho.
            if not new_facts:  #Si no hay nuevos hechos deducidos, salimos del bucle.
                break
            self.facts.update(new_facts)  #Agregamos nuevos hechos al conjunto de hechos.

#Definimos de la clase BackwardChaining.
class BackwardChaining:
    def __init__(self, rules):
        self.rules = rules  #Lista de reglas.

    #Método para verificar si un objetivo se puede alcanzar a partir de los hechos dados.
    def check_goal(self, goal, facts):
        if goal in facts:  #Si el objetivo ya está presente en los hechos, devolvemos True.
            return True
        for rule in self.rules:
            if rule.result == goal:
                #Verificamos si todas las condiciones de la regla se pueden alcanzar a partir de los hechos.
                if all(self.check_goal(cond, facts) for cond in rule.condition):
                    return True  #Si todas las condiciones se pueden alcanzar, devolvemos True.
        return False  #Si no se puede alcanzar el objetivo a partir de las reglas y hechos dados, devolvemos False.

#Definimos las reglas.
rules = [
    Rule(["tiene pelo", "da leche"], "es mamífero"),
    Rule(["tiene plumas", "vuela"], "es ave"),
    Rule(["es mamífero"], "es animal"),
    Rule(["es ave"], "es animal")
]

#Encadenamiento hacia adelante.
forward_chain = ForwardChaining(rules)
forward_chain.add_fact("tiene pelo")
forward_chain.add_fact("da leche")
print("Usando encadenamiento hacia adelante:")
print("Facts:", forward_chain.facts)

#Encadenamiento hacia atrás.
backward_chain = BackwardChaining(rules)
goal = "es animal"
print("\nUsando encadenamiento hacia atrás:")
print("¿El animal es un mamífero?:", backward_chain.check_goal(goal, forward_chain.facts))