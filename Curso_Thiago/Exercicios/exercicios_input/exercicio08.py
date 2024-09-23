# 08- Solicite ao usuário que insira uma string e imprima ela com todas as vogais substituídas por "*": 

texto = input("Digite um texto qualquer: ")
texto = texto.lower()

texto_sem_vogal_a = texto.replace("a", "*")

texto_sem_vogal_e = texto_sem_vogal_a.replace ("e", "*")

texto_sem_vogal_i = texto_sem_vogal_e.replace ("i", "*")
texto_sem_vogal_o = texto_sem_vogal_i.replace ("o", "*")
texto_sem_vogal_u = texto_sem_vogal_o.replace ("u", "*")

resultado = texto_sem_vogal_u
print(resultado)

print(f'O seu texto digitado caso tiver as vogais "a", "e", "i", "o", "u", serão trocadas pelo " * " é o resultado será: {resultado}')


#.replace usado para fazer a troca de caracteres na string, no caso como sao varias a serem trocadas, fiz um .replace para cada uma delas.