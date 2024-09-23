# Ex.057 - Faça um programa que leia o sexo de uma pessoa, mas so aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto:

sexo = input('Digite aqui o sexo de uma pessoa [M / F]: ').strip().upper()[0]

while sexo not in 'MmFf':
    print('Dados invalidos. Por favor digite o sexo com [M] para masculino e [F] para feminino. Tente Novamente:')
    sexo = input('Digite aqui novamente o sexo de uma pessoa: ').strip().upper()[0]
    
print(f'Sexo [{sexo}] registrado com sucesso.')