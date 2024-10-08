# *Args
    # Posição
        # Exemplo:

def calcular_imposto(valor, *args):
    total_imposto = 0
    for item in args:
        total_imposto += valor * item
        return total_imposto
    
print(calcular_imposto(1000, 0.275, 0.05, 0.0375, 0.03))

# **Kwargs
    # Chave e valor
        # Exemplo:

def calcular_imposto_trimestral(valor, **kwargs):
    total_imposto = 0
    print(kwargs)
    if 'perc_iss' in kwargs:
        total_imposto += valor * kwargs['perc_iss']
    if 'perc_pis' in kwargs:
        total_imposto += valor * kwargs['perc_pis']
    if 'perc_ir' in kwargs:
        total_imposto += valor * kwargs['perc_ir']
    if 'perc_csll' in kwargs:
        total_imposto += valor * kwargs['perc_csll']
        return total_imposto

print(calcular_imposto_trimestral(1000, perc_iss=0.05, perc_pis=0.03, perc_ir=0.275, perc_csll=0.0375))