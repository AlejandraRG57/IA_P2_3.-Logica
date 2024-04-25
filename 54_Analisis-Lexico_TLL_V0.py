#Alejandra Rodriguez Guevara 21310127 6E1

#El análisis léxico es la primera fase del proceso de compilación en la que se escanea el código fuente de un programa para identificar y 
#clasificar los distintos elementos léxicos que lo componen, también conocidos como tokens. 

import re

#Definición de tokens.
tokens = [
    ('NUMBER', r'\d*\.\d+|\d+'), #Números enteros y decimales.
    ('PLUS', r'\+'), #Operador de suma.
    ('MINUS', r'\-'), #Operador de resta.
    ('TIMES', r'\*'), #Operador de multiplicación.
    ('DIVIDE', r'\/'), #Operador de división.
    ('LPAREN', r'\('), #Paréntesis izquierdo.
    ('RPAREN', r'\)'), #Paréntesis derecho.
]

#Función para analizar el código fuente.
def lex(code):
    tokens_matched = []

    #Iteramos sobre cada token definido.
    for token_name, token_pattern in tokens:
        #Buscamos todas las coincidencias en el código.
        matches = re.findall(token_pattern, code)
        
        #Agregamos cada coincidencia al resultado.
        for match in matches:
            tokens_matched.append((token_name, match))
    
    return tokens_matched

code = '.14 + 42 - (7 * 2) / 3'

#Ejecutamos el análisis léxico.
tokens_found = lex(code)

#Imprimimos los tokens encontrados.
for token in tokens_found:
    print(token)