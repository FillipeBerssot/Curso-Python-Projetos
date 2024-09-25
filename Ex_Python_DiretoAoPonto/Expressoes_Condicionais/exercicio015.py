# Ex. 015 - Faça uma função validadora de input, para verificar se o input do ussuario é apenas numerico.
# Imprima uma mensagen de erro se nao for:

def validar_input_numero(input_usuario):
    try:
        float(input_usuario)
        return True
    except ValueError:
        return False
    

input_usuario = input('Digite um número: ')
if validar_input_numero(input_usuario):
    print('Input Válido.')
else:
    print('ERRO. Input não é númerico.')
