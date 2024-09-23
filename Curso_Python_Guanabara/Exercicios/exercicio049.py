# Ex. 049- Refaça o desafio 009, mostrando a tabuada de um numero que o usuario escolher, só que agora utilizando um laço for:

numero = int(input("Digite aqui um numero inteiro para saber sua Tabuada: "))
for multiplicacao in range(1,10+1):
    resultado = numero * multiplicacao
    print(f'{numero} x {multiplicacao} = {resultado}')
