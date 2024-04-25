#Alejandra Rodriguez Guevara 21310127 6E1

#La inducción gramatical es un proceso mediante el cual se intenta inferir una gramática formal a partir de un conjunto de ejemplos o datos observados. 

class GrammarInduction:
    def __init__(self, examples):
        self.examples = examples #Almacenamos los ejemplos de texto proporcionados.
        self.grammar = None #Inicializamos la gramática como nula al principio.
    
    def induce_grammar(self):
        #Definimos una gramática de ejemplo de forma manual. 
        self.grammar = {
            'S': ['NP VP', 'S CONJ S'], #Reglas para la categoría sintáctica S.
            'NP': ['Det N', 'N'], #Reglas para la categoría sintáctica NP.
            'VP': ['V NP'], #Reglas para la categoría sintáctica VP.
            'Det': ['el', 'un'], #Reglas para determinantes.
            'N': ['gato', 'perro'], #Reglas para nombres.
            'V': ['persigue', 'adora'], #Reglas para verbos.
            'CONJ': ['y', 'o'] #Reglas para conjunciones.
        }
    
    def print_grammar(self):
        if self.grammar:
            print("Gramática inferida:")
            #Imprimimos las reglas de producción de la gramática inferida.
            for non_terminal, productions in self.grammar.items():
                print(f"{non_terminal} -> {' | '.join(productions)}")
        else:
            print("Primero necesitas inducir la gramática.") #Mensaje si la gramática no ha sido inducida aún.

examples = [
    "el gato persigue al perro",
    "el perro adora al gato",
    "el gato persigue al perro y el perro adora al gato"
]

#Creamos una instancia de la clase GrammarInduction con los ejemplos proporcionados.
grammar_induction = GrammarInduction(examples)
#Inducimos la gramática a partir de los ejemplos.
grammar_induction.induce_grammar()
#Imprimimos la gramática inferida.
grammar_induction.print_grammar()