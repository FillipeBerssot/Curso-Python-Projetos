# 18- Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, e calcule quantos dias de vida um fumante perderá. Exiba o total em dias:

cigarros_por_dia = float(input("Digite aqui a quantidade de cigarros fumados por dia: "))
quantos_anos_fumando = float(input("Digite aqui por quantos anos voçe já fuma: "))

total_de_cigarros = cigarros_por_dia * quantos_anos_fumando * 365


minutos_perdidos = total_de_cigarros * 10
dias_perdidos = minutos_perdidos / (24 * 60)
dias_perdidos_arredondados = round(dias_perdidos)

print(f"De acordo com os dados inseridos voçê perdeu aproximadamente {dias_perdidos_arredondados} dias de vida por causa do cigarro.")
