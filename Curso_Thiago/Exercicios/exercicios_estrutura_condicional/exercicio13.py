#Ex.13- Escreva um programa que calcule o preço a pagar pelo fornecimento de energia elétrica.                                      
# Pergunte a quantidade de kWh consumida e o tipo de instalação: R para residências, I para indústrias e C para comércios. 
# Calcule o preço a pagar de acordo com a tabela a seguir:

# quantidade de kwh consumida e o tipo de instalaçao:
consumo = float(input("Digite aqui o valor consumido em kWh: "))
tipo_de_instalacao = input("Qual é o tipo de instalação, digite R para RESIDENCIAS, I para INDUSTRIAS, C para COMERCIOS: ")
tipo_de_instalacao = tipo_de_instalacao.upper()

#tipo de instalaçao:
if tipo_de_instalacao == "R":
   if consumo <= 500:
        preco_a_pagar = consumo * 0.40
   else:
        preco_a_pagar = consumo * 0.65

if tipo_de_instalacao == "I":
    if consumo <= 5000:
        preco_a_pagar = consumo * 0.55
    else:
        preco_a_pagar = consumo * 0.60
    
if tipo_de_instalacao == "C":
    if consumo <= 1000:
        preco_a_pagar = consumo * 0.55 
    else:
        preco_a_pagar = consumo * 0.60

# calcular o preço:
print(f"De acordo com o consumo de {consumo} kWh e o tipo de instalação então o preço a se pagar será R$ {preco_a_pagar}.")
