# IF, ELSE STATEMENTS, OPERADORES LOGICOS E COMPARAÇÂO :

# tenho_sede = True

# if tenho_sede:
#    print("Beber agua")

# print("nao fazer nada")

# esta_frio = True

# if esta_frio:
#    print("Vestir Casaco")
# else:
 #   print("Vestir Camiseta")

#---------------------------------------------------------------------------------------

# or :
# tenho_sede = True
# tenho_fome = True

# if tenho_fome or tenho_sede:                          ( or = ou , um ou outro, se os dois tiverem True = True, se so um estiver True = True, so sera negativo se o dois nao atenderem. )
#    print("Vou na cozinha")
# else:
#    print("Vou ficar quieto")


# and :
# tenho_sede = True
# tenho_fome = False

# if tenho_fome and tenho_sede:                          ( and = e , os dois tem que atender  True = True, se um dos dois nao atenderem False , so sera True se o dois atenderem. )                         
#    print("fazer sanduiche e tomar uma coca")
# else:
#    print("nao tenho fome ou nao tenho sede")


# elif = elseif :

# tenho_sede = True
# tenho_fome = False
# estou_em_dieta = True

# if tenho_sede and tenho_fome:                                      
#    print("Fazer sanduiche e coca")
# elif tenho_sede and not (tenho_fome):                               # and not = e nao, nao (tenho_fome), converte a variavel para False
#    if estou_em_dieta:
#        print("Beber agua")                                                  # OPERADORES LOGICOS :
#    else:                                                                    # OR      =>   OU
#        print("Tomar uma coca")                                              # AND     =>   E
# elif not(tenho_sede) and tenho_fome:                                        # NOT()   =>   NEGAÇÃO
#    print("fazer um sanduiche")
# else:
#    print("Ficar quieto")    

#----------------------------------------------------------------------------------------

# OPERADORES DE COMPARAÇÃO :

# ==   ->   ( IGUAL )
# !=   ->   ( DIFERENTE )
# >    ->   ( MAIOR )
# <    ->   ( MENOR )
# >=   ->   ( MAIOR OU IGUAL )
# <=   ->   ( MENOR OU IGUAL )
