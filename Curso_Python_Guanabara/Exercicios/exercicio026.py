# Desafio 026- Faça um programa que leia uma frase pelo teclado e mostre:
# -> Quantas vezes aparece a letra " A ":
# -> Em que posição ela aparece a primeira vez:
# -> Em que posição ela aparece a ultima vez:

frase = str(input("Digite aqui uma frase: ")).lower().strip()


letra_a = frase.count('a')
print(f'A letra "a" apareceu {letra_a} vezes na frase digitada.')

posicao01 = frase.find('a')
print(f'A letra "a" aparece a primeira vez na posição: {posicao01}')

posicao02 = frase.rfind('a')
print(f'A letra "a" aparece pela ultima vez na posição: {posicao02}')