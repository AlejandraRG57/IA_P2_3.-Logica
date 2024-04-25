#Alejandra Rodriguez Guevara 21310127 6E1

#El análisis sintáctico es la segunda fase del proceso de compilación, que sigue al análisis léxico. Su objetivo principal es analizar la estructura 
#gramatical del código fuente para determinar si cumple con las reglas sintácticas del lenguaje de programación en cuestión. 

#Importamos las bibliotecas necesarias.
import ply.lex as lex #Importamos el módulo para el análisis léxico.
import codecs #Importamos el módulo para la manipulación de archivos.
import os #Importamos el módulo para funciones relacionadas con el sistema operativo.

#Definimos las palabras reservadas y los tokens.
reservadas = ['BEGIN', 'END', 'IF', 'THEN', 'WHILE', 'DO', 'CALL', 'CONST',
              'VAR', 'PROCEDURE', 'OUT', 'IN', 'ELSE']
tokens = reservadas + ['ID', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
                       'ODD', 'ASSIGN', 'NE', 'LT', 'LTE', 'GT', 'GTE',
                       'LPARENT', 'RPARENT', 'COMMA', 'SEMMICOLOM',
                       'DOT', 'UPDATE']

#Definimos la regla para ignorar espacios y tabulaciones.
t_ignore = '\t '

#Definimos las expresiones regulares para los tokens.
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_ODD = r'ODD'
t_ASSIGN = r'='
t_NE = r'<>'
t_LT = r'<'
t_LTE = r'<='
t_GT = r'>'
t_GTE = r'>='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_COMMA = r','
t_SEMMICOLOM = r';'
t_DOT = r'\.'
t_UPDATE = r':='

#Definimos la regla para tokens de identificadores.
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    #Verificamos si el identificador es una palabra reservada.
    if t.value.upper() in reservadas:
        t.value = t.value.upper()  #Convertimos a mayúsculas.
        t.type = t.value  #Establecemos el tipo de token como la palabra reservada.
    return t

#Definimos la regla para tokens de nueva línea.
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)  #Actualizamos el número de línea.

#Definimos la regla para tokens de comentario.
def t_COMMENT(t):
    r'\#.*'
    pass  #Ignoramos los comentarios.

#Definimos la regla para tokens de números.
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)  #Convertimos a enter
    return t

#Definimos la regla para manejar errores léxicos.
def t_error(t):
    print("caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1)  #Saltamos el caracter ilegal.

#Función para buscar archivos en un directorio dado.
def buscarFicheros(directorio):
    ficheros = []
    numArchivo = ''
    respuesta = False
    cont = 1

    #Recorremos los archivos en el directorio.
    for base, dirs, files in os.walk(directorio):
        ficheros.append(files)

    #Mostramos la lista de archivos y solicitar la selección.
    for file in files:
        print(str(cont) + ". " + file)
        cont = cont + 1

    #Solicitamos al usuario que seleccione un archivo.
    while respuesta == False:
        numArchivo = input('\nNumero del test: ')
        for file in files:
            if file == files[int(numArchivo) - 1]:
                respuesta = True
                break

    print("Has escogido \"%s\" \n" % files[int(numArchivo) - 1])

    return files[int(numArchivo) - 1]

#Directorio donde se encuentran los archivos.
directorio = 'C:/Users/mahom_frrxtxx/OneDrive/Documentos/2. Sexto Semestre/Inteligencia Artificial/3. Lógica'

#Buscamos y seleccionamos un archivo en el directorio.
archivo = buscarFicheros(directorio)

#Ruta completa del archivo seleccionado.
test = directorio + archivo

#Abrimos y leemos el archivo.
fp = codecs.open(test, "r", "utf-8")
cadena = fp.read()
fp.close()

#Creamos un analizador léxico.
analizador = lex.lex()

#Establecemos la entrada del analizador como la cadena leída del archivo.
analizador.input(cadena)

#Procesamos los tokens en la entrada del analizador.
while True:
    tok = analizador.token()
    if not tok:
        break
    print(tok)  #Imprimimos los tokens.