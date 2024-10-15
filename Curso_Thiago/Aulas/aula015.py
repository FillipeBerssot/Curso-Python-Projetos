# Herança de classe:
#   Forma Simples:
class Mamifero:
    def _init_(self) -> None:
        self.pelos = True
        self.glandulas_mamarias = 'grandula produtora de leite'
        self.sistema_nervoso = ['cérebro', 'medúla espinhal']
        self.respiracao = 'pulmonar'
        self.sistema_circulatorio = ['fechada', 'dupla', 'completa', 'coracao de 4 cavidades']
        self.sistema_excretor = dict(rins=2)
        self.reproducao = 'sexuada'
        self.dentes = 'diferenciados'
        self.diafragma = 'membrana muscular que separa o tórax'

    @staticmethod
    def respirar():
        return 'Executando respiração pulmonar'
    
class Voar:
    def _init_(self) -> None:
        self.capacidade_de_voar = True
    
class Sonar:
    capacidade_de_ver_no_escuro = True


class Pessoa(Mamifero):
    ...

class Cachorro(Mamifero):
    ...

class Baleia(Mamifero):
    ...

class Morcego(Mamifero, Voar, Sonar):
    ...

felipe = Pessoa()
castiel = Cachorro()
mobi_dick = Baleia()
batman = Morcego()

#   Forma 2:
class Mamifero:
    def _init_(self, tipo_de_ambiente) -> None:
        self.pelos = True
        self.glandulas_mamarias = 'grandula produtora de leite'
        self.sistema_nervoso = ['cérebro', 'medúla espinhal']
        self.respiracao = 'pulmonar'
        self.sistema_circulatorio = ['fechada', 'dupla', 'completa', 'coracao de 4 cavidades']
        self.sistema_excretor = dict(rins=2)
        self.reproducao = 'sexuada'
        self.dentes = 'diferenciados'
        self.diafragma = 'membrana muscular que separa o tórax'
        self.tipo_de_ambiente = tipo_de_ambiente

    @staticmethod
    def respirar():
        return 'Executando respiração pulmonar'
    

class Cachorro(Mamifero):
    ...
class Baleia(Mamifero):
    ...

castiel = Cachorro(tipo_de_ambiente='terrestre')
mobi_dick = Baleia(tipo_de_ambiente='aquatico')

# Forma 3
class Mamifero:
    
    def _init_(self, tipo_de_ambiente) -> None:
        self.pelos = True
        self.glandulas_mamarias = 'grandula produtora de leite'
        self.sistema_nervoso = ['cérebro', 'medúla espinhal']
        self.respiracao = 'pulmonar'
        self.sistema_circulatorio = ['fechada', 'dupla', 'completa', 'coracao de 4 cavidades']
        self.sistema_excretor = dict(rins=2)
        self.reproducao = 'sexuada'
        self.dentes = 'diferenciados'
        self.diafragma = 'membrana muscular que separa o tórax'
        self.tipo_de_ambiente = tipo_de_ambiente

    @staticmethod
    def respirar():
        return 'Executando respiração pulmonar'
    

class Cachorro(Mamifero):
    late = True
    abana_o_rabo = True

castiel = Cachorro(tipo_de_ambiente='terrestre')

# Forma 4
class Mamifero:
    
    pelos = True
    glandulas_mamarias = 'grandula produtora de leite'
    sistema_nervoso = ['cérebro', 'medúla espinhal']
    respiracao = 'pulmonar'
    sistema_circulatorio = ['fechada', 'dupla', 'completa', 'coracao de 4 cavidades']
    sistema_excretor = dict(rins=2)
    reproducao = 'sexuada'
    dentes = 'diferenciados'
    diafragma = 'membrana muscular que separa o tórax'

    def _init_(self, tipo_de_ambiente, tipo_de_locomocao) -> None:
        self.tipo_de_ambiente = tipo_de_ambiente
        self.tipo_de_locomocao = tipo_de_locomocao

    @staticmethod
    def respirar():
        return 'Executando respiração pulmonar'


class Cachorro(Mamifero):
    
    def _init_(self, tipo_de_ambiente, tipo_de_locomocao) -> None:
        super()._init_(
            tipo_de_ambiente=tipo_de_ambiente, 
            tipo_de_locomocao=tipo_de_locomocao
        )


class Baleia(Mamifero):
    
    def _init_(self, tipo_de_ambiente, tipo_de_locomocao) -> None:
        super()._init_(
            tipo_de_ambiente=tipo_de_ambiente, 
            tipo_de_locomocao=tipo_de_locomocao
        )

castiel = Cachorro(tipo_de_ambiente='terrestre', tipo_de_locomocao='quadrupede')
mobi_dick = Baleia(tipo_de_ambiente='aquático', tipo_de_locomocao='natatória')

print(castiel.tipo_de_ambiente)
print(mobi_dick.tipo_de_ambiente)
print(castiel.tipo_de_locomocao)
print(mobi_dick.tipo_de_locomocao)
print(castiel.sistema_nervoso)
print(mobi_dick.sistema_nervoso)

# Forma 5

class Mamifero:
    
    pelos = True
    glandulas_mamarias = 'grandula produtora de leite'
    sistema_nervoso = ['cérebro', 'medúla espinhal']
    respiracao = 'pulmonar'
    sistema_circulatorio = ['fechada', 'dupla', 'completa', 'coracao de 4 cavidades']
    sistema_excretor = dict(rins=2)
    reproducao = 'sexuada'
    dentes = 'diferenciados'
    diafragma = 'membrana muscular que separa o tórax'

    def _init_(self, tipo_de_ambiente, tipo_de_locomocao) -> None:
        self.tipo_de_ambiente = tipo_de_ambiente
        self.tipo_de_locomocao = tipo_de_locomocao

    @staticmethod
    def respirar():
        return 'Executando respiração pulmonar'
    

class Mergulhar:
    def _init_(self, tempo_de_mergulho_em_minutos):
        self.tempo_de_mergulho_em_minutos = tempo_de_mergulho_em_minutos


class Cachorro(Mamifero):
    def _init_(self, tipo_de_ambiente, tipo_de_locomocao) -> None:
        super()._init_(
            tipo_de_ambiente=tipo_de_ambiente, 
            tipo_de_locomocao=tipo_de_locomocao
        )


class Baleia(Mamifero, Mergulhar):
    
    def _init_(self, tipo_de_ambiente, tipo_de_locomocao) -> None:
        super()._init_(
            tipo_de_ambiente=tipo_de_ambiente, 
            tipo_de_locomocao=tipo_de_locomocao
        )
        Mergulhar._init_(
            self,
            tempo_de_mergulho_em_minutos = 30
        )
        self.tamanho_da_cauda = 50
        
    @staticmethod
    def comer_krill():
        return 'Comendo Krill'


castiel = Cachorro(tipo_de_ambiente='terrestre', tipo_de_locomocao='quadrupede')
mobi_dick = Baleia(tipo_de_ambiente='aquático', tipo_de_locomocao='natatória')


print(mobi_dick.tipo_de_locomocao)
print(mobi_dick.tempo_de_mergulho_em_minutos)
print(mobi_dick.comer_krill())