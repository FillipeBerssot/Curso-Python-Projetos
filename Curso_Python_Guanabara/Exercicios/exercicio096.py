# Ex.096- Faça um programa que tenha uma função chamada area(), que receba as dimensões de um terreno retangular
# (largura e comprimento) e mostre a area do terreno:

def area(larg, comp):
    area_terreno = larg * comp 
    print(f'A área de um terreno {larg} x {comp} é de {area_terreno:.2f}m2')


l = float(input('Digite a largura(base) do terreno: '))
c = float(input('Digite o comprimento(altura) do terreno: '))
area(l, c)


