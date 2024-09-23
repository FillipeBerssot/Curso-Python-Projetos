# Ex.087- Aprimore o dessafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados:
# B) A soma dos valores da terceira coluna:
# C) O maior valor da segunda linha:

matriz = []
soma_pares = 0
soma_terceira_coluna = 0
maior_valor_segunda_linha = None

for i in range(0,3):
    linha = []
    for v in range(0,3):
        numero = int(input(f'Digite um valor para a posicao {[i], [v]}: '))
        linha.append(numero)        

        if numero % 2 == 0:
            soma_pares += numero
        if v == 2:
            soma_terceira_coluna += numero
        if i == 1:
            if maior_valor_segunda_linha is None or numero > maior_valor_segunda_linha:
                maior_valor_segunda_linha = numero
                
    matriz.append(linha)

print('\nMatriz 3x3 formatada: ')
for linha in matriz:
    for numero in linha:
        print(f'[{numero:^3}]', end='')
    print()

print(f'\nA soma de todos os valores parees digitados: {soma_pares}')
print(f'A soma dos valores da terceira coluna: {soma_terceira_coluna}')
print(f'O maior valor da segunda lista: {maior_valor_segunda_linha}')