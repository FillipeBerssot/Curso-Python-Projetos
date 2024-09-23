# Ex.001 - Crie um programa que classifique uma pessoa como criança (0-12 anos), adolescente (13-19 anos), adulto (20-64 anos)
# ou idoso (65+ anos) com base na idade inserida:

# Criança       0 < idade <= 12
# Adolescente  13 < idade <= 19
# Adulto       20 < idade <= 64
# Idoso        65 < idade 

def classificacao_pessoa_por_idade(idade):
    if 0 < idade <= 12:
        return 'Voçê é uma Criança.'
    elif 12 < idade <= 19:
        return 'Voçê é um Adolescente.'
    elif 19 < idade <= 64:
        return 'Voçê é um Adulto.'
    else:
        return 'Voçê é um Idoso.'
    

idade = int(input('Digite aqui a sua idade e descubra se voçê e uma Criança, Adolescente, Adulto ou Idoso: '))
print(classificacao_pessoa_por_idade(idade))