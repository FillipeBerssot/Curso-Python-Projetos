#Ex.21- Faça um programa que peça para o usuário inserir dois números, pergunte se ele quer realizar a operação de adição ou de subtração e, 
# que a partir desta escolha, mostre o resultado na tela:

numero1 = float(input("Insira aqui um numero: "))
numero2 = float(input("Insira aqui outro numero: "))

print("Digite agora qual opção voçê quer: ")
print("Digite (+) para somar os dois numeros inseridos.")
print("Digite (-) para subtrair os dois numeros inseridos.")
operacao = input("  ")

if operacao == "+":
    calculo = numero1 + numero2
    print(f"A soma entre os dois numeros inseridos é {calculo}.")
elif operacao == "-":
    calculo = numero1 - numero2
    print(f"A subtração entre os dois numeros digitados é {calculo}")
else:
    print("Digite uma das opções válidas.")