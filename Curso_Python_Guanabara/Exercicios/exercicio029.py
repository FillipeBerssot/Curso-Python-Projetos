# Desafio 029- Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado:
# A multa vai custar R$ 7,00 por cada Km acima do limite:

print('---------- Seja bem vindo a Máfia do Transito mais conhecida como DETRAN ----------')
print('Veja aqui o quanto voçê vai contribuir para o natal dos nossos queridos funcionarios:')


print('Lembrando que nossos radares multam em R$ 7,00 a cada km acima de 80 km/h')

velocidade = float(input('Digite aqui a velocidade em kms que voçê passou no radar: '))
multa = (velocidade - 80) * 7

if velocidade <= 80:
    print(f'Sua velocidade foi de {velocidade} km/h, para o nosso azar voçê não será multado.')
else:
    print(f'Sua velocidade foi de {velocidade} km/h, voçê terá que pagar R$ {multa}, OTÁRIO!!!')

