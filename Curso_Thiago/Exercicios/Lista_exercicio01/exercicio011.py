# Ex. 011- Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.
# usuario colocar flutuante tambem:
numero01 = float(input('Digite aqui um numero inteiro: '))
numero02 = float(input('Digite aqui outro numero inteiro: '))

#print(numero01)
#print(numero02)

for numeros in range(numero01 + 1, numero02):
    print(f'Os numeros que estão no intervalo do dois numeros inteiros digitados são: {numeros}')