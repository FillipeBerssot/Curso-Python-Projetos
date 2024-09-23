# Ex.008 - Jogo de Pedra-Papel-Tesoura: Crie um jogo para jogar contra o computador de Pedra-Papel-Tesoura usando
# instruções condicionais e loops. Permita que o usuario escolha sua jogada e determine o vencedor com base na logica do jogo.
# Implemente um sistema de pontuação para acompanhar as vitorias e derrotas de cada jogador:

def Pedra_Papel_Tesoura():
    from random import choice

    print('=============== Pedra Papel Tesoura ===============')
    print('Vamos jogar!')
    print('===================================================')

    vitorias = 0
    derrotas = 0
    empates = 0

    while True:
        opcoes = ['Pedra' , 'Papel', 'Tesoura']
        escolha_do_computador = choice(opcoes)

        escolha_do_usuario = input('Escolha entre Pedra, Papel ou Tesoura: ').strip().capitalize()

        if escolha_do_usuario not in opcoes:
            print('\nEscolha inválida. Tente Novamente.')
            continue

        if escolha_do_usuario == escolha_do_computador:
            print(f'\nVoçê escolheu {escolha_do_usuario} e eu escolhi {escolha_do_computador}.')
            print('EMPATAMOS.')
            empates += 1
                
        elif escolha_do_usuario == 'Pedra' and escolha_do_computador == 'Tesoura':
            print(f'\nVoçê escolheu {escolha_do_usuario} e eu escolhi {escolha_do_computador}.')
            print('Pedra ganha de Tesoura. VOÇÊ GANHOU!')
            vitorias += 1
                
        elif escolha_do_usuario == 'Pedra' and escolha_do_computador == 'Papel':
            print(f'\nVoçê escolheu {escolha_do_usuario} e eu escolhi {escolha_do_computador}.')
            print('Papel ganha de Pedra. VOÇÊ PERDEU!')
            derrotas += 1

        elif escolha_do_usuario == 'Papel' and escolha_do_computador == 'Pedra':
            print(f'\nVoçê escolheu {escolha_do_usuario} e eu escolhi {escolha_do_computador}.')
            print('Papel ganha de pedra. VOÇÊ GANHOU!')
            vitorias += 1

        elif escolha_do_usuario == 'Papel' and escolha_do_computador == 'Tesoura':
            print(f'\nVoçê escolheu {escolha_do_usuario} e eu escolhi {escolha_do_computador}.')
            print('Tesoura ganha de Papel. VOÇÊ PERDEU!')
            derrotas += 1

        elif escolha_do_usuario == 'Tesoura' and escolha_do_computador == 'Pedra':
            print(f'\nVoçê escolheu {escolha_do_usuario} e eu escolhi {escolha_do_computador}.')
            print('Pedra ganha de Tesoura. VOÇÊ PERDEU!')
            derrotas += 1

        elif escolha_do_usuario == 'Tesoura' and escolha_do_computador == 'Papel':
            print(f'\nVoçê escolheu {escolha_do_usuario} e eu escolhi {escolha_do_computador}.')
            print('Tesoura ganha de Papel. VOÇÊ GANHOU!')
            vitorias += 1

        jogar_novamente = input('\nDeseja jogar novamente [s/n]: ').strip().lower()[0]
        
        if jogar_novamente == 'n':
            print('\nEncerrando os Jogos. Abaixo está os dados:')
            print(f'\nVoçê GANHOU {vitorias} vez(s) de mim.')
            print(f'Voçê PERDEU {derrotas} vez(s) para mim.')
            print(f'Nós EMPATAMOS {empates} vez(s).')
            break


Pedra_Papel_Tesoura()