# Desafio 038- Escreva um programa que leia dois numeros inteiros e compare-os mostrando na tela uma mensagem:
# - O primeiro valor é maior:
# - O segundo valor é maior:
# - Não existe valor maior, os dois são iguais:

numero01 = int(input('Digite aqui um numero: '))
numero02 = int(input('Digite agora outro numero: '))
print('==============================================================================')
print(f'O primeiro numero digitado é {numero01}.')
print(f'O segundo numero digitado é {numero02}.')

if numero01 > numero02:
    print('O primeiro numero digitado é MAIOR do que o segundo numero digitado.')
elif numero02 > numero01:
    print('O segundo numero digitado é MAIOR do que o segundo numero digitado')
else:
    print('Não existe valor MAIOR os dois numeros são IGUAIS.')

print('==============================================================================')
