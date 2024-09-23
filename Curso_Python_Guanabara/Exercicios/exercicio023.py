# Desafio 023- Faça um programa que leia um numero de 0 ao 9999 e mostre na tela cada um dos digitos separados:
# Ex: digite um numero : 1834
# Ex: unidade 4, dezena 3, centena 8, milhar 1.

# numero = int(input("Digite aqui um numero de 0 a 9999: "))

# numero_formatado = str(numero)

# print(f"Analisando o numero {numero} ")
# print(f"Unidade: {numero_formatado[3]}")
# print(f"Dezena: {numero_formatado[2]}")
# print(f"Centena: {numero_formatado[1]}")
# print(f"Milhar: {numero_formatado[0]}")


numero = int(input("Digite aqui um numero de 0 a 9999: "))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10
print(f"Vamos analisar o numero digitado: {numero}")
print(f"A unidade do numero digitado: {unidade}")
print(f"A dezena do numero digitado: {dezena}")
print(f"A centena do numero digitado: {centena}")
print(f"O milhar do numero digitado: {milhar}")
