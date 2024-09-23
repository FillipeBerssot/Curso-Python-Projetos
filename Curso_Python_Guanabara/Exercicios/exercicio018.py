# Desafio 018- Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo:
import math

angulo = float(input("Digite aqui o valor de um angulo qualquer: "))
radiano = math.radians(angulo)                                    # math.radians   --> funcionalidade importada da biblioteca MATH para descobrir o valor do angulo em RADIANOS
print(radiano)       
print(f"O angulo digitado convertido para radianos é: {radiano}")
                                                


seno = math.sin(radiano)                                          # math.sin   --->  descobrir o seno
print(f"O seno do angulo digitado é: {seno:.2f}")                      
cosseno = math.cos(radiano)                                       # math.cos   --->  descobrir o cosseno
print(f"O cosseno do angulo digitado é: {cosseno:.2f}")
tangente = math.tan(radiano)                                      # math.tan   --->  descobrir a tangente
print(f"A tangente do angulo digitado é: {tangente:.2f}")
