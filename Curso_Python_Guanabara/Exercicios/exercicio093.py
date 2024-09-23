# Ex.093- Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
# quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado
# em um dicionario, incluindo o total de gols feitos durante o campeonato:

nome_jogador = input('Digite o nome do jogador e veja seu aproveitamento: ')
partidas_jogadas = int(input('Quantas partidas ele jogou? '))
gols_ao_total = []
gols_em_cada_partida = []

for g in range(partidas_jogadas):
    gols_feitos = int(input(f'Quantos gols ele fez na {g+1}º partida? '))
    gols_em_cada_partida.append(gols_feitos)
    gols_ao_total.append(gols_feitos)

print('-=' * 50)

dados_do_jogador = {}
dados_do_jogador['Nome'] = nome_jogador.capitalize()
dados_do_jogador['Partidas Jogadas'] = partidas_jogadas
dados_do_jogador['Gols em cada partida'] = gols_em_cada_partida
dados_do_jogador['Gols Feitos ao total'] = sum(gols_ao_total)

print(dados_do_jogador)

print('-=' * 50)
print(f'O jogador {nome_jogador.capitalize()} jogou {partidas_jogadas} partidas.')
for c,v in enumerate(dados_do_jogador['Gols em cada partida'], 1):
    print(f'    =>Na {c}º partida, fez {v} gols.')
print(f'Foi um total de {dados_do_jogador["Gols Feitos ao total"]} gols feitos durante o campeonato.')
print('-=' * 50)