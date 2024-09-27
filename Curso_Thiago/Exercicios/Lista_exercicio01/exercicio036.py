# Ex.036- Faça um programa que:
# O usuário vai fornecer o tempo de vídeo do YouTube e a velocidade
# que irá assistir (1,25 / 1,5 / 2,0).
# O programa deve falar qual será a durabilidade do vídeo para cada tempo de
# aceleração:
# Exemplo: se um vídeo dura 1h, na velocidade 2 ele irá durar 30 min.

numero_partes_tempo = 3
limite_minutos_segundos = 59


def calcular_duracao_acelerada(tempo_em_segundos, velocidade):
    duracao_acelerada = tempo_em_segundos / velocidade

    horas = int(duracao_acelerada // 3600)
    minutos = int((duracao_acelerada % 3600) // 60)
    segundos = int(duracao_acelerada % 60)

    return horas, minutos, segundos


def validar_tempo(tempo):
    partes = tempo.split(':')

    if len(partes) != numero_partes_tempo:
        print('Erro: O formato deve ser HH:MM:SS.')
        return False

    if (not partes[0].isdigit() or not partes[1].isdigit() or
        not partes[2].isdigit()):
        print('Erro: Horas, minutos e segundos devem ser números inteiros.')
        return False

    horas, minutos, segundos = map(int, partes)

    if horas < 0:
        print('Erro: As horas devem ser maiores ou iguais a 0')
        return False

    if not (0 <= minutos <= limite_minutos_segundos):
        print(f'Erro: Minutos devem estar entre 0 e '
              f'{limite_minutos_segundos}.')
        return False
    if not (0 <= segundos <= limite_minutos_segundos):
        print(f'Erro: Segundos devem estar entre 0 e '
              f'{limite_minutos_segundos}.')
        return False
    return True


def obter_tempo_em_segundos(tempo):
    horas, minutos, segundos = map(int, tempo.split(':'))
    return horas * 3600 + minutos * 60 + segundos


def obter_velocidade_do_usuario():
    opcoes_velocidade = """
Escolha a velocidade de reprodução:
[1] - 0.25x
[2] - 0.5x
[3] - 0.75x
[4] - 1.25x
[5] - 1.5x
[6] - 1.75x
[7] - 2.0x
"""
    print(opcoes_velocidade)

    velocidades = {
        '1': 0.25,
        '2': 0.5,
        '3': 0.75,
        '4': 1.25,
        '5': 1.5,
        '6': 1.75,
        '7': 2.0,
    }

    opcao_velocidade = input('Digite sua escolha: ').strip()
    while opcao_velocidade not in velocidades:
        print('Opção inválida. Escolha uma opção válida entre 1 e 7.')
        opcao_velocidade = input('Digite sua escolha: ').strip()

    return velocidades[opcao_velocidade]


tempo = input('Digite o tempo do vídeo no formato HH:MM:SS: ')

while not validar_tempo(tempo):
    tempo = input('Digite o tempo de vídeo no formato HH:MM:SS: ')

velocidade = obter_velocidade_do_usuario()

tempo_em_segundos = obter_tempo_em_segundos(tempo)

horas, minutos, segundos = calcular_duracao_acelerada(
    tempo_em_segundos, velocidade
)

print(
    f'\nNa velocidade {velocidade}x, a duração do vídeo será de '
    f'aproximadamente {horas} horas, {minutos} minutos e {segundos} segundos.'
)
