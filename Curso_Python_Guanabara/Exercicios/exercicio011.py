# Desafio 011- Faça um programa que leia a altura e a largura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-la, sabendo que
# cada litro de tinta, pinta uma area de 2m quadrados:

altura = float(input("Digite aqui a altura em metros da parede: "))
# print(altura)
largura = float(input("Digite agora a largura em metros da parede: "))
# print(largura)


area = altura * largura
print(f"A area da parede é: {area} m²")

tinta = area / 2
print(f'Sabendo que 1 litro de tinta pinta uma area de 2m², de acordo com a area total da parede de {area} m², voçê precisaria de {tinta:.1f} litros de tinta para poder pintar sua parede.')


