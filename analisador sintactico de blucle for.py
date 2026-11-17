# ============================================================
# ANALIZADOR SINTACTICO DEL BUCLE FOR EN PYTHON
# ============================================================

# 1. TABLA DE TOKENS

FOR = 10
ID = 20
IN = 30
COLON = 40
SIMPLE_STMT = 50
SUITE = 60
ELSE = 70
NEWLINE = 80

# 2. REGLAS DE PRODUCCION (segun el diagrama)
#
# start = for_stmt
# for_stmt = FOR target_list IN expression_list COLON bloque [ELSE COLON NEWLINE suite_else]
# target_list = ID
# expression_list = ID | NUMBER
# bloque = simple_stmt | suite
# suite_else = SUITE
#
# Los corchetes [ ] indican que el bloque else es opcional.
# La alternativa | significa que se puede elegir una opcion.

# 3. VECTOR DE PRUEBA
# Representa:
# for elemento in lista:
#     instruccion
# else:
#     instrucciones_alternativas

vector = [FOR, ID, IN, ID, COLON, SUITE, ELSE, COLON, NEWLINE, SUITE]


#  ANALIZADOR SINTACTICO

def start(tokens):
    i = 0
    i, error = for_stmt(tokens, i)

    if error != '':
        return error

    if i < len(tokens):
        return "Error sintactico: token inesperado " + str(tokens[i]) + " en posicion " + str(i)

    return "VALIDO"



def for_stmt(tokens, i):


    if i < len(tokens) and tokens[i] == FOR:
        i = i + 1
    else:
        return i, "Se esperaba la palabra FOR"

 
    i, error = target_list(tokens, i)
    if error != '':
        return i, error

  
    if i < len(tokens) and tokens[i] == IN:
        i = i + 1
    else:
        return i, "Se esperaba IN"

    
    i, error = expression_list(tokens, i)
    if error != '':
        return i, error

  
    if i < len(tokens) and tokens[i] == COLON:
        i = i + 1
    else:
        return i, "Se esperaba ':' despues de expression_list"

   
    i, error = bloque(tokens, i)
    if error != '':
        return i, error

    if i < len(tokens) and tokens[i] == ELSE:
        i = i + 1

        if i < len(tokens) and tokens[i] == COLON:
            i = i + 1
        else:
            return i, "Se esperaba ':' despues de ELSE"

        if i < len(tokens) and tokens[i] == NEWLINE:
            i = i + 1
        else:
            return i, "Se esperaba NEWLINE despues de ELSE:"

        i, error = suite_else(tokens, i)
        if error != '':
            return i, error

    return i, ''



def target_list(tokens, i):
    if i < len(tokens) and tokens[i] == ID:
        i = i + 1
        return i, ''

    return i, "Se esperaba un identificador en target_list"


def expression_list(tokens, i):
    if i < len(tokens) and (tokens[i] == ID or tokens[i] == 100):
        i = i + 1
        return i, ''

    return i, "Se esperaba una expresion en expression_list"


def bloque(tokens, i):
    if i < len(tokens) and tokens[i] == SIMPLE_STMT:
        i = i + 1
        return i, ''

    elif i < len(tokens) and tokens[i] == SUITE:
        i = i + 1
        return i, ''

    return i, "Se esperaba simple_stmt o suite"



def suite_else(tokens, i):
    if i < len(tokens) and tokens[i] == SUITE:
        i = i + 1
        return i, ''

    return i, "Se esperaba suite despues de ELSE:"


# PRUEBA DEL ANALIZADOR
print("TOKENS:", vector)
print("RESULTADO DEL ANALISIS DEL FOR:")
print(start(vector))