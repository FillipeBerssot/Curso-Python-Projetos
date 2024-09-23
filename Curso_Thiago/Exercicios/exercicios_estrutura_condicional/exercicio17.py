#Ex.17- Faça um programa que pergunte ao usuário se ele possui irmãos, e que, caso a resposta seja “sim”, pergunte quantos e mostre na tela uma mensagem de sua escolha.
# No caso de o usuário responder “não”, pergunte se ele gostaria de ter e mostre na tela uma mensagem de sua escolha:

possui_irmaos = input("Voçê possui irmâos? ")
possui_irmaos = possui_irmaos.capitalize()

if possui_irmaos == "Sim":
    quantos = input("Quantos irmãos? ")
    print(f"Voçê possui {quantos} irmãos. Parabens!")

if possui_irmaos == "Não":
    gostaria_de_ter = input("Mas gostaria de ter? ")
    gostaria_de_ter = gostaria_de_ter.capitalize()
    if gostaria_de_ter == "Sim":
        print("Que legal!")
    elif gostaria_de_ter == "Não":
        print("Que pena!")
    else:
        print("Opçao inválida. Digite Sim ou Não.")