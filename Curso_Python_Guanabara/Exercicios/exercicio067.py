# Ex.067- Faça um programa que mostre a tabuada de varios numeros, um de cada vez, para cada valor digitado pelo usuario.
# O programa será interrompido quando o numero solicitado for negativo:

numeros = 0

while True:
    numeros = int(input('Digite aqui um numero e descubra sua TABUADA [Digite qualquer numero negativo para encerrar o programa]: '))
    if numeros < 0:
        print('PROGRAMA ENCERRADO.')
        break
    print('------- TABUADA -------')
    for contador in range(1,11):
        tabuada = numeros * contador
        print(f'       {numeros} x {contador} = {tabuada}')
        