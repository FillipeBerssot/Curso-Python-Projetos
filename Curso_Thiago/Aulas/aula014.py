class Carro:
    marca = 'BMW'

    def _init_(self, cor, nome, valor, modelo, placa, adicionais):
        self.cor = cor
        self.nome = nome
        self.valor = valor
        self.modelo = modelo
        self.placa = placa
        self.adicionais = adicionais

    @staticmethod
    def acelerar_carro():
        print('Estou acelerando o carro.')
        
    @staticmethod
    def frear():
        print('Estou freando o carro.')

    def ligar_carro(self, chave):
        if chave:
            print(f'Estou ligando o carro, do modelo {self.modelo}')
        else:
            print('Não colocou a chave')

    def _repr_(self):
        return f'Carro do modelo: {self.modelo}, da cor{self.cor}, do valor de: {self.valor}'
    
    def _str_(self):
        return f'Carro da cor: {self.cor}'
    
    def _eq_(self, value: object) -> bool:
        return self.valor == value.valor and self.cor == value.cor
    
    def _lt_(self, value: object) -> bool:
        return self.valor < value.valor
    
    def _le_(self, value: object) -> bool:
        return self.valor <= value.valor
    
    def _gt_(self, value: object) -> bool:
        return self.valor > value.valor
    
    def _ge_(self, value: object) -> bool:
        return self.valor >= value.valor
    
    def _add_(self, value):
        return self.valor + value.valor
    
    def _len_(self):
        return len(self.nome)
    
    def _getitem_(self, chave):
        return self.adicionais[chave]
    
    def _setitem_(self, chave, valor):
        self.adicionais[chave] = valor
    
# Adicionais
adicionais = {
    'freio_abs': True,
    'ar_condicionado': True,
    'roda': 'liga_leve',
    'banco': 'couro',
    'quilometragem': 0
}

# Objeto
meu_carro = Carro(
    cor='prata',
    nome='Tucson', 
    valor=50000, 
    modelo=2024, 
    placa='NGT12',
    adicionais = adicionais
)
meu_carro_2 = Carro(
    cor='amarelo', 
    nome='Pajero', 
    valor=50000, 
    modelo=2024,
    placa='NGT12',
    adicionais = adicionais
)

# Dessa forma chamo o _repr_
print(repr(meu_carro))

# Dessa forma chamo o _str_
print(meu_carro)

# Dessa forma chamo o _eq_ (Comparador de objetos da mesma Instância)
print(meu_carro == meu_carro_2)

# lt, le, gt, ge
print(meu_carro < meu_carro_2)
print(meu_carro <= meu_carro_2)
print(meu_carro > meu_carro_2)
print(meu_carro >= meu_carro_2)

# Utilizando o _add_
preco_total = meu_carro + meu_carro_2
print(preco_total)

# Utilizando o _len_
print(len(meu_carro_2))

# Utilizando o _getitem_
print(meu_carro['banco'])

# Utilizando o _setitem_
meu_carro['teto_solar'] = 'Adicionei Teto Solar'
print(meu_carro['teto_solar'])


# Eu quero que vcs criem uma classe Pessoa, Cidade e pesquisem como utilizar o getattr e o setattr métodos dunder methods