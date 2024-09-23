#Ex.22- .Faça um programa que peça para o usuário inserir dois números, pergunte se ele quer realizar a operação de multiplicação ou de divisão e que,
# a partir desta escolha, mostre o resultado na tela:

numero1 = float(input("Insira aqui um numero: "))
numero2 = float(input("Insira aqui outro numero: "))

print("Digite agora qual opção voçê quer: ")
print("Digite (*) para multiplicar os dois numeros inseridos.")
print("Digite (/) para dividir os dois numeros inseridos.")
operacao = input("  ")

if operacao == "*":
    calculo = numero1 * numero2
    print(f"A multiplicaçâo entre os dois numeros inseridos é {calculo}.")
elif operacao == "/":
    calculo = numero1 / numero2
    print(f"A divisão entre os dois numeros digitados é {calculo}")
else:
    print("Digite uma das opções válidas.")