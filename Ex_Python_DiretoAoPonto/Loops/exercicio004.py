# Ex.004 - Escreva um programa que gere uma a tabuada de um número:


def tabuada(numero):
    tabuada = ''
    for i in range(1, 11):
        tabuada += f'{numero} x {i} = {numero * i}\n'
    print(f'TABUADA de {numero}:')
    return tabuada          


numero = 3
print(tabuada(numero))
