# FUNÇÕES:
#    def:

# Exemplo 01: Sem parâmetros:
def linha():
    print('=' * 30)


linha()
print('     CURSO EM VIDEO      ')
linha()
print('     APRENDA PYTHON      ')
linha()
print('     GUSTAVO GUANABARA       ')    
linha()

# Exemplo 02: Com parâmetros:
def titulo(txt):
    print('=' *30)
    print(txt)
    print('=' *30)


titulo('    CURSO EM VIDEO      ')
titulo('        PYTHON          ')
titulo('         OLÁ            ')

# Exemplo 03: FUNÇÃO PARA SOMAR:
def soma(a, b):
    s = a + b
    print(f'A soma é: {s}.')


soma(4,5)
soma(8, 9)
soma(2, 1)
linha()
''' a = 4
b = 5
s = a + b
print(s) '''

# Exemplo 04: DESEMPACOTAMENTO:
#          def contador(* numero):   serve para colocar quantos parametros dentro de (numero) que quiser.
def contador(* numero):
    for valor in numero:
        print(f'{valor} ',end='')
    print('FIM')


contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
linha()

# Exemplo 05:
def soma(*valores):
    s = 0
    for numeros in valores:
        s += numeros
    print(f'Somando os valores {valores} temos {s}')


soma(5, 2)
soma(2, 9, 4)
linha()

# Exemplo 06: 
def dobra(lista):
    posicao = 0
    while posicao < len(lista):
        lista[posicao] *= 2
        posicao += 1


valores = [6, 3, 9, 1, 0, 2]
print(valores)
dobra(valores)
print(f'Dobrando os valores fica: {valores}')
