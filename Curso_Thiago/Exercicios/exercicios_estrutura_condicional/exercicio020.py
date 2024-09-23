#.Ex20- Faça um programa que peça para o usuário inserir dois números e que verifique qual é o menor ou se eles são iguais:

numero1 = float(input("Insira aqui um numero: "))
numero2 = float(input("Insira aqui outro numero: "))

if numero1 < numero2:
    print("O primeiro numero digitado é o menor.")
elif numero2 < numero1:
    print("O segundo numero digitado é o menor.")
else:
    print("Os numeros são iguais.")