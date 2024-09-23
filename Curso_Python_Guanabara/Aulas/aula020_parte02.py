# FUNÇÕES  Parte 02:
#      def:

#       Interactive Help:
#           Ajuda Interativa:   help()
def contador(i, f, p):
    """
    Faz uma contagem e mostra na tela.
    i : inicio da contagem
    f : fim da contagem
    p : passo da contagem
    """
    c = i
    while c <= f:
        print(f'{c}, ', end='')
        c += p
    print('FIM!')
    

contador(2, 10, 2)

#       PARAMETROS OPCIONAIS:
def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}')


somar(3, 2, 5)
somar(8, 4)
somar()

#       ESCOPO DE VARIAVEIS:
print('='* 30)
def teste():
    x = 8
    print(f'Na função teste, n vale {n}')                            # LOCAL
    print(f'Na função teste, x vale {x}')


n = 2
print(f'No programa principal, n vale {n}')
teste()                                                              # GLOBAL

#       RETORNO DE VALORES:
#               return :
def somar02(a=0, b=0, c=0):
    s = a + b + c
    return s


r1 = somar02(3, 2, 5)
r2 = somar02(2, 2)
r3 = somar02(6)
print(f'Os resultados foram {r1}, {r2}, {r3}.')

# Exemplo 01:
print('='* 30)
def fatorial(numero=1):
    f = 1
    for c in range(numero, 0, -1):
        f *= c
    return f


f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2}, {f3}.')
n = int(input('Digite um numero: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')

# Exemplo 02:
print('='* 30)
def par_ou_impar(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
    

num = int(input('Digite um numero: '))
if par_ou_impar(num):
    print('É PAR!')
else:
    print('É IMPAR!')
