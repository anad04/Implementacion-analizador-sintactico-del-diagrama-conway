################################################################## ANALIZADOR SINTACTICO DE DEFINICION DE FUNCIONES

#################################################################

DEF = 10
FUNCTION_NAME = 20
LPAREN = 30
PARAMETER = 40
COMMA = 50
RPAREN = 60
COLON = 70
SIMPLE_STMT = 80
STATEMENT = 90
NEWLINE = 100


vector = [
    DEF, FUNCTION_NAME, LPAREN,
    PARAMETER, COMMA, PARAMETER,
    RPAREN, COLON, NEWLINE, STATEMENT
]


#ANALIZADOR SINTACTICO

def start(tokens):
    i = 0
    i, error = function_def(tokens, i)

    if error != '':
        return error

    if i < len(tokens):
        return "Error sintactico: token inesperado " + str(tokens[i]) + " en posicion " + str(i)

    return "VALIDO"



def function_def(tokens, i):

 
    if i < len(tokens) and tokens[i] == DEF:
        i = i + 1
    else:
        return i, "Se esperaba DEF"

  
    if i < len(tokens) and tokens[i] == FUNCTION_NAME:
        i = i + 1
    else:
        return i, "Se esperaba function_name"

   
    if i < len(tokens) and tokens[i] == LPAREN:
        i = i + 1
    else:
        return i, "Se esperaba '('"

  
    if i < len(tokens) and tokens[i] == PARAMETER:
        i, error = parameter_list(tokens, i)
        if error != '':
            return i, error

    
    if i < len(tokens) and tokens[i] == RPAREN:
        i = i + 1
    else:
        return i, "Se esperaba ')'"

    
    if i < len(tokens) and tokens[i] == COLON:
        i = i + 1
    else:
        return i, "Se esperaba ':' despues de los parentesis"

   
    i, error = cuerpo(tokens, i)
    if error != '':
        return i, error

    return i, ''



def parameter_list(tokens, i):

    
    if i < len(tokens) and tokens[i] == PARAMETER:
        i = i + 1
    else:
        return i, "Se esperaba parameter"

    
    while i < len(tokens) and tokens[i] == COMMA:
        i = i + 1

        if i < len(tokens) and tokens[i] == PARAMETER:
            i = i + 1
        else:
            return i, "Se esperaba parameter despues de la coma"

    return i, ''



def cuerpo(tokens, i):

   
    if i < len(tokens) and tokens[i] == SIMPLE_STMT:
        i = i + 1
        return i, ''

  
    elif i < len(tokens) and tokens[i] == NEWLINE:
        i = i + 1

        if i < len(tokens) and tokens[i] == STATEMENT:
            i = i + 1
        else:
            return i, "Se esperaba statement dentro del cuerpo"

        
        while i < len(tokens) and tokens[i] == STATEMENT:
            i = i + 1

        return i, ''

    elif i < len(tokens) and tokens[i] == STATEMENT:
        i = i + 1
        while i < len(tokens) and tokens[i] == STATEMENT:
            i = i + 1
        return i, ''

    return i, "Se esperaba simple_stmt o statement"


#  PRUEBA DEL ANALIZADOR
print("TOKENS:", vector)
print("RESULTADO DEL ANALISIS DE FUNCION:")
print(start(vector))