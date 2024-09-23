# Desafio 019- Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido:

import random                                    # import random  ---> Importar uma biblioteca random (aleatorio) para fazer o computador exibir um numero aleatorio na tela


print("--------------Sorteio--------------")
print("ALUNOS:")
aluno1 = print("João será o numero 1")
aluno2 = print("Maria será o numero 2")
aluno3 = print("Bastião será o numero 3")
aluno4 = print("Josefina será o numero 4")

numero_aleatorio = random.randint(1,4)
print(f"O numero sorteado foi: {numero_aleatorio}")

if numero_aleatorio == 1:
    print("João foi o escolhido")
elif numero_aleatorio == 2:
    print("Maria foi a escolhida")
elif numero_aleatorio == 3:
    print("Bastião foi o escolhido")
elif numero_aleatorio == 4:
    print("Josefina foi a escolhida")


# OBS:
# random.randrange   ---->  Para gerar números inteiros em um intervalo definido, na randrange o valor final do intervalo nunca é gerado.
# random.randint     ---->  Para gerar números inteiros em um intervalo definido.
# random.random      ---->  Essa função sempre será irá gerar um float com diversas casas decimais. Entre 0 e 1.
# random.choice      ---->  A função choice recebe como argumento uma lista de elementos, que podem ser números ou textos, e retorna aleatoriamente um único elemento dela.
# random.choices     ---->  A função choices permite selecionar múltiplos elementos aleatoriamente dentro dessa lista.
# random.sample      ---->  A função permite selecionar múltiplos elementos aleatoriamente dentro de uma lista, garantindo que não haja repetição de elementos selecionados.
# random.shuffle     ---->  Essa função serve para embaralhar os elementos de uma lista.