# Ex.068- Faça um programa que jogue par ou impar com o computador. O jogo so sera interrompido quando o jogador PERDER,
# mostrando o total de vitorias consecutivas que ele consquistou no final do jogo:

import random

print('=============== JOGO ===============')
print('===============  DO ================')
print('=========== PAR OU IMPAR ===========')
print('\nEscolha PAR ou IMPAR e veja se voçê pode ganhar do computador:')

contador_vitorias = 0

while True:
    opcao = input('Escolha PAR ou IMPAR: ').strip().upper()
    numero_jogador = int(input('\nDigite aqui um numero:  '))
    numero_computador = random.randint(0, 100)

    soma = numero_jogador + numero_computador
    print('==============================================================================================')
    print(f'VOÇÊ escolheu o numero {numero_jogador} e o COMPUTADOR escolheu o numero {numero_computador}.')
    print(f'\nO NUMERO SORTEADO FOI {soma}, ', end='')

    if soma % 2 == 0:
        resultado = 'PAR'
        print('DEU PAR!')
    else:
        resultado = 'IMPAR'
        print('DEU IMPAR!')

    if resultado == opcao:
        print('VOÇÊ VENCEU')
        print('==========================================================================================')
        print('Vamos jogar novamente...')
        print('==========================================================================================')
        contador_vitorias += 1
    else:
        print('VOÇÊ PERDEU.')
        print(f'\nFinalizando o programa.\nVoçê ganhou {contador_vitorias}x consecutivas.\nObrigado por Jogar.')
        break
    
