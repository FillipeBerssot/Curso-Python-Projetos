# 05- Faça um programa que solicite o nome completo do usuário e exiba somente o seu primeiro sobrenome:     !!!!!Modo simples


nome_completo = input("Digite aqui o seu nome completo: ")
sobrenome2 = nome_completo.split(" ")                                             #.split faz uma divisao dentro da string considerando o que foi seleciona (" " vai fazer divisao nos espaços, "i" ira fazer divisao em cada i)
print(f"O seu sobrenome é: {sobrenome2[1]}")                                      # [1] para que imprima somente do 1 em diante, no sendo so o sobrenome em diante