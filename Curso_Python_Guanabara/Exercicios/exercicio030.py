# Desafio 030- Crie um programa que leia um numero inteiro e mostre na tela se ele e PAR ou IMPAR:

numero = int(input('Digite aqui um número aleátorio e descubra se ele é PAR ou ÍMPAR: '))

if numero % 2 == 0:
    print(f'O número digitado {numero} é um número PAR.')
else:
    print(f'O número digitado {numero} é ÍMPAR.')