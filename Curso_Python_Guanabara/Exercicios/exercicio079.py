# Ex.079- Crie um programa onde o usuario possa digitar varios valores numericos e cadastre-os em uma lista.
# Caso o numero ja exista la dentro, ele não sera adicionado.
# No final, serão exibidos todos os valores unicos digitados, em ordem crescente:

valores = []

while True:
    numeros = int(input('Digite aqui um valor: '))

    if numeros in valores:
        print('Este valor ja existe dentro da lista. Digite outro valor.')
    else:
        valores.append(numeros)

    opcao = input('Para continuar digite [s] e para parar digite [n]: ').strip().lower()
    if opcao == 'n':
        break

valores.sort()
print(f'\nValores cadastrados na lista em ordem crescente: {valores}.')
    