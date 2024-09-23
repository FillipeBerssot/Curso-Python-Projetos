# Ex. 108- Adapte o codigo do desafio 107, criando uma função adicional chamada moeda() que consiga mostrar os valores
# como um valor monetario formatado:

from moedas_ex107 import dobro, metade, aumentar, diminuir, moeda


p = float(input('Digite um preço: R$ '))

print(f'A metade de {moeda(p)} é {moeda(metade(p))}')
print(f'O Dobro de {moeda(p)} é {moeda(dobro(p))}')
print(f'Aumentando 10%, temos {moeda(aumentar(p, 10))}')
print(f'Reduzindo 13%, temos {moeda(diminuir(p, 13))}')