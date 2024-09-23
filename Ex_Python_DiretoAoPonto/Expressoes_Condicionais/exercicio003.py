# Ex.003 - Calculadora simples:
# Crie um programa que peça ao usuario dois numeros e uma operação (soma, subtração, multipliicação, divisão) e exiba o resultado:

numero01 = float(input('Digite aqui um número: '))
numero02 = float(input('Digite aqui um outro número: '))

print('\nEscolha abaixo uma operação matématica para ser feita com os dois numeros digitados: ')
print('Digite [+] para Somar, [-] para Subtrair, [*] para Multiplicar e [/] para Dividir.')

operacao = input('Digite aqui a sua opção de operação: ').strip()[0]

if operacao == '+':
    resultado = numero01 + numero02
elif operacao == '-':
    resultado = numero01 - numero02
elif operacao == '*':
    resultado = numero01 * numero02
elif operacao == '/':
    resultado = numero01 / numero02

print(f'\nO resultado da operção matématica desejada foi {resultado}.')
