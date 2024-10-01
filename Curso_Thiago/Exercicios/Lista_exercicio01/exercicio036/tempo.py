numero_partes_tempo = 3
limite_minutos_segundos = 59

def validar_tempo(tempo):
    """
    Objetivo: Verificar se o tempo fornecido está no formato correto
    e se todas as partes são válidas.

    O tempo é dividido em 3 partes (split) e faz a verificação.

    Cada item é transformado em números inteiro usando o map().
    
    Cada parte do tempo é convertido em um número inteiro e 
    realiza o calculo necessário para obter o tempo total em
    segundos, utilizando a função lambda
    """
    partes = tempo.split(':')

    if len(partes) != numero_partes_tempo:
        print('Erro: O formato deve ser HH:MM:SS.')
        return False

    if not all([parte.isdigit() for parte in partes]):
        print('Erro: Horas, minutos e segundos devem ser números inteiros.')
        return False

    horas, minutos, segundos = map(int, partes)

    if horas < 0:
        print('Erro: As horas devem ser maiores ou iguais a 0')
        return False

    if not (0 <= minutos <= limite_minutos_segundos):
        print(f'Erro: Minutos devem estar entre 0 e {limite_minutos_segundos}.')
        return False

    if not (0 <= segundos <= limite_minutos_segundos):
        print(f'Erro: Segundos devem estar entre 0 e {limite_minutos_segundos}.')
        return False

    return True


obter_tempo_em_segundos = lambda tempo: (int(tempo.split(':')[0]) * 3600 +
                                         int(tempo.split(':')[1]) * 60 +
                                         int(tempo.split(':')[2]))
