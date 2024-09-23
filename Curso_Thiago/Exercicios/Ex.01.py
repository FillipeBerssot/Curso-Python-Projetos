import math
#Exercicios 01-

#1. *Soma Simples*:
   #- Calcule a soma de 7 e 5:

a = 7 + 5 
print(f"Ex.01 - A soma de 7 e 5 é igual a: {a}")

#2. *Subtração Simples*:
   #- Calcule a diferença entre 15 e 9:
b = 15 - 9
print(f"Ex.02 - A diferença entre 15 e 9 é: {b}")

#3. *Multiplicação Simples*:
   #- Calcule o produto de 4 e 6:

c = 4 * 6
print(f"Ex.03 - A multiplicação de 4 e 6 é: {c}")

#4. *Divisão Simples*:
   #- Calcule a divisão de 20 por 4:

d = 20 / 4
d1 = int(d)

print(f"Ex.04 - A divisão de 20 por 4 é: {d1}")

#5. *Potência Simples*:
   #- Calcule 3 elevado à potência de 4:
e = 3 ** 4
print(f"Ex.05 - 3 elevado à 4 é: {e}")

#6. *Arredondamento Simples*:
   #- Arredonde o número 8.75 para o inteiro mais próximo:
f = round(8.75)
print(f"Ex.06 - 8.75 arredondado ao inteiro mais proximo é: {f}")

#7. *Soma de Três Números*:
   #- Calcule a soma de 12, 8 e 7.

g = 12 + 8 + 7
print(f"Ex.07 - A soma de 12 + 8 + 7 é: {g}")

#8. *Subtração e Multiplicação*:
   #- Subtraia 5 de 20 e multiplique o resultado por 3:
h = 20 - 5
h1 = h * 3
print(f"Ex.08 - A subtração de 5 e 20 multiplicado o resultado por 3 é: {h1}")

#9. *Divisão e Potência*:
   #- Divida 16 por 2 e eleve o resultado ao quadrado:
i = 16 / 2 
i1 = i ** 2
i2 = int(i1)
print(f"Ex.09 - 16 divido por 2 e o resultado elevado ao quadrado é: {i2}")

#10. *Arredondamento para Baixo*:
    #- Arredonde o número 9.87 para baixo:

j = 9.87
j1 = math.floor(j)
print(f"Ex.10 - O numero 9.87 arredondado para baixo é: {j1}")


#11. *Arredondamento para Cima*:
    #- Arredonde o número 3.14 para cima:
k = 3.14
k1 = math.ceil(k)
print(f"Ex.11 - O numero 3.14 arredondado para cima é: {k1}")

#12. *Soma e Divisão*:
    #- Some 25 e 15 e divida o resultado por 10:
l = 25 + 15
l1 = l / 10
print(f"Ex.12 - A soma de 25 e 15 dividido por 10 é: {l1}")

#13. *Multiplicação de Dois Resultados*:
    #- Multiplique 3 por 4 e 5 por 2. Multiplique os dois resultados obtidos:
m = 3 * 4 
m1 = 5 * 2
m2 = m * m1
print(f"Ex.13 - A multiplicação de 3 por 4 e a multiplicação de 5 por 2, o resultado dos dois multiplicado é: {m2}")

#14. *Subtração e Potência*:
    #- Subtraia 7 de 15 e eleve o resultado ao quadrado:
n = 15 - 7
n2 = n ** 2
print(f"Ex.14 - A subtração de 7 e 15 com o resultado elevado ao quadrado é: {n2}")

#15. *Arredondamento de Divisão*:
    #- Divida 22 por 7 e arredonde o resultado para duas casas decimais:
o = 22 / 7
o2 = round(o, 2)
print(f"Ex.15 - Divisão de 22 por 7 com o resultado aredondado para duas casas decimais é: {o2}")


#16. *Potência de Soma de Potências*:
    #- Calcule 2 elevado à potência de 3 e 3 elevado à potência de 2. Some os dois resultados e exiba o resultado:
p = 2 ** 3 
p1 = 3 ** 2
p2 = p + p1
print(f"Ex.16 - O resultado de 2 elevado a potencia de 3 e 3 elevado a potencia de 2 somados é: {p2}")

#17. *Raiz Quadrada e Multiplicação*:
    #- Calcule a raiz quadrada de 25, multiplique o resultado por 4 e arredonde para o inteiro mais próximo:

numero = 25 
raiz_quadrada = math.sqrt(numero)
resultado = raiz_quadrada * 4
resultado_arredondado = round(resultado)
print(f"Ex.17 - O resultado da raiz quadrada de 25 multiplicado por 4, arredondado ao inteiro mais proximo é: {resultado_arredondado}")


#18. *Divisão Complexa e Arredondamento*:
    #- Divida 50 por (2 vezes 5) e arredonde o resultado para três casas decimais:
z = 50 / (2 * 5)
z1 = round(z, 3) 
print(f"Ex.18 - A divisao de 50 por (2 vezes 5) é {z}, arredondando tres casas decimais fica {z1}")

#19. *Média de Potências*:
    #- Calcule a média dos seguintes números: 2 elevado à potência de 3, 3 elevado à potência de 2, e 4 elevado à potência de 1:
q = 2 ** 3
q1 = 3 ** 2
q2 = 4 
media_q_q1_q2 = (q + q1 + q2) / 3
print(f"Ex.19 - A média dos seguintes numeros: 2 elevado a potencia de 3, 3 elevado a potencia de 2, e 4 elevado a potencia de 1 é: {media_q_q1_q2}")

#20. *Cálculo de Volume*: 
    #- Calcule o volume de um cilindro com raio 5 e altura 10, utilizando π = 3.14159. Arredonde o resultado para duas casas decimais:
volume = 3.14159 * (5 ** 2) * 10
arredondando = round(volume, 2)
print(f"Ex.20 - O volume de um cilindro de raio 5 e altura 10 utilizando PI = 3.14159 é {volume}, arredondado duas casas decimais fica {arredondando}")
