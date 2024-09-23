# Ex.053- Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços:
# Ex: APOS A SOPA
# Ex: A SACADA DA CASA
# Ex: A TORRE DA DERROTA
# Ex: O LOBO AMA O BOLO


frase_qualquer = input('Digite aqui uma frase qualquer e descubra se ela é ou não um palíndromo: ').upper(). replace(' ','')

frase_ao_contrario = frase_qualquer[::-1].upper().replace(' ', '')

print(f'A frase {frase_qualquer} invertida é = {frase_ao_contrario}.')

if frase_qualquer == frase_ao_contrario:
    print(f'Por isso a frase = {frase_qualquer}, é um PALÍNDROMO.')
else: 
    print(f'Por isso a frase = {frase_qualquer}, não é um PALÍNDROMO.')

# Outra forma usando o FOR:
frase = str(input('\nDigite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palíndromo.')
else:
    print('A frase digitada não é um palíndromo.')
