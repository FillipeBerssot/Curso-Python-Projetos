# Desafio 034- Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.
# Para salarios superiores a R$ 1.250,00, calcule um aumento de 10%:
# Para os inferiores ou iguais o aumento é de 15%:

salario = float(input("Digite aqui o seu salario atual R$: "))

if salario <= 1250:
    novo_salario = salario * 0.15
    print(f"O seu novo salario será de R$: {novo_salario + salario}, por causa do aumento de 15%")
else:
    novo_salario = salario * 0.10
    print(f"O seu novo salario será de R$: {novo_salario + salario}, por causa do aumento de 10%")