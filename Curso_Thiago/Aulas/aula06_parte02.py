# TUPLES:
# Tuples é imutavel (nao posso alterar , adicionar, remover valores dentro de um Tuple)

#Para criar um Tuple deve-se colocar entre parenteses "  ( )  " e os valores separados por virgula.

coordenadas = (-49,-36)
print(coordenadas)


# DICIONARIO:
# Dicionario e aberto por CHAVES , dicionario trabalha com chaves e valor ( [ " " ] ) , pode haver alterações , nao tem index
# Ex: 

pessoa = {
    "nome": "Thiago",
    "idade": 30,
    "cidade": "Goiania"
}

print(pessoa)

print(pessoa["nome"])
print(pessoa.get("nome"))