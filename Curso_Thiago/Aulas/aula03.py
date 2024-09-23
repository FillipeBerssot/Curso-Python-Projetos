num1 = 5
num2 = 3.5

print(type(num1))                                            #Type (tipo), mostra o tipo da variável
print(type(num2))

a = float(num1)                                              #Mudar tipo da variável, colocar o tipo antes da variável float(num1)
print(a)
print(type(a))

b = int(num2)                                                #Mudando de float para int, arredonda para baixo, (3.5 vira 3)
print(b)
print(type(b))

print(num1 + num2)                                           #Soma  
print(num1 - num2)                                           #Subtraçâo
print(num1 * num2)                                           #Multiplicação
print(10 / 3)                                                #Divisão
print(10 // 3)                                               #For Division = Retorna com Divisão Inteira
print(10 % 3)                                                #Resto de Divisão
print(10 ** 3)                                               #Exponenciação

print(3 + 5 * 7 + 3)
print((3 + 5) * (7 + 3))                                     #O que estiver entre Parênteses, vai ser realizado primeiro.

print(abs(-15))                                              #ABS serve para imprimir numero Absoluto (-15 vira 15)
print(pow(3, 3))                                             #POW serve para fazer a Exponenciação de um numero
print(max(1, 85, 17, -155, 5))                               #MAX serve para mostrar o maior numero
print(min(1, 85, 17, -155, 5))                               #MIN serve para mostrar o menor numero
print(round(8.567, 1))                                       #ROUND serve para arrendondar por aproximaçâo (8.8 vira 9 // 8.4 vira 8)
