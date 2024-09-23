# Ex.058- Melhore o jogo do DESAFIO 028 onde o computador vai 'pensar' em um numero entre 0 e 10. 
# So que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessarios para vencer:

from random import randint

computador = randint(0, 10)
print('Sou o seu computador...   Acabei de pensar em um numero entre 0 e 10.')
print('Será que voçê consegue adivinhar qual foi?')
acertou = False
tentativas = 0

while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    tentativas += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... Tente novamente.')
        elif jogador > computador:
            print('Menos... Tente novamente.')
print(f'Acertou com {tentativas} tentativas. Parabens!')
