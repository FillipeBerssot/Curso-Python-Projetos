# Ex. 075- Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
# A) Quantas vezes apareceu o valor 9: FEITO
# B) Em que posição foi digitado o primeiro valor 3: FEITO
# C) Quais foram os numeros pares: FEITO

tupla_de_4_valores = (
    int(input('Digite aqui um valor: ')),
    int(input('Digite aqui outro valor: ')),
    int(input('Digite aqui outro valor: ')),
    int(input('Digite aqui outro valor: '))
)

# A):
contador = tupla_de_4_valores.count(9)
print(f'O numero 9 apareceu {contador} vezes na tupla.')

# B):
if 3 not in tupla_de_4_valores:
    print(f'O numero 3 não foi digitado em nenhuma posição dentro da tupla.')
else:
    print(f'O numero 3 ficou na {tupla_de_4_valores.index(3) + 1}º posição dentro da tupla.')

# C):
numeros_pares = []
for numeros in tupla_de_4_valores:
    if numeros % 2 == 0:
        numeros_pares.append(numeros)
if numeros_pares == 0:
    print('Não foram digitados nenhum numero Par.')
else:
    print(f'Foram digitados dentro da tupla os numeros pares: {numeros_pares}.')
        