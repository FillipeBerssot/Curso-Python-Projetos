# Ex. 021- Altere o programa anterior para que ele aceite apenas números entre 0 e 1000:

lista_num = []
num = int(input("digite a quantidade de numeros no conjunto: "))
for i in range(num):
    while True:
        numero = int(input("Digite um número inteiro entre 0 e 1000: "))
        if 0 <= numero <= 1000:
            lista_num.append(numero)
            break
        else:
            print("Número fora do intervalo. Tente novamente.")
'''max = max(lista_num)
min = min(lista_num)
calculo = max + min
print(f"a soma entre o maior: {max} e o menor: {min} é: {calculo}")'''