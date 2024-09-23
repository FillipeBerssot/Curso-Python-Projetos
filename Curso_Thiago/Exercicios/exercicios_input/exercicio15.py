# 15- Escreva um programa que calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem:

distancia_a_percorrer = float(input("Digite aqui a distancia em Kms a percorrer na viagem: "))
velocidade_media = float(input("Digite a velocidade media esperada para a viagem: "))

tempo_da_viagem = distancia_a_percorrer / velocidade_media

tempo_da_viagem_horas = int(tempo_da_viagem)
tempo_da_viagem_minutos = int((tempo_da_viagem - tempo_da_viagem_horas) * 60)


print(f"O tempo total da viagem será {tempo_da_viagem_horas} horas e {tempo_da_viagem_minutos} minutos.")
