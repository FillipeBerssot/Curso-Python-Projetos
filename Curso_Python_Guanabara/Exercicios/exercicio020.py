# Desafio 020- O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e
# mostre a ordem sorteada:

import random


# print("-------------- Sorteio Apresentação do Trabalho --------------")
# print("ALUNOS:")
# aluno1 = print("João será o numero 1")
# aluno2 = print("Maria será o numero 2")
# aluno3 = print("Bastião será o numero 3")
# aluno4 = print("Josefina será o numero 4")

# numero_aleatorio = [1, 2, 3, 4]
# print(f"A sequencia sorteada para começar a apresentação dos trabalhos é: {random.sample(numero_aleatorio, k=4)}")


n1 = str(input("Primeiro aluno: "))
n2 = str(input("Segundo aluno: "))
n3 = str(input("Terceiro aluno: "))
n4 = str(input("Quarto aluno: "))

lista = [n1, n2, n3, n4]
random.shuffle(lista)
print("A ordem de apresentação será: ")
print(lista)