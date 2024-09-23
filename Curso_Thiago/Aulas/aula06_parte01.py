# LISTA E FUNÇÕES PARA MANIPULAR LISTA: 
# Colections = coleção de dados
# Varias variaveis do mesmo tipo (int, float, bool, str) em uma lista

#Para criar uma lista deve colocar os valores entre COLCHETES " [] " e separados por virgulas.

#Lista "familia":
familia = ["pai", "mae", "filho", "filha"]
#print(familia)


#lista = retorna indice, que sempre começa com 0:
familia = ["pai", "mae", "filho", "filha"]
#            0      1       2        3
#print(familia[2])                                          #Obter o indicie = " [] " COLCHETES 


#lista de trás para frente = retrorna indice de tras para frente, começa com -1:
familia = ["pai", "mae", "filho", "filha"]
#           -4     -3      -2       -1
#print(familia[-4])


#Obter parte especifica na lista com o indice = usar entre o COLCHETES " [] " , indice : indice ( [0:3] )
familia = ["pai", "mae", "filho", "filha"]
#print (familia[0:3])


#Alterar o valor no indice = acessar a lista ( familia, alterar o indice escolhido ( indice 2 = "filho" ) ) 
#print(familia)
familia = ["pai", "mae", "filho", "filha"]
familia[2] = "Filho Jr."
#print(familia)


#Adicionar uma outra lista na lista ja definida, ou criar uma lista para adicionar a outra lista ja definida = .extend = (  familia.extend(["cahorro", "gato"])  )
familia = ["pai", "mae", "filho", "filha"]
familia.extend(["gato", "cachorro"])
#print(familia)
#Adicionar somente 1 valor na lista ja definida = .append = (  familia.append ("avó")  )
familia.append("avó")
#print(familia)
#Adicionar um valor na lista ja definida mas inserindo em um local especifico = .insert = (  familia.insert(6, "avô")  ) 
familia.insert(6, "avô")
#print(familia)

#Remover valor da lista definida (remove o ultimo valor) = .pop() = ( familia.pop() )
familia.pop()
#print(familia)
#Remover um valor especifico da lista definida = .remove = ( familia.remove("avô") )
familia.remove("avô")
#print(familia)
#Remover todos os indices da lista definida = .clear = ( familia.clear() )
#familia.clear()
#print(familia)

# Retornar o valor do indice especifico = .index = ( ( familia.index() ) )
familia.index("gato")
#print(familia.index("mae"))

#Contar quantos valores de um indice especifico tem dentro da lista definida = .count = ( ( familia.count() ) )
familia.count("gato")
#print(familia.count("gato"))

#Podemos fazer listas com inteiros:
#Para ordernar a lista em ordem CRESCENTE = .sort() = ( ( idade_familia.sort() ) )      (podendo ser utilizado em INT e STRING)
idade_familia = [35, 33, 12, 10, 2, 3]
idade_familia.sort()
print(idade_familia)
#Para inverter a lista definida = .reverse() = ( ( idade_familia.reverse() ) )          (podendo utilizar em INT e STRING)
idade_familia.reverse()
print(idade_familia)


#Para fazer uma copia de uma lista, coleção = .copy() = ( ( familia.copy() ) )           (se nao utilizar, .copy() as variavies feitas serao alteradas juntos com a original e vice versa!!!)
#familia2 = familia                                                                        (dessa forma nao sera realmente uma copia, sera uma referencia)
#print(familia)
familia2 = familia.copy()
#print(familia2)



