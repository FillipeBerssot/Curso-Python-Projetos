# Ex.086- Crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta:

matriz = []

for i in range(0,3):
    linha = []
    for v in range(0,3):
        numero = int(input(f'Digite um valor para a posicao {[i], [v]}: '))
        linha.append(numero)
    matriz.append(linha)

print('\nMatriz 3x3 formatada: ')
for linha in matriz:
    for numero in linha:
        print(f'[{numero:^3}]', end='')
    print()