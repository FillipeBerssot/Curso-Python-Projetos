# Desafio 027- Faça um programa que leia o nome de uma pessoa , mostrando em seguida o primeiro e o ultimo nome separadamente:
# Ex: Ana Maria de Souza , primeiro: Ana, ultimo: Souza.

nome = str(input("Digite aqui o seu nome completo: ")).lower().strip()

nome = nome.split()
print(nome)

primeiro_nome = nome[0]
print(f"O primeiro nome do seu nome é: {primeiro_nome.title()}")

ultimo_nome = nome[-1]
print(f"O ultimo nome do seu nome é: {ultimo_nome.title()}")