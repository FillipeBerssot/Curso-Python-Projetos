# Ex.004 - Escreva um programa que calcule o Indice de Massa Corporal (IMC) e classifique o usuario como abaixo do peso, peso normal,
# sobrepeso ou obeso:

# Abaixo do peso     18.5 >= peso
# Peso Normal        18.5 <  peso <= 24.9
# Sobrepeso           25  <  peso <= 29.9
# Obeso               30  < peso 

def IMC(peso, altura):
    print('\nCalculo do IMC:')
    imc = peso / (altura * altura)

    if 18.5 >= imc:
        return f'O seu IMC é {imc:.2f}. Voçê está Abaixo do Peso.'
    elif 18.5 < imc <= 24.9:
        return f'O seu IMC é {imc:.2f}. Voçê está com um Peso Normal.'
    elif 25 < imc <= 29.9:
        return f'O seu IMC é {imc:.2f}. Voçê está com Sobrepeso.'
    else:
        return f'O seu IMC é {imc:.2f}. Voçê está Obeso.' 
    

peso = float(input('Digite aqui o seu peso atual em kgs: '))
altura = float(input('Agora digite a sua altura: '))
print(IMC(peso, altura))