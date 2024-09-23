# Ex.007 - Jogo da adivinhação: Escreva um programa que gere um numero aleatorio entre 1 e 100 e desafie o usuario a adivinha-lo.
# O programa deve fornecer dicas ao usuario, informando se o seu palpite esta acima, abaixo ou igual ao numero secreto. O jogo termina
# quando o usuario acerta o numero ou atinge um limite máximo de tentativas:

def jogo_da_adivinhacao():
    from time import sleep
    from random import randint
    print('=============== Jogo da Adivinhação ===============')
    print('Tente Descobrir qual o número que estou pensando!')
    print('Voçê tem 10 tentativas para acertar o meu número!')
    print('===================================================')

    numero_pc = randint(1, 100)
    tentativas = 0
    limite_tentativas = 10

    while tentativas < limite_tentativas:
        numero_usuario = int(input('\nDigite um número inteiro entre 1 e 100 para tentar adivinhar: '))
        tentativas += 1

        if numero_usuario > numero_pc:
            print('Analisando o seu número ...')
            sleep(1)
            print('\nO número que voçê digitou é maior que o número que eu pensei. Tente Novamente.')
        elif numero_usuario < numero_pc:
            print('Analisando o seu número ...')
            sleep(0.5)
            print('\nO número que voçê digitou é menor que o número que eu pensei. Tente Novamente.')
        else:  
            print('Analisando o seu número ...')
            sleep(0.5)
            print(f'\nVoçê ACERTOU! PARABÉNS!!! O número que eu pensei era {numero_pc}')
            return
        
        print(f'Tentativas restantes: {limite_tentativas - tentativas}')
    
    if tentativas == limite_tentativas:
        print(f'\nVoçê atingiu o limite maximo de tentativas. O número era {numero_pc}')

jogo_da_adivinhacao()