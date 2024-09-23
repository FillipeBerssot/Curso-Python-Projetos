# MODULOS E PACOTES :
#   Modularização

#   Exemplo 01:
from uteis_aula021 import fatorial, triplo, dobro


num = int(input('Digite um valor: '))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobro do valor {num} é {dobro(num)}')
print(f'O triplo do valor {num} é {triplo(num)}')


# Pacotes:
#   Para quando so a modularização não resolve
#   Pacote com modulos
#   Criar uma pasta para os pacotes

