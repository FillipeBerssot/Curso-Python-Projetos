# Ex. 09- Faça um programa que leia 5 números e informe a soma e a média dos números.

numero1 = float(input('Digite aqui um numero: '))
numero2 = float(input('Digite aqui um numero: '))
numero3 = float(input('Digite aqui um numero: '))
numero4 = float(input('Digite aqui um numero: '))
numero5 = float(input('Digite aqui um numero: '))

soma = numero1 + numero2 + numero3 + numero4 + numero5
media = (numero1 + numero2 + numero3 + numero4 + numero5) / 5

print(f'A soma dos numero digitados é {soma}')
print(f'A média dos numeros digitados é {media}')

