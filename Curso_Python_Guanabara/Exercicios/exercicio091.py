# Ex.091- Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatorios. Guarde esses resultados em um dicionario. No final,
# coloque esse dicionario em ordem, sabendo que o vencedor tirou o maior numero no dado:

import random
from time import sleep
from operator import itemgetter

jogo = {
    'Jogador01': random.randint(1,6),
    'Jogador02': random.randint(1,6),
    'Jogador03': random.randint(1,6),
    'Jogador04': random.randint(1,6)}

ranking = []

print('Resultados dos Jogadores: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('-=' * 20)
print('  == RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'    {i+1}º lugar {v[0]} com {v[1]}.')
    sleep(1)
print('-=' * 20)

