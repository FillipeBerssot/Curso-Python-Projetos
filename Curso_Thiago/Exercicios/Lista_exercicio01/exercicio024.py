# Ex. 024- Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível:

num = int(input('digite um numero: '))
divi = []
if num >= 2:
    for i in range(1, num):
        if num % i == 0:
            divi.append(i)
if len(divi) > 2:
    print(f'não é primo porque foi divisivel por: {divi}')
else:
    print('numero primo')
