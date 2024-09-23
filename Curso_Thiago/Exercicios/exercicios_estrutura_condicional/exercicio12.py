#Ex.12- Escreva um programa para aprovar o empréstimo bancário para compra de uma casa. O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar.
# O valor da prestação mensal não pode ser superior a 30% do salário. Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar:

# 1- as perguntas: 
print("Bem vindo ao programa de emprestimo bancario!")

valor_da_casa = float(input("Qual o valor da casa R$ "))
salario = float(input("Digite aqui o seu salario atual R$ "))
quantidade_anos = float(input("Digite em quantos anos deseja pagar o emprestimo: "))

# 2 - calculos:
quantidade_anos_meses = quantidade_anos * 12                                      #converter os anos em meses
quantidade_anos_meses = round(quantidade_anos_meses)

valor_da_prestacao = valor_da_casa / quantidade_anos_meses                        #valor das prestações
print(f"O emprestimo será dividido em {quantidade_anos_meses} meses")
valor_da_prestacao = (round(valor_da_prestacao, 2))
print(f"O valor de cada prestação do emprestimo será R$ {valor_da_prestacao}")

# 3- ver se pode ou nao pode emprestar:  valor da prestaçao nao pode ser superior a 30%

if valor_da_prestacao < salario * 0.30:
    print("Emprestimo foi aceito com sucesso, parabens!")
else:
    print(f'Infelizmente o seu emprestimo foi recusado, pois a prestação mensal está superior a 30% do seu salario.')
