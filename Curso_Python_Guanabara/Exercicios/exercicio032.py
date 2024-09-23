# Desafio 032- Faça um programa que leia um ano qualquer e mostre se ele e BISSEXTO:

ano = float(input("Digite aqui um ano aleatorio para saber se ele e BISSEXTO ou não: "))

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"O ano de {ano} é um ano BISSEXTO")
else:
    print(f"O ano de {ano} não é um ano BISSEXTO")