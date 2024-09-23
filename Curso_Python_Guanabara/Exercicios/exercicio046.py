# Ex. 046- Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de  10 ate 0,
# com uma pausa de 1 segundo entre eles:

import time


print('======== Contagem Regressiva ========')
for c in range(10, -1, -1):
    time.sleep(1)    
    print(c)
print('======== FOGOS ESTOURANDO ========')
