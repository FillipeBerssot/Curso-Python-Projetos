#Ex.16- Faça um programa que peça para o usuário inserir um nome, pergunte se ele gosta do nome e, em ambos os possíveis casos de resposta (Sim ou Não),
# mostre uma mensagem de sua escolha na tela:

nome = input("Insira um nome: ")

print("Voçê gosta desse nome? ")
print("Digite 1 para sim")
print("Digite 2 para não")
escolha_do_usuario = input(" ")

if escolha_do_usuario == "1":
    print("Parabéns voçê gosta desse nome.")
elif escolha_do_usuario == "2":
    print("Infelizmente voçê não gosta desse nome.")
else:
    print("Digite uma opçâo válida.")