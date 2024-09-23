# Ex. 107- Crie um modulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça tambem um programa que importe esse modulo e use algumas dessas funções:


from moedas_ex107 import dobro, metade, aumentar, diminuir


p = float(input('Digite um preço: R$ '))

print(f'A metade de {p} é {metade(p)}')
print(f'O Dobro de {p} é {dobro(p)}')
print(f'Aumentando 10%, temos {aumentar(p, 10)}')
print(f'Reduzindo 13%, temos {diminuir(p, 13)}')