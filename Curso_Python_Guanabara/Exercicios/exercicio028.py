# Desafio 028- Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0 e 5 e peça para o usuario tentar descobrir qual foi o numero 
# escolhido pelo computador o programa devera escrever na tela se o usuario venceu ou perdeu:

import random

numero_pc = random.randint(0,5)
# print(numero_pc)

print('------- DESCUBRA QUAL É O NÚMERO CORRETO -------')
numero_jogador = int(input('Digite aqui um número de 0 a 5 para tentar acertar o número correto: '))

if numero_jogador == numero_pc:
    print(f'Parabéns o número escolhido foi o {numero_pc} , voçê acertou!')
else:
    print(f'Errou, o número correto foi o {numero_pc} , tente novamente!')