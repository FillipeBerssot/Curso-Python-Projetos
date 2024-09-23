#Ex.18- Faça um programa que permita o usuário escolher entre três opções de bebidas e mostre na tela a bebida escolhida:

print("------ Bem Vindo a Distribuidora Paraíba ------")

print("Temos Coca-Cola")
print("Temos Guarana")
print("Temos Guarana Jesus")

print("Por Favor digite uma opção de bebida: ")
print("Para Coca-Cola digite 1:")
print("Para Guarana digite 2:")
print("Para Guarana Jesus digite 3:")

escolha_do_usuario = input(" ")

#Cola Cola:
if escolha_do_usuario == "1":
    print("Voçê escolheu Coca-Cola. Agora escolha se voçê quer 1.5L ou 2L. Digite a opção desejada: ")
    escolha_do_usuario2 = input(" ")
    if escolha_do_usuario2 == "1.5L":                                                                                        
        print("Voçê escolheu Coca-Cola 1.5L. Aguarde o entregador. Muito Obrigado!")
    elif escolha_do_usuario2 == "2L":
        print("Voçê escolheu Coca-Cola 2L. Aguarde o entregador. Muito Obrigado!")

#Guarana:
if escolha_do_usuario == "2":
    print("Voçê escolheu Guarana. Agora escolha se voçê quer 1.5L ou 2L. Digite a opção desejada: ")
    escolha_do_usuario2 = input(" ")
    if escolha_do_usuario2 == "1.5L":
        print("Voçê escolheu Guarana 1.5L. Aguarde o entregador. Muito Obrigado!")
    elif escolha_do_usuario2 == "2L":
        print("Voçê escolheu Guarana 2L. Aguarde o entregador. Muito Obrigado!")

#Guarana Jesus:
if escolha_do_usuario == "3":
    print("Voçê escolheu Guarana Jesus. Agora escolha se voçê quer 1.5L ou 2L. Digite a opção desejada: ")
    escolha_do_usuario2 = input(" ")
    if escolha_do_usuario2 == "1.5L":
        print("Voçê escolheu Guarana Jesus 1.5L. Aguarde o entregador. Muito Obrigado!")
    elif escolha_do_usuario2 == "2L":
        print("Voçê escolheu Guarana Jesus 2L. Aguarde o entregador. Muito Obrigado!")