# Ex. 081- Crie um programa que vai ler varios numeros e colocar em lista. Depois disso mostre:
# A) Quantos numeros foram digitados: FEITO
# B) A lista de valores ordenada de forma decrescente: FEITO
# C) Se o valor 5 foi digitado e esta ou não na lista: FEITO

lista_numeros = []

while True:
    lista_numeros.append(int(input('Digite aqui um valor: ')))
    print('Numero adicionado a lista.')
    while True:
        opcao = input('Digite [s] para continuar e [n] para parar o programa: ').strip().lower()

        if opcao == 'n':
            print('Programa encerrado.')
            break
        elif opcao == 's':
            break
        else:
            print('Opçao Invalida. Digite [s / n]')
    if opcao == 'n':
        break

# A):
print(f'\nForam digitados {len(lista_numeros)} numeros na lista: {lista_numeros}.')

# B):
lista_numeros.sort(reverse=True)
print(f'A lista formatada de forma Decrescente fica: {lista_numeros}')

# C):
if 5 in lista_numeros:
    print(f'O numero 5 foi digitado na lista e esta na {lista_numeros.index(5) + 1}º posição')
else:
    print('O numero 5 não foi digitado na lista.')
