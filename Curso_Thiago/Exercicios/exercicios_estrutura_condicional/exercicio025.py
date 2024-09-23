#Ex.25- Escreva um programa que leia um nome e verifique se este nome é igual ao seu. Imprimir conforme o caso: “NOME CORRETO” ou “NOME INCORRETO”:

nome = input("Digite um nome e tente acertar o nome correto: ")
nome = nome.capitalize()

if nome == "Fillipe":
    print(f"Nome digitado foi {nome}, NOME CORRETO")
else:
    print(f"Nome digitado foi {nome}, NOME INCORRETO")