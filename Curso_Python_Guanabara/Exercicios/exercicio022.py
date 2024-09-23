# Desafio 022- Crie um programa que leia o nome completo de uma pessoa e mostre:
# -> O nome com todas as letras maiusculas:
# -> O nome com todas minusculas:
# -> Quantas letras ao todo (sem considerar espaços):
# -> Quantas letras tem o primeiro nome:

nome_completo = str(input("Digite aqui o seu nome completo: ")).strip()

nome_completo_m = nome_completo.upper()
print(f"O seu nome completo em Maiusculo é {nome_completo_m}")
nome_completo_min = nome_completo.lower()
print(f"O seu nome completo em Minusculo é {nome_completo_min}")

print(f"O seu nome completo tem ao todo {len(nome_completo) - nome_completo.count(" ")} letras")

print(f"O seu primeiro nome tem {nome_completo.find(" ")} letras")