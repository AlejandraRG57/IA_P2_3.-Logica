#Alejandra Rodriguez Guevara 21310127 6E1

#La Jerarquía de Chomsky es útil para comprender las propiedades de los lenguajes formales y las gramáticas utilizadas en el tratamiento lógico del lenguaje, 
#así como para clasificar la complejidad de los problemas relacionados con la generación y el reconocimiento de lenguajes.

class Grammar:
    def __init__(self, rules):
        self.rules = rules  #Inicializamos las reglas de la gramática.

    def generate(self, start_symbol, max_length):
        if max_length == 0:
            return []  #Si la longitud máxima es cero, no se generan cadenas.

        productions = self.rules.get(start_symbol, [])  #Obtenemos las producciones para el símbolo inicial.
        if not productions:
            return [start_symbol]  #Si no hay producciones, devolvemos el símbolo inicial como cadena.

        generated_strings = []  #Lista para almacenar las cadenas generadas.
        for production in productions:
            generated_string = []  #Lista para almacenar la cadena generada por cada producción.
            for symbol in production:
                if isinstance(symbol, str):
                    generated_string.append(symbol)  #Si el símbolo es una cadena, lo agregamos a la cadena generada.
                else:
                    #Si el símbolo es un no terminal, generamos las cadenas correspondientes recursivamente.
                    generated_string.extend(self.generate(symbol, max_length - 1))
            generated_strings.append(''.join(generated_string))  #Unimos los caracteres generados para formar una cadena.
        return generated_strings  #Devolvemos todas las cadenas generadas.

#Reglas de la gramática regular.
regular_grammar_rules = {
    'S': ['aA', 'bB'],
    'A': ['aA', 'bB', ''],
    'B': ['bB', '']
}

#Reglas de la gramática libre de contexto.
context_free_grammar_rules = {
    'S': ['AB'],
    'A': ['aA', ''],
    'B': ['bB', '']
}

#Reglas de la gramática sensible al contexto.
context_sensitive_grammar_rules = {
    'S': ['AB'],
    'AB': ['AaB']
}

#Reglas de la gramática irrestricta.
unrestricted_grammar_rules = {
    'S': ['AB', 'a']
}

#Creamos instancias de gramáticas con las respectivas reglas.
regular_grammar = Grammar(regular_grammar_rules)
context_free_grammar = Grammar(context_free_grammar_rules)
context_sensitive_grammar = Grammar(context_sensitive_grammar_rules)
unrestricted_grammar = Grammar(unrestricted_grammar_rules)

#Generamos cadenas utilizando las diferentes gramáticas y mostramos los resultados.
print("Gramática Regular:")
print(regular_grammar.generate('S', 5))

print("\nGramática Libre de Contexto:")
print(context_free_grammar.generate('S', 5))

print("\nGramática Sensible al Contexto:")
print(context_sensitive_grammar.generate('S', 5))

print("\nGramática Irrestricta:")
print(unrestricted_grammar.generate('S', 5))