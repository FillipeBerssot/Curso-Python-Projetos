# Desafio 043- Desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do Peso:
# - Entre 18.5 e 25: Peso Ideal:
# - 25 até 30: Sobrepeso:
# - 30 até 40: Obesidade:
# - Acima de 40: Obesidade Mórbida:


print('-=-=-=-=-=-=-=-=-=-    Tabela IMC     -=-=-=-=-=-=-=-=-=-')
print('       Veja qual o seu Status de acordo com seu IMC     ')
print('-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-')
print('Abaixo de 18.5: Abaixo do Peso')
print('Entre 18.5 e 25: Peso Ideal')
print('25 até 30: Sobrepeso')
print('30 até 40: Obesidade')
print('Acima de 40: Obesidade Mórbida')
print('-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-')

peso = float(input('Digite aqui o seu peso atual em kgs: '))
altura = float(input('Digite agora a sua altura em metros: '))
imc = peso / (altura * altura)

print(f'De acordo com os dados inseridos o seu IMC é: {imc:.2f}')

if imc <= 18.5:
    print('O seu status é: ABAIXO DO PESO')
elif imc <= 25:
    print('O seu status é: PESO IDEAL')
elif imc <= 30:
    print('O seu status é: SOBREPESO')
elif imc <= 40:
    print('O seu status é: OBESIDADE')
else:
    print('O seu status é: OBESIDADE MÓRBIDA')