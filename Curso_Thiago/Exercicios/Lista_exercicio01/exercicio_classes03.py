# Exercício:
# Crie uma classe Personagem com os atributos nome, vida e ataque. 
# A classe deve ter um método atacar que recebe outro personagem e diminui a vida dele de acordo com o ataque.
# Depois, crie subclasses Guerreiro e Mago, cada uma com características diferentes para o ataque. 
# Crie uma simulação de batalha onde um guerreiro e um mago atacam um ao outro até que um dos dois tenha vida zero.

# import random

# class Personagem:
#     raca = 'Humano'

#     def __init__(self, nome, vida, ataque, defesa):
#         self.nome = nome
#         self.vida = vida
#         self.ataque = ataque
#         self.defesa = defesa

#     def atacar(self, outro_personagem):
#         dano = self.ataque - outro_personagem.defesa
#         dano = max(dano, 0)
#         outro_personagem.vida -= dano
#         print(f'{self.nome} (raça: {self.raca}) atacou {outro_personagem.nome} (raça: {self.raca}) causando {dano} de dano!')
#         print(f'Vida restante de {outro_personagem.nome}: {outro_personagem.vida}')
#         print(f'Vida restante de {self.nome}: {self.vida}\n')
#         return outro_personagem.vida <= 0 

# class Guerreiro(Personagem):
#     def __init__(self):
#         super().__init__(
#             nome = 'Aristeu o Guerreiro',
#             vida = 120,
#             ataque = 10,
#             defesa = 15
#         )

#     def usar_poder(self):
#         chance = random.random()
#         if chance > 0.7:
#             print(f'{self.nome} usou o poder ESCUDO SUPREMO, reduzindo o dano recebido!')
#             self.defesa += 10 

# class Mago(Personagem):
#     def __init__(self):
#         super().__init__(
#             nome = 'Lucifer o Mago',
#             vida = 100,
#             ataque = 20,
#             defesa = 5
#         )

#     def usar_poder(self):
#         chance = random.random()
#         if chance > 0.7:
#             print(f'{self.nome} usou o poder BOLA DE FOGO, causando dano extra!')
#             self.ataque += 10


# guerreiro = Guerreiro()
# mago = Mago()


# while guerreiro.vida > 0 and mago.vida > 0:
#     guerreiro.usar_poder()
#     if guerreiro.atacar(mago):
#         print(f'{mago.nome} foi derrotado!')
#         break

#     mago.usar_poder()
#     if mago.atacar(guerreiro):
#         print(f'{guerreiro.nome} foi derrotado!')
#         break

#     guerreiro.defesa = 15 
#     mago.ataque = 20 

import random

class Personagem:
    raca = 'Humano'

    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, outro_personagem):
        dano = self.ataque - outro_personagem.defesa
        dano = max(dano, 0)
        outro_personagem.vida -= dano

        if self.classe == 'guerreiro':
            print(f'{self.nome} 💂 atacou  ⚔️ {outro_personagem.nome} 🧙‍♂️ causando {dano} de dano! 🤕')
        elif self.classe == 'mago':
            print(f'{self.nome} 🧙‍♂️ atacou  🪄  {outro_personagem.nome} 💂 causando {dano} de dano! 🤕')
            

        print(f'Vida restante de {outro_personagem.nome}: {outro_personagem.vida}')
        print(f'Vida restante de {self.nome}: {self.vida}\n')
        
class Guerreiro(Personagem):
    def __init__(self):
        super().__init__(
            nome = 'Aquiles',
            vida = 120,
            ataque = 10,
            defesa = 15
        )
        self.classe = 'guerreiro'

    def usar_poder(self):
        chance = random.random()
        if chance > 0.7:
            print(f'{self.nome} usou o poder 🛡️ ESCUDO SUPREMO 🛡️, reduzindo o dano recebido!')
            self.defesa += 10 

class Mago(Personagem):
    def __init__(self):
        super().__init__(
            nome = 'Gandalf o Mago',
            vida = 100,
            ataque = 20,
            defesa = 5
        )
        self.classe = 'mago'

    def usar_poder(self):
        chance = random.random()
        if chance > 0.7:
            print(f'{self.nome} usou o poder 🔥 BOLA DE FOGO 🔥, causando dano extra!')
            self.ataque += 10

class Combate:

    def __init__(self):
        self.guerreiro = Guerreiro()
        self.mago = Mago()

    def batalhar(self):
        self.guerreiro.usar_poder()
        self.guerreiro.atacar(self.mago)

        if self.mago.vida <= 0:
            print(f'☠️⚰️🪦{self.mago.nome} foi derrotado!🪦⚰️☠️')
            return

        self.mago.usar_poder()
        self.mago.atacar(self.guerreiro)
        if self.guerreiro.vida <= 0:
            print(f'☠️⚰️🪦 {self.guerreiro.nome} foi derrotado!🪦⚰️☠️')
        
    def restaurar_skills(self, mago_ataque, guerreiro_defesa):
        self.mago.ataque = mago_ataque
        self.guerreiro.defesa = guerreiro_defesa


info_combate = Combate()
while True:

    info_combate.batalhar()
    info_combate.restaurar_skills(mago_ataque=20, guerreiro_defesa=15)
 
    if info_combate.guerreiro.vida <= 0 or info_combate.mago.vida <= 0:
        break
    