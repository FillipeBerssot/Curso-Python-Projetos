# Ex.088- Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão gerados
# e vai sortear 6 numeros entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta:

import random
import time

print('-' * 45)
print(f'{'JOGO DA MEGA-SENA':^35}')
print('-' * 45)
quantidade_jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('\n-=-=-=-=-=' 'SORTEANDO JOGOS' '-=-=-=-=-=')

jogos = []

for _ in range(quantidade_jogos):
    jogo = random.sample(range(1,61), 6)
    jogo.sort()
    jogos.append(jogo)

for i, jogo in enumerate(jogos, 1):
    time.sleep(1)
    print(f'Jogo {i}: {jogo}')    
print('-=-=-=-=-=-= BOA SORTE -=-=-=-=-=-=')
