# LOOPS : WHILE E FOR

# Tradução de WHILE é enquanto. Enquanto alguma situação não ser atingida fique repetindo.

# Exemplo 01 - WHILE   CUIDADO :

# i = 1

# while i < 10:                                             # Se não houver alteração na variavel o WHILE ficara rodando ate consumir toda memoria do computador ate dar erro !!!
#   print(i)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# Exemplo 02 - WHILE:

# i = 1
# while i < 10:
#   print(i)
#   i += 1                                                  # OU mesma coisa que ( i = i + 1 )

# print("Terminou")
# print(i)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

# FOR : Tradução literal = PARA
#Exemplo 01 - FOR:

# criancas = ["Manu", "Vini", "Selina"]

# for item in criancas:                                      # Imprimir cada iten separado que esteja dentro da lista especifica.
#    print(item)

# Exemplo 02 - FOR:

# canal = "Refatorando"

# for letra in canal:                                        # Imprimir cada letra dentro do valor canal = "Refatorando", (cada letra = um indice)
#   print(letra)

# Exemplo 03 - FOR:

# for index in range(6,20,2):                                # Range pode receber 3 parametros (Inicio, fim e de quanto quer pular, fim e o parametro obrigatorio.)
#   print(index)                                             # Valores

# Exemplo 04 - FOR:

# criancas = ["Manu", "Vini", "Selina"]
#              0       1        2

# for index in range(len(criancas)):                         # Imprimir o tamanho da lista, indice
#   print(criancas[index], index)                            # indice de cada valor dentro da lista especifica

# Exemplo 05 - FOR:

# for index in range(5):
#   if index == 0:                                           # Se o indice for igual a 0
#       print("primeira linha")
#   else:
#       print(f"outras linhas {index}")


# MATRIX:                                                    # Listas dentro de Listas , varias linhas e varias colunas:

#matrix_numeros = [
#    [1,2,3],
#    [4,5,6],
#    [7,8,9],
#    [0],
#]

#for linha in matrix_numeros:                                # Dentro dessa matrix de numero, gere um loop (for) para cada linha
#   print(linha)
#    print("------")                                         # mostrar em cada linha que ele entra
#    for coluna in linha:                                    # For alinhado = for dentro de for
#        print(coluna)