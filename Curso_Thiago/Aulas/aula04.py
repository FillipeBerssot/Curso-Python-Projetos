minha_string = "qualquer texto"
minha_string2 = "QUALQUER TEXTO"
nome = "Thiago"

print(len(nome))
print(nome[0:1])
print(minha_string)
print(minha_string.upper())                                                #.UPPER serve para deixar minha String em Maiusculo
print(minha_string.capitalize())                                           #.CAPITALIZE serve para deixar a primeira letra Maiuscula
print(minha_string2.lower())                                               #.LOWER serve para deixar minha String em Minusculo
print(minha_string2.islower())                                             #.islower ou .isupper serve para saber se a String esta maiusculo ou minusculo
print(minha_string.strip())                                                #.strip serve para remover os espaços do começo e do final da String
print(minha_string.replace("qualquer", "meu", 2))                          #.replace serve para trocar alguma palavra ou letra na String por outra. Caso queira mudar somente 1 ou 2, etc, coloque a quantiade na frente do novo numero.
print(len(minha_string))                                                   #len serve para saber quantas palavras tem na minha String (sempre contando a partir do 0)
print(minha_string[4:8])                                                   #para usar somente os numeros selecionado, colocar entre [] e colocar qual numero correponde, contando a partir do 0 e para o contrario: contando a partir do -1
print(nome.index("hia"))                                                   #.index serve para retornar a posição da letra na String 


x = "texto" in nome                                                         #Mostrar se o que foi digitado está ou não dentro da variavel ("texto" está dentro da variavel minha_string, retorna True, caso contrario retorna False)
print(x)

minha_string3 = """linha 1                                                 
linha 2
linha 3"""                                                                  #Colocar 3 aspas """ texto """, fará quebra de linha
print(minha_string3)
minha_string4 = "linha 1, \nlinha 2, \nlinha 3. \"linha 4\" "               #Colocar \n tambem faz a quebra de linha, colocar \ vira caractere de escape, podendo assim adicionar caracteres sem sair da String (\"" adiciona as aspas na String) 
print(minha_string4)                                                                

minha_string5 = 'linha 1, "linha 2" '