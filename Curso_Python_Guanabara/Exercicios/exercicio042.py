# Desafio 042- Refaça o Desafio 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triangulo será formado:
# - Equilatero: Todos os lados iguais:
# - Isosceles: dois lados iguais:
# - Escaleno: Todos os lados diferentes:



r1 = float(input('Digite aqui o valor da primeira reta para ver se forma um triangulo: '))
r2 = float(input('Digite aqui o valor de segunda reta para ver se forma um triangulo: '))
r3 = float(input('Digite aqui o valor de terceira reta para ver se forma um triangulo: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("SIM, PODE  FORMAR UM TRIANGULO")
    if r1 == r2 == r3:
        print("FORMA UM TRIANGULO EQUILATERO")
    elif r1 != r2 != r3 != r1:
        print("FORMA UM TRIANGULO ESCALENO")
    else:
        print("FORMA UM TRIANGULO ISOSCELES")
else:
    print("NÃO, NÃO PODE FORMAR UM TRIANGULO")
