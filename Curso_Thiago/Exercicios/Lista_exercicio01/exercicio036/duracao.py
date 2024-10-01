def calcular_duracao_acelerada(tempo_em_segundos, velocidade):
    """
    Objetivo: Calcular a nova duração do vídeo com base na 
    velocidade escolhida pelo usuario.

    Calcula e converte para horas, minutos e segundos.

    Retorna divido em 3 partes (variaveis)
    """

    duracao_acelerada = tempo_em_segundos / velocidade

    horas = int(duracao_acelerada // 3600)
    minutos = int((duracao_acelerada % 3600) // 60)
    segundos = int(duracao_acelerada % 60)

    return horas, minutos, segundos
