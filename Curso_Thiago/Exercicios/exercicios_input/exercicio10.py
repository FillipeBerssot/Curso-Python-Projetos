# 10- Solicite ao usuário que insira dois números e imprima o resultado de a elevado a b + b elevado a a:

numero_1 = int(input("Digite um numero: ")) 
numero_2 = int(input("Digite outro numero: "))

a = numero_1
b = numero_2 

c = (a ** b) + (b ** a)
print(f"O primeiro numero digitado: {numero_1} será transformado em A e o segundo numero digitado: {numero_2} será transformado em B, sendo assim a equação de A ** B + B ** A terá a resposta de: {c}")
