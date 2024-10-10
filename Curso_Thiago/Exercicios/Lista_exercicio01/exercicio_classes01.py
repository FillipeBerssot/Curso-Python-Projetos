# Crie uma classe Pessoa, pesquisem como utilizar o getattr e o setattr métodos dunder methods:

# Classe Pessoa = FEITO
class Pessoa:
    nacionalidade = 'Brasileiro'
    salario_minimo = 1412
    imc_abaixo_normal = 18.5
    imc_normal_minimo = 18.6
    imc_normal_maximo = 24.9
    imc_sobrepeso_minimo = 25.0
    imc_sobrepeso_maximo = 29.9
    imc_obesidade = 30.0

    def __init__(self, nome, sobrenome, altura, peso, idade, sexo, cpf, endereco, profissao, salario):
        self.nome = nome
        self.sobrenome = sobrenome
        self.altura = altura
        self.peso = peso
        self.idade = idade
        self.sexo = sexo
        self.cpf = cpf
        self.endereco = endereco
        self.profissao = profissao
        self.salario = salario

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'
    
    def verificar_imc(self):
        imc = self.peso / (self.altura ** 2)
        imc = round(imc, 2)
        if imc <= Pessoa.imc_abaixo_normal:
            return f'{imc}, por tanto {self.nome} está Abaixo do Normal.'
        elif Pessoa.imc_normal_minimo <= imc <= Pessoa.imc_normal_maximo:
            return f'{imc}, por tanto {self.nome} está com IMC Normal.'
        elif Pessoa.imc_sobrepeso_minimo <= imc <= Pessoa.imc_sobrepeso_maximo:
            return f'{imc}, por tanto {self.nome} está com Sobrepeso.'
        elif imc >= Pessoa.imc_obesidade:
            return f'{imc}, por tanto {self.nome} está com Obesidade.'
    
    def maior_de_idade(self):
        if self.idade >= 18:
            return f'{self.nome} é maior de idade.'
        else:
            return f'{self.nome} não é maior de idade.'
        
    def maior_que_salario_minimo(self):
        if self.salario == 0:
            return f'{self.nome} não recebe nenhum salário.'
        elif self.salario > Pessoa.salario_minimo:
            return f'o salário de {self.nome} é maior do que um salário minimo.'
        else:
            return f'o salário de {self.nome} é menor do que um salário minimo.'

    # Dunder STRING: utilizar str (strings) 
    def __str__(self):
        return f'As informações da pessoa cadastrada: ' \
        f'\nNome Completo: {self.nome_completo()}.' \
        f'\nAltura: {self.altura:.2f} metros' \
        f'\nPeso: {self.peso:.2f} kgs.' \
        f'\nIMC: {self.verificar_imc()}' \
        f'\nIdade: {self.idade} anos, por tanto {self.maior_de_idade()}' \
        f'\nSexo: {self.sexo}' \
        f'\nCPF: {self.cpf}' \
        f'\nEndereço: {self.endereco}' \
        f'\nProfissão: {self.profissao}.' \
        f'\nSalário: {self.salario} reais, por tanto {self.maior_que_salario_minimo()}'
        
    # Dunder REPRESENTATION: representar precisa do objeto
    def __repr__(self):
        return f'Apresentação do (nome = "{self.nome}", sobrenome = "{self.sobrenome}", idade = "{self.idade}")\n'
        
    # Dunder EQUAL: Operador == (igualdade) 
    def __eq__(self, outra_pessoa):
        return self.idade == outra_pessoa.idade

    # Dunder LESS THAN: Operador < (menor que) 
    def __lt__(self, outra_pessoa):
        return self.idade < outra_pessoa.idade 
    
    # Dunder LESST THAN OR EQUAL: Operador <= (menor ou igual) 
    def __le__(self, outra_pessoa):
        return self.idade <= outra_pessoa.idade 
                
    # Dunder GREATER THAN: Operador > (maior que) 
    def __gt__(self, outra_pessoa):
        return self.idade > outra_pessoa.idade
    
    # Dunder GREATER THAN OR EQUAL: Operador == (maior ou igual) 
    def __ge__(self, outra_pessoa):
        return self.idade >= outra_pessoa.idade 

pessoa_01 = Pessoa(
    nome = 'Fillipe',
    sobrenome = 'Berssot',
    altura = 1.80,
    peso = 105,
    idade = 29,
    sexo = 'Masculino',
    cpf = '031.784.941-70',
    endereco = 'Rua Golfo de Bengala, Nº 45, João Pessoa, JP.',
    profissao = 'Estudante',
    salario = 0
)

pessoa_02 = Pessoa(
    nome = 'Thiago',
    sobrenome = 'Tancredi',
    altura = 1.80,
    peso = 90,
    idade = 30,
    sexo = 'Indefinido',
    cpf = '000.000.000-00',
    endereco = 'Alto da Glória, Nº 100, Goiânia, GO.',
    profissao = 'Desenvolvedor Senior',
    salario = 20000,
)

pessoa_03 = Pessoa(
    nome = 'Alberdan',
    sobrenome = 'Fernandes',
    altura = 1.70,
    peso = 70,
    idade = 17,
    sexo = 'Feminino',
    cpf = '111.111.111-11',
    endereco = 'Parque Trindade, Nº 32, Goiânia, GO.',
    profissao = 'Estudante',
    salario = 1000
)

print(repr(pessoa_01))
print(pessoa_01)
print(f'A Nacionalidade de {pessoa_01.nome_completo()} é {pessoa_01.nacionalidade}.\n')

print(repr(pessoa_02))
print(pessoa_02)
print(f'A Nacionalidade de {pessoa_02.nome_completo()} é {pessoa_02.nacionalidade}.\n')

print(repr(pessoa_03))
print(pessoa_03)
print(f'A Nacionalidade de {pessoa_03.nome_completo()} é {pessoa_03.nacionalidade}.\n')

print(f'{pessoa_01.nome_completo()} tem a mesma idade que {pessoa_02.nome_completo()}? {pessoa_01 == pessoa_02}')
print(f'{pessoa_01.nome_completo()} é mais jovem que {pessoa_02.nome_completo()}? {pessoa_01 < pessoa_02}')
print(f'{pessoa_01.nome_completo()} é mais velho que {pessoa_02.nome_completo()}? {pessoa_01 > pessoa_02}')

print(f'{pessoa_03.nome_completo()} é mais jovem ou tem a mesma idade que {pessoa_02.nome_completo()}? {pessoa_03 <= pessoa_02}')
print(f'{pessoa_03.nome_completo()} é mais velho ou tem a mesma idade que {pessoa_01.nome_completo()}? {pessoa_03 >= pessoa_01}')