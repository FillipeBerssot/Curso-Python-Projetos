# Ex.017 - Faça um programa que leia o seu tempo em um estacionamento. Se a sua permanencia for inferior a 3 minutos voçê pode sair de graça.
# Caso contrario, voçê deve pagar 15 reais:


def simula_estacionamento(entrada_estacionamento, saida_estacionamento):
    partes_entrada = entrada_estacionamento.split(':')
    hora_entrada = int(partes_entrada[0])
    minutos_entrada = int(partes_entrada[1])
    tempo_entrada_minutos = hora_entrada * 60 + minutos_entrada

    partes_saida = saida_estacionamento.split(':')
    hora_saida = int(partes_saida[0])
    minutos_saida = int(partes_saida[1])
    tempo_saida_minutos = hora_saida * 60 + minutos_saida

    permanencia_total = tempo_saida_minutos - tempo_entrada_minutos

    if permanencia_total > 3:
        return f'\nA sua permanencia total no estacionamento foi de {permanencia_total} minutos. Voçê excedeu o limite de 3 minutos, voçê deve pagar 15 reais.'
    else:
        return f'\nA sua permanencia total no estacionamento foi de {permanencia_total} minutos. Voçê não excedeu o limite de 3 minutos, voçê pode sair de graça.'
    
    
entrada_estacionamento = input('Digite aqui o Horario em que voçê chegou no estacionamento (00:00): ')
saida_estacionamento = input('Digite aqui o Horario de saída do estacionamento (00:00): ')

print(simula_estacionamento(entrada_estacionamento, saida_estacionamento))