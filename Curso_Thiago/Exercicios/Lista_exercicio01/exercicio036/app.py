from tempo import validar_tempo, obter_tempo_em_segundos
from velocidade import obter_velocidade_do_usuario
from duracao import calcular_duracao_acelerada

def app():
    """
    Objetivo: Entrada principal do programa, realiza as chamadas
    com o usuario e as funções dos outros modulos para fazer os 
    calculos e exibir o resultado ajustado para o usuario.
    
    """

    tempo = input('Digite o tempo do vídeo no formato HH:MM:SS (ex: 01:45:30): ')

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

if __name__ == "__main__":
    app()
