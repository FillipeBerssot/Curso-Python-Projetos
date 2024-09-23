# Ex. 023- Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1:

num = int(input("Digite um número inteiro: "))

divisores = 0

if num >= 2:
    for i in range(1, num + 1):
        if num % i == 0:
            divisores += 1

if divisores == 2:
    print(f"{num} é um número primo.")
else:
    print(f"{num} não é um número primo.")
