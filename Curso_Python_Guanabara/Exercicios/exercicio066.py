# Ex.066- Crie um programa que leia varios numeros inteiros pelo teclado. O programa so vai parar quando o usuario digitar o valor 999,
# que é a condiçao de parada. No final, mostre os quantos numeros foram digitados e qual foi a soma entre eles.(Desconsiderando o Flag):

numero = 0
soma = 0
contador = 0

while True:
    numero = int(input('Digite aqui varios numeros e descubra soma entre eles: [Digite 999 para parar o programa] '))
    if numero == 999:
        break
    contador += 1
    soma += numero
    
 
print(f'A soma dos {contador} numeros digitados é: {soma}')

