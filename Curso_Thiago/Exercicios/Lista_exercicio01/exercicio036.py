# Ex.036- Faça um programa que:
# O usuário vai fornecer o tempo de vídeo do YouTube e a velocidade
# que irá assistir (1,25 / 1,5 / 2,0).
# O programa deve falar qual será a durabilidade do vídeo para cada tempo de
# aceleração:
# Exemplo: se um vídeo dura 1h, na velocidade 2 ele irá durar 30 min.

def duracao_do_video_acelerado(tempo_do_video, opcao_de_velocidade_do_video):
    partes = tempo_do_video.split(':')
    horas = int(partes[0])
    minutos = int(partes[1])
    tempo_em_minutos = horas * 60 + minutos

    velocidades = {
        '1': 0.25,
        '2': 0.5,
        '3': 0.75,
        '4': 1.25,
        '5': 1.5,
        '6': 1.75,
        '7': 2.0,
    }

    velocidade = velocidades[opcao_de_velocidade_do_video]
    duracao_do_video_acelerado = tempo_em_minutos / velocidade

    horas_aceleradas = int(duracao_do_video_acelerado // 60)
    minutos_acelerados = int(duracao_do_video_acelerado % 60)

    print(
        f'\nNa velocidade {velocidade}x. A duração do vídeo será de '
        f'aproximadamente {horas_aceleradas} horas '
        f'e {minutos_acelerados} minutos.'
    )


tempo_do_video = input(
    'Digite aqui o tempo de video do youtube que voçê irá assitir (HH:MM): '
)

opcoes = """
Escolha a velocidade do vídeo:
[1] para velocidade 0.25
[2] para velocidade 0.5
[3] para velocidade 0.75
[4] para velocidade 1.25
[5] para velocidade 1.5
[6] para velocidade 1.75
[7] para velocidade 2.0
"""

opcao_de_velocidade_do_video = ''
while opcao_de_velocidade_do_video not in {'1', '2', '3', '4', '5', '6', '7'}:
    print(opcoes)
    opcao_de_velocidade_do_video = input(
        'Digite aqui sua opcão de velocidade de acordo com as opções acima: '
    ).strip()

    if opcao_de_velocidade_do_video not in {'1', '2', '3', '4', '5', '6', '7'}:
        print('Opção inválida. Por favor, escolha uma opção entre 1 e 7.')

duracao_do_video_acelerado(tempo_do_video, opcao_de_velocidade_do_video)
