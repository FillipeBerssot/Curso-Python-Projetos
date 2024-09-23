# Ex. 08- Faça um programa que leia 5 números e informe o maior número:
# Fazer sem utilizar a função MAX:

'''numero1 = float(input('Digite aqui um numero: '))
numero2 = float(input('Digite aqui um numero: '))
numero3 = float(input('Digite aqui um numero: '))
numero4 = float(input('Digite aqui um numero: '))
numero5 = float(input('Digite aqui um numero: '))

lista = [numero1, numero2, numero3, numero4, numero5]

print(f'Aqui está os numeros digitados: {lista}')
print(f'O Maior numero digitado foi o {max(lista)}')'''


i = 1
lista_numerica = []
while i <= 5:
    numero = float(input(f'Digite o {i}° numero: '))
    lista_numerica.append(numero)
    i += 1
print(f'O maior numero é: {max(lista_numerica)}')