# Crie uma classe Cidade, pesquisem como utilizar o getattr e o setattr métodos dunder methods:

# Classe Cidade:
class Cidade:
    pais = 'Brasil'
    # Habitantes:
    cidade_pequena = 99000
    cidade_media_minima = 100000
    cidade_media_maxima = 499000
    cidade_grande = 500000

    def __init__(self, **kwargs):
        self.nome = kwargs.get('nome')
        self.populacao = kwargs.get('populacao')
        self.area = kwargs.get('area')
        self.localizacao = kwargs.get('localizacao')
        self. prefeito = kwargs.get('prefeito')
        self.fundacao = kwargs.get('fundacao')
        self.pib = kwargs.get('pib')

    def verificar_tipologia_cidade(self):
        if self.populacao <= Cidade.cidade_pequena:
            return f'{self.nome} tem {self.populacao} habitantes, portanto é considerada uma Cidade Pequena.'
        elif Cidade.cidade_media_minima <= self.populacao <= Cidade.cidade_media_maxima:
            return f'{self.nome} tem {self.populacao} habitantes, portanto é considerada uma Cidade Média.'
        elif self.populacao >= Cidade.cidade_grande:
            return f'{self.nome} tem {self.populacao} habitantes, portanto é considerada uma Cidade Grande.'

    def verificar_localizacao_cidade(self):
        if self.localizacao == 'Nordeste':
            return f'{self.nome} está situada na região Nordeste do {Cidade.pais}.'
        elif self.localizacao == 'Norte':
            return f'{self.nome} está situada na região Norte do {Cidade.pais}.'
        elif self.localizacao == 'Centro-Oeste':
            return f'{self.nome} está situada na região Centro-Oeste do {Cidade.pais}.'
        elif self.localizacao == 'Sudeste':
            return f'{self.nome} está situada na região Sudeste do {Cidade.pais}.'
        elif self.localizacao == 'Sul':
            return f'{self.nome} está situada na região Sul do {Cidade.pais}.'
        
    def verificar_idade_cidade(self):
        idade = 2024 - self.fundacao
        return f'{self.nome} foi fundada em {self.fundacao}, por tanto tem {idade} anos.'
    
    def __str__(self):
        return f'Caracteristicas da Cidade cadastrada: '\
        f'\nNome da cidade: {self.nome}'\
        f'\nPaís em que a cidade está situada: {Cidade.pais}'\
        f'\nPopulação da cidade: {self.populacao} mil habitantes.'\
        f'\nTipologia da cidade de acordo com a população: {self.verificar_tipologia_cidade()}'\
        f'\nÁrea da cidade: {self.area:.1f} km2.'\
        f'\nRegião da cidade: {self.verificar_localizacao_cidade()}'\
        f'\nO Prefeito da cidade no momento é: {self.prefeito}.'\
        f'\nFundação da cidade: {self.verificar_idade_cidade()}'\
        f'\nO PIB da cidade (2023): {self.nome} teve um PIB de {self.pib:.2f} milhões de reais.\n'
    
    # Dunder EQUAL: Operador == (igualdade) 
    def __eq__(self, outra_cidade):
        return self.populacao == outra_cidade.populacao and self.area == outra_cidade.area and self.pib == outra_cidade.pib

    # Dunder LESS THAN: Operador < (menor que) 
    def __lt__(self, outra_cidade):
        return self.idade < outra_cidade.idade 
    
    # Dunder LESST THAN OR EQUAL: Operador <= (menor ou igual) 
    def __le__(self, outra_cidade):
        return self.idade <= outra_cidade.idade 
                
    # Dunder GREATER THAN: Operador > (maior que) 
    def __gt__(self, outra_cidade):
        return self.idade > outra_cidade.idade
    
    # Dunder GREATER THAN OR EQUAL: Operador == (maior ou igual) 
    def __ge__(self, outra_cidade):
        return self.idade >= outra_cidade.idade 


cidade_01 = Cidade(
    nome = 'João Pessoa',
    populacao = 888679,
    area = 211.5,
    localizacao = 'Nordeste',
    prefeito = 'Cícero Lucena',
    fundacao = 1585,
    pib = 22.244284
)
cidade_02 = Cidade(
    nome = 'Goiânia',
    populacao = 1494599,
    area = 728.8,
    localizacao = 'Centro-Oeste',
    prefeito = 'Rogério Cruz',
    fundacao = 1933,
    pib = 59.865990
)

print(cidade_01)
print(cidade_02)

print(f'{cidade_01.nome} tem a mesma população, area, pib que {cidade_02.nome}? {cidade_01 == cidade_02}')
print(f'{cidade_01.nome} tem uma população menor que {cidade_02.nome}? {cidade_01.populacao < cidade_02.populacao}')
print(f'{cidade_01.nome} tem uma área maior que {cidade_02.nome}? {cidade_01.area > cidade_02.area}')

print(f'{cidade_01.nome} tem um PIB maior ou igual a {cidade_02.nome}? {cidade_01.pib >= cidade_02.pib}')
print(f'{cidade_02.nome} tem uma população menor ou igual a {cidade_01.nome}? {cidade_02.populacao <= cidade_01.populacao}')

# getattr:
# O getattr é usado para obter o valor de um atributo de um objeto. Se o atributo não existir, ele pode retornar um valor padrão.
nome = getattr(cidade_01, 'nome')
profissao = getattr(cidade_01,'profissao', 'Não Informado')
print(f'\nAcessando dados da cidade com o getattr. Nome: {nome}. Profissão: {profissao}')

# setattr:
# O setattr é usado para definir ou modificar o valor de um atributo de um objeto de forma dinâmica.
setattr(cidade_02, 'pib', 0)                # Modificar atributo
setattr(cidade_02, 'profissao', 'Ladrão')   # Definir um novo atributo
print(f'Modificando e adicionando atributos com o setattr. PIB: {cidade_02.pib}, Profissão: {cidade_02.profissao}')
