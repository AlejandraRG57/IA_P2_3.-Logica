#Alejandra Rodriguez Guevara 21310127 6E1

#La Programación Lógica Inductiva (PLI) es un enfoque en el aprendizaje automático que combina la programación 
#lógica con técnicas inductivas para inducir reglas lógicas a partir de ejemplos.

class Rule:
    def __init__(self, antecedent, consequent, score):
        self.antecedent = antecedent #Antecedente de la regla.
        self.consequent = consequent #Consecuente de la regla.
        self.score = score #Puntaje de la regla.

def foil(examples_pos, examples_neg, attributes):
    rules = [] #Lista para almacenar las reglas generadas.

    #Iteramos sobre los valores objetivo únicos.
    for target_value in set(example["PlayTennis"] for example in examples_pos):
        #Ejemplos positivos cubiertos por el valor objetivo.
        pos_covered = [example for example in examples_pos if example["PlayTennis"] == target_value]
        #Ejemplos negativos cubiertos por el valor objetivo.
        neg_covered = [example for example in examples_neg if example["PlayTennis"] == target_value]

        #Iteramos sobre los atributos.
        for attribute in attributes:
            #Iteramos sobre los valores únicos del atributo.
            for value in set(example[attribute] for example in examples_pos):
                #Ejemplos positivos con el valor de atributo dado.
                pos_value = [example for example in pos_covered if example[attribute] == value]
                #Ejemplos negativos con el valor de atributo dado.
                neg_value = [example for example in neg_covered if example[attribute] == value]

                pos_count = len(pos_value)  # Contar ejemplos positivos
                neg_count = len(neg_value)  # Contar ejemplos negativos

                #Calculamos el puntaje de la regla si hay ejemplos positivos y negativos cubiertos.
                if pos_count > 0 and neg_count > 0:
                    score = pos_count / (pos_count + neg_count)
                    #Agregamos la regla a la lista de reglas.
                    rules.append(Rule(attribute + "=" + value, target_value, score))

    #Ordenamos las reglas por puntaje en orden descendente.
    rules.sort(key=lambda x: x.score, reverse=True)
    return rules

examples_pos = [
    {"Outlook": "Sunny", "Temperature": "Hot", "Humidity": "High", "Windy": "False", "PlayTennis": "Yes"},
    {"Outlook": "Sunny", "Temperature": "Hot", "Humidity": "High", "Windy": "True", "PlayTennis": "No"}
]

examples_neg = [
    {"Outlook": "Overcast", "Temperature": "Cool", "Humidity": "High", "Windy": "False", "PlayTennis": "Yes"}
]

attributes = ["Outlook", "Temperature", "Humidity", "Windy"]

rules = foil(examples_pos, examples_neg, attributes)

for rule in rules:
    print("IF", rule.antecedent, "THEN PlayTennis =", rule.consequent)