# Ex.06- Escreva uma expressão para determinar se uma pessoa deve ou não pagar imposto. Considere que somente as pessoas que tem um salario maior que R$ 1.200,00 pagam imposto:

# 1200.00 > pagam imposto
# salario > 1200.00  = pagar imposto 

salario = float(input("Digite aqui o seu salario: "))

if salario > 1200.00:
    print("Voçê deve pagar imposto.")
else:
    print("Voçê não deve pagar imposto.")
