#Ex.09- 9. Escreva um programa que pergunte o salário do funcionário e calcule o valor do aumento. 
# Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, de 15%.

salario = float(input("Digite aqui o seu salario atual: "))
#salario > 1250.00 aumento de 10%
#salario <= 1250.00 aumento de 15%

if salario <= 1250.00:
    aumento = salario * 0.15
else:
    aumento = salario * 0.10

salario_final = salario + aumento 

print(f"Seu salario mais o aumento de R$ {aumento} será de R$ {salario_final}")
