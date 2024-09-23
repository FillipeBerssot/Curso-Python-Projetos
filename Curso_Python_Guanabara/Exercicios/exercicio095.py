# Ex.095- Aprimore o desafio 093 para que ele funcione com varios jogadores, incluindo um ssistema de visualização 
# de detalhes do aproveitamento de cada jogador:

# Maneira 01:
time = []
jogador = {}
partidas = []

while True:
    jogador.clear()
    jogador['Nome'] = input('Nome do jogador: ')
    tot = int(input(f'Quantas partidas {jogador['Nome']} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'     Quantos gols na partida {c+1}? ')))
    jogador['Gols'] = partidas[:]
    jogador['Total'] = sum(partidas)
    time.append(jogador.copy())

    while True:
        resposta = input('Quer continuar?[S/N]: ').upper()[0]
        if resposta in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resposta == 'N':
        break
print('-=' * 40)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15} ', end='')
print()
print('-=' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ' , end='')
    for d in v.values():
        print(f'{str(d):<15}' , end='')
    print()
print('-=' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca > len(time):
        print(f'ERRO! Não existe jogador com codigo {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}: ')
        for i, g in enumerate(time[busca]['Gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('-=' * 40)
print('<< VOLTE SEMPRE >>')

# Maneira 02:

lista_de_jogadores = []

while True:
    nome_jogador = input('Digite o nome do jogador e veja seu aproveitamento: ')
    partidas_jogadas = int(input('Quantas partidas ele jogou? '))
    gols_em_cada_partida = []

    for g in range(partidas_jogadas):
        gols_feitos = int(input(f'Quantos gols ele fez na {g+1}º partida? '))
        gols_em_cada_partida.append(gols_feitos)

    dados_do_jogador = {}
    dados_do_jogador['Nome'] = nome_jogador.capitalize()
    dados_do_jogador['Partidas Jogadas'] = partidas_jogadas
    dados_do_jogador['Gols em cada partida'] = gols_em_cada_partida
    dados_do_jogador['Gols Feitos ao total'] = sum(gols_em_cada_partida)

    lista_de_jogadores.append(dados_do_jogador)

    opcao = input('Deseja continuar?[S/N]: ').strip().upper()
    if opcao == 'N':
        print('Encerrando o programa.')
        break

print('-=' * 50)
for i, jogador in enumerate(lista_de_jogadores):
    print(f'{i+1}. Nome: {jogador['Nome']} - Total de Gols: {jogador['Gols Feitos ao total']}')

while True:
    opcao_detalhes = input('\nDeseja ver os detalhes de qual jogador? (Digite o numero correspondente ou [999] para sair): ').strip()
    if opcao_detalhes.isdigit():
        opcao_detalhes = int(opcao_detalhes)
        if opcao_detalhes == 999:
            print('Encerrando o Programa.')
            break
        elif 1 <= opcao_detalhes <= len(lista_de_jogadores):
            jogador_selecionado = lista_de_jogadores[opcao_detalhes - 1]
            print('-=' * 50)
            print(f"Detalhes do jogador {jogador_selecionado['Nome']}:")
            print(f"  Partidas Jogadas: {jogador_selecionado['Partidas Jogadas']}")
            for i, gols in enumerate(jogador_selecionado['Gols em cada partida'], 1):
                print(f'    => Na {i}º partida, fez {gols} gols')
            print(f'    Total de Gols no Campeonato: {jogador_selecionado['Gols Feitos ao total']}')
            print('-='*50)
        else:
            print('Numeros invalido. Tente novamente.')
    else:
        print('Entrada invalida. Digite um numero valido.')