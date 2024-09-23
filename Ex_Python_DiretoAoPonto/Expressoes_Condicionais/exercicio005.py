# Ex.005 - Crie um programa que verifique se um numero inserido pelo usuario é primo ou não:

def numero_primo(numero):
    if numero < 2:
        return f'O número {numero} não é Primo.'
    for i in range (2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return f'O número {numero} não é Primo.'
    return f'O número {numero} é Primo.'

numero = int(input('Digite aqui um número é descubra se ele é Primo ou não: '))
print(numero_primo(numero))
