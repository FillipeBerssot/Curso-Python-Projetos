#Ex.11- Escreva um programa que leia dois números e que pergunte qual operação você deseja realizar. 
# Você deve poder calcular soma (+), subtração (-), multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada:

numero1 = float(input("Digite aqui um numero: "))
numero2 = float(input("Digite aqui outro numero: "))

operacao = input("Digite qual operação voçê quer utilizar adição (+), subtração (-), multiplicação (*), divisão (/): ")

if operacao == "+":
    resultado = numero1 + numero2
    print(f"De acordo com os valores digitados e a operação escolhida (+) o resultado é: {resultado}")
elif operacao == "-":
    resultado = numero1 - numero2
    print(f"De acordo com os valores digitados e a operação escolhida (-) o resultado é: {resultado}")
elif operacao == "*":
    resultado = numero1 * numero2
    print(f"De acordo com os valores digitados e a operação escolhida (*) o resultado é: {resultado}")
elif operacao == "/":
    resultado = numero1 / numero2
    print(f"De acordo com os valores digitados e a operação escolhida (/) o resultado é: {resultado}")
else:
    resultado = "Digite um operador válido."
    print(resultado)
