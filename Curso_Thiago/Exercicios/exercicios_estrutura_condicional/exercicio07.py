#Ex.07- Escreva um programa que pergunte a velocidade do carro de um usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado. 
#Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.

# multa = 5
velocidade = float(input("Digite a velocidade em que estava no seu carro: "))

if velocidade > 80:
    excesso_velocidade = velocidade - 80
    multa_total = excesso_velocidade * 5
    print(f"Voçê ultrapassou o limite de velocidade de 80 km/h, sua velocidade foi de {excesso_velocidade} km/h acima do permitido, o valor da sua multa é de R$ {multa_total}")
else:
    print(f"Voçê não ultrapassou o limite de velocidade permitido, não haverá multas.")
