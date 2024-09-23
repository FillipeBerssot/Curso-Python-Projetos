# Ex.109- Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parametro a mais, informando se o valor retornado 
# por elas vai ser ou não formatado pela função moeda(), desenvolvido no desafio 108:

from moedas_ex107 import dobro, metade, aumentar, diminuir, moeda


p = float(input('Digite um preço: R$ '))

print(f'A metade de {moeda(p, True)} é {moeda(metade(p, True))}')
print(f'O Dobro de {moeda(p)} é {moeda(dobro(p, True))}')
print(f'Aumentando 10%, temos {moeda(aumentar(p, 10, True))}')
print(f'Reduzindo 13%, temos {moeda(diminuir(p, 13, True))}')