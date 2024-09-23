# Desafio 013- Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento:

salario = float(input("Digite aqui o seu salario atual em reais: "))
# print(salario)

aumento = salario * 15 / 100
print(f"De acordo com o aumento de 15% no seu salario atual, o aumento será de R$: {aumento:.2f}")

novo_salario = salario + aumento
print(f"Agora com o aumento de 15% adicionado ao seu salario, o salario atual será de R$: {novo_salario:.2f}")