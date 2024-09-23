# Escreva um programa que verifique se um numero inserido pelo usuario é par ou ímpar:

def par_ou_impar(numero):
    if numero % 2 == 0:
        return 'Esse número é Par.'
    else:
        return 'Esse número é Ímpar.'
    

numero = int(input('Digite aqui um número inteiro e descubra se ele é Par ou Ímpar: '))
print(par_ou_impar(numero))