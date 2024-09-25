# Ex.014 - Faça um programa que consulte a lista de temperaturas de um notebook e verifique se alguma temperatura
# é superior a 80. Utilize a lista de temperaturas:
#  
# temperaturas = [72,75,78,85,77,79]:


def verificar_temperaturas(temperaturas):
    temperaturas_acima_80 = []
    
    for i in temperaturas:
        if i > 80:
            temperaturas_acima_80.append(i)

    if temperaturas_acima_80 == []:
        return('De acordo com a lista inserida, não existe nenhuma temperatura acima de 80º graus.')
    else:
        return f'De acordo com a lista inserida, as temperaturas acima de 80º graus são: {temperaturas_acima_80} graus'
    

temperaturas = [72, 75, 78, 77 ,79]
print(verificar_temperaturas(temperaturas))

temperaturas02 = [72, 75, 78, 77 ,81, 101, 95, 84]
print(verificar_temperaturas(temperaturas02))

