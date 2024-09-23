# 13- Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

valor_do_salario = float(input("Digite aqui o valor do seu salario atual: "))
porcentagem_do_aumento = float(input("Digite agora a porcentagem do aumento salarial: "))

valor_do_aumento_salario = valor_do_salario * (porcentagem_do_aumento / 100)
valor_do_novo_salario = valor_do_salario + valor_do_aumento_salario

print(f"De acordo com os valores digitados o aumento salarial vai ser de R$: {valor_do_aumento_salario} e o salario atual será de R$: {valor_do_novo_salario}")