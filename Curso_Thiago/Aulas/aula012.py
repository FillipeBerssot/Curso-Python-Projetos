# Funções Lambdas:
#     Funções anônimas, não precisa definir um nome, voçê define já usando direto.
#     Recebe um valor, e devolve a 'resposta'.

#       Exemplo 01:
#         Modo tradicional, usando uma função normal:

valor = 1000
def calcular_imposto(valor):
    return valor * 0.3
print(f'Print do modo tradicional, usando função normal: {calcular_imposto(valor)}.')

#       Exemplo 02:
#         Utilizando Lambda:

calcular_imposto02 = lambda valor: valor * 0.3
print(f'Print utilizando lambda: {calcular_imposto02(valor)}.')

# Funções Map:
#    Aplica uma função em cada item de uma lista de itens.
#    Map exigi duas informações, qual a função que vai aplicar em cada um dos itens e
#    qual é a lista de itens que ele vai aplicara função.
#    Se quiser que o map retorne um print em uma lista, deve-se utilizar list.

#       Exemplo 01:
#         Modo tradicional, usando for:

precos = [1000, 1500, 1250, 2500]
def adicionar_imposto(preco):
    return preco * 1.1

precos_com_imposto = []
for preco in precos:
    precos_com_imposto.append(adicionar_imposto(preco))
print(f'Print do modo tradicional utilizando for: {precos_com_imposto}')

#       Exemplo 02:
#         Utilizando o map:

precos = [1000, 1500, 1250, 2500]
def adicionar_imposto(preco):
    return preco * 1.1
precos_com_imposto02 = list(map(adicionar_imposto,precos))
print(f'Print utilizando o map: {precos_com_imposto02}')

# Exemplo utilizando lambda e o map juntos:

numeros1 = [10, 20, 30, 40, 50]
numero2 = [10, 20, 30, 50, 40]

soma_numeros = list(map(lambda x,y: x + y, numeros1, numero2))
print(f'Soma de todos os numeros utilizando função lambda e map: {soma_numeros}')