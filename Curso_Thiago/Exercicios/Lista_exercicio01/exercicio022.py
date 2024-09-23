# Ex.022- Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16:

while True:
    while True:
        num = int(input("digite um numero para obter o fatorial: "))
        if num <= 16 and num > 0:
            print("valido")
            break
        else:
            print("numero invalido")
            num = int(input("digite um numero para obter o fatorial: "))
    lista = list(range(1, num+1))
    produto = 1
    for numero in lista:
        produto = numero * produto
    print(produto)
    print("deseja fazer a operação novamente? ")
    print("se sim digite 1")
    print("se não digite qualquer outra tecla")
    num1 = input("digite aqui: ")
    if num1 != "1":
        print("fechando")
        break