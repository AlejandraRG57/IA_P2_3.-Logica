#Alejandra Rodriguez Guevara 21310127 6E1

#El análisis semántico es la tercera fase del proceso de compilación, que sigue al análisis léxico y al análisis sintáctico. Su objetivo principal es verificar 
#que el código fuente cumpla con las reglas semánticas del lenguaje de programación y detectar errores semánticos que no pueden ser capturados por el análisis léxico y sintáctico. 

#Definición de tokens.
tokens = [
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
]

#Expresiones regulares para cada token.
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

#Expresión regular para números.
def t_NUMBER(t):
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t

#Ignoramos espacios en blanco y tabulaciones.
t_ignore = ' \t'

#Manejo de errores.
def t_error(t):
    print("Carácter ilegal:", t.value[0])
    t.lexer.skip(1)

#Importación del analizador léxico de Ply.
import ply.lex as lex
lexer = lex.lex()

#Definición de la gramática y reglas de precedencia.
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
)

#Reglas de la gramática.
def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_divide(p):
    'term : term DIVIDE factor'
    if p[3] != 0:
        p[0] = p[1] / p[3]
    else:
        print("Error: División por cero")
        p[0] = None

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_number(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_expression(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_error(p):
    print("Error de sintaxis en la entrada")

#Importación del analizador sintáctico de Ply.
import ply.yacc as yacc
parser = yacc.yacc()

#Función para realizar el análisis semántico.
def semantic_analysis(data):
    result = parser.parse(data)
    return result

expression = "3 + (4 * 2)"
result = semantic_analysis(expression)
print("Resultado:", result)