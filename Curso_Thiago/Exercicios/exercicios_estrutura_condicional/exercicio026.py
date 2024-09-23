#Ex.26- Fazer um programa que leia a capacidade de um elevador e o peso de 5 pessoas. Informar se o elevador está liberado para subir ou se excedeu a carga máxima:

print("------ A Capacidade maxima do elevador é de 500 kg ------")

kg_pessoa1 = float(input("Qual o peso da primeira pessoa em kgs? "))
kg_pessoa2 = float(input("Qual o peso da segunda pessoa em kgs? "))
kg_pessoa3 = float(input("Qual o peso da terceira pessoa em kgs? "))
kg_pessoa4 = float(input("Qual o peso da quarta pessoa em kgs? "))
kg_pessoa5 = float(input("Qual o peso da quinta pessoa em kgs? "))

#media_kgs = pessoa1 + pessoa2 + pessoa3 + pessoa4 + pessoa5

if kg_pessoa1 <= 100:
    print("Pessoa 1 esta liberada")
else: 
    print("Pessoa 1 nao esta liberada")

if kg_pessoa2 <= 100:
    print("Pessoa 2 esta liberada")
else: 
    print("Pessoa 2 nao esta liberada")

if kg_pessoa3 <= 100:
    print("Pessoa 3 esta liberada")
else: 
    print("Pessoa 3 nao esta liberada")

if kg_pessoa4 <= 100:
    print("Pessoa 4 esta liberada")
else: 
    print("Pessoa 4 nao esta liberada")

if kg_pessoa5 <= 100:
    print("Pessoa 5 esta liberada")
else: 
    print("Pessoa 5 nao esta liberada")                                                         #queria especificar qual a pessoa que esta excedendo o peso total que o elevador suporta

media_kgs = kg_pessoa1 + kg_pessoa2 + kg_pessoa3 + kg_pessoa4 + kg_pessoa5

if media_kgs <= 500:
    print(f"Peso total de {media_kgs} kgs, suportado. Elevador liberado para subir.")
else:
    print(f"Peso total de {media_kgs} kgs, excede o peso total suportado. Elevador não será liberado para subir.")