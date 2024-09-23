# Ex.08- Escreva um programa que leia três números e que imprima o maior e o menor:

a = float(input("Digite aqui algum valor: "))
b = float(input("Digite aqui algum valor: "))       
c = float(input("Digite aqui algum valor: "))

maior = max(a, b, c)
menor = min(a, b, c)

print(f"O maior valor dentre os 3 valores digitado é: {maior} ")
print(f"O menor valor dentre os 3 valores digitado é: {menor}")

#-----------------------------------------------------------------------------------------------------------------------

maior1 = a            #100
menor1 = a            #10

if b > maior1:         #10
    maior1 = b
elif b < menor1: 
    menor1 = b         #10

if c > maior1:         
    maior1 = c
elif c < menor1:         #7
    menor1 = c


print(f"O maior valor dentre os 3 valores digitados é: {maior1}")
print(f"O menor valor dentre os 3 valores digitados é: {menor1}")
