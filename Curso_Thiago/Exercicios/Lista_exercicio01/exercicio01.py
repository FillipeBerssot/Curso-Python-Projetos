# Ex. 01- Faça um programa que peça uma nota, entre zero e dez. 
# Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido:
# Solução: Validação de dados em Python

nota = float(input('Digite aqui uma nota entre 0 e 10: '))

while nota < 0 or nota > 10:
    print('Valor Inválido, por favor digite um valor entre 0 e 10.')
    nota = float(input('Digite aqui uma nota entre 0 e 10: '))

else:
    print(f'Valor digitado igual a {nota}. Valor Válido.')

