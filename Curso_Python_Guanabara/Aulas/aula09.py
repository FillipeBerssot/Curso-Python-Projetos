# MANIPULANDO TEXTO (STRING):

# frase = 'Curso em Video Python'

# indice: começa com 0

#FATIAMENTO DE STRING SIMPLES : [ ]

frase = 'Curso em Video Python'

print(frase[9])                     # ---> V 

# FATIAMENTO DE STRING: [9:13]        ---> não conta o ultimo valor

print(frase[9:13])                  # ---> Vide
print(frase[9:21])                  # ---> Video Python

# FATIAMENTO DE STRING: [9:13:2]      ---> pular de 2 em 2      [inicio : fim : pular]

print(frase[9:21:2])                # ---> VdoPto

# FATIAMENTO DE STRING: [:5]

print(frase[:5])                    # ---> Curso

# FATIAMENTO DE STRING: [15:]

print(frase[15:])                   # ---> Python

# FATIAMENTO DE STRING: [9::3]

print(frase[9::3])                  # ---> VePh

# LEN() :            Mostrar quantos caracteres tem.

print(len(frase))                   # ---> 21

# FRASE.COUNT() :           CONTAR QUANTAS VEZES EXISTE A LETRA DEFINIDA.

print(frase.count("o"))             # ---> 1

# FRASE.FIND() :       Encontrar a posição

print(frase.find('deo'))            # ---> 11

# IN FRASE :     existe dentro da variavel.

print('Curso' in frase)             # ---> True

# FRASE.REPLACE() :       SUBSTITUIR

print(frase.replace('Python', 'Android'))       # ---> 'Curso em Video Android'
print(frase.replace('Android', 'Python'))       # ---> 'Curso em Video Python'

# FRASE.TITLE() :    DEIXAR TODAS AS PRIMEIRAS LETRAS DE CADA PALAVRA EM MAIUSCULO

frase2 = 'curso em video em python'
print(frase2.title())                           # ---> Curso Em Video Em Python

# DIVISÃO :
# frase.split() :

print(frase.split())                            # ---> ['Curso', 'em', 'Video', 'Python']

#JUNÇÃO :
# '-'.join(frase) :

print('-'.join(frase))                          # ---> C-u-r-s-o- -e-m- -V-i-d-e-o- -P-y-t-h-o-n

# IMPRIMIR TEXTOS GRANDE DE OUTRA FORMA : 

print("""Welcome! 
Are you completely new to programming?
About why and how to get started with Python.""")
