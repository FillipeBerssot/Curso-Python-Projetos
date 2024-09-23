# 09- Solicite ao usuário que insira um número e imprima 20% dele somado com 30% dele:

numero = int(input("Digite aqui um numero: "))
numero_20_por_cento = numero * (20 /100)
numero_30_por_cento = numero * (30/100)
soma_das_porcentagens = numero_20_por_cento + numero_30_por_cento
print(f"20% do numero digitado é: {numero_20_por_cento}, 30% do numero digitado é: {numero_30_por_cento} e a soma dos dois é de: {soma_das_porcentagens}")
