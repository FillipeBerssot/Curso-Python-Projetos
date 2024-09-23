# 11- Solicite ao usuário que insira um número e imprima a raiz cúbica dele. Com no máximo 3 casas após a virgula:

numero01 = float(input("Insira aqui um número: "))
raiz_cubica = numero01 ** (1/3)
arredondamento_raiz_cubica = round(raiz_cubica, 3)
print(f"A raiz cubica do numero inserido com no maximo 3 casas após a virgula é: {arredondamento_raiz_cubica}")