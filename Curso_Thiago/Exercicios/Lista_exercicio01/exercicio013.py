# Ex. 013- Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
# O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
# Tabuada de 5:
# 5 X 1 = 5
# 5 X 2 = 10
# ...
# 5 X 10 = 50

'''numero = int(input("Digite aqui um numero inteiro aleatorio: "))

numero_tabuada1 = numero * 1
numero_tabuada2 = numero * 2
numero_tabuada3 = numero * 3
numero_tabuada4 = numero * 4
numero_tabuada5 = numero * 5
numero_tabuada6 = numero * 6
numero_tabuada7 = numero * 7
numero_tabuada8 = numero * 8
numero_tabuada9 = numero * 9
numero_tabuada10 = numero * 10

print(f"A tabuada do numero {numero} é: {numero} x 1 = {numero_tabuada1}")
print(f"A tabuada do numero {numero} é: {numero} x 2 = {numero_tabuada2}")
print(f"A tabuada do numero {numero} é: {numero} x 3 = {numero_tabuada3}")
print(f"A tabuada do numero {numero} é: {numero} x 4 = {numero_tabuada4}")
print(f"A tabuada do numero {numero} é: {numero} x 5 = {numero_tabuada5}")
print(f"A tabuada do numero {numero} é: {numero} x 6 = {numero_tabuada6}")
print(f"A tabuada do numero {numero} é: {numero} x 7 = {numero_tabuada7}")
print(f"A tabuada do numero {numero} é: {numero} x 8 = {numero_tabuada8}")
print(f"A tabuada do numero {numero} é: {numero} x 9 = {numero_tabuada9}")
print(f"A tabuada do numero {numero} é: {numero} x 10 = {numero_tabuada10}")'''

numero = int(input('Digite aqui um numero de 1 a 10: '))

while numero > 10:
    print('Invalido, digite um numero de 1 a 10:')
    numero = int(input('Digite aqui um numero de 1 a 10: '))

for multiplicacao in range(1, 11):
    resultado = numero * multiplicacao
    print(f'{numero} x {multiplicacao} = {resultado}')

