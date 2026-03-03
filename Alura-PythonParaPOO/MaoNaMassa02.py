class Pessoa:

    pessoas = []

    def __init__(self, nome='', idade=0, profissao=''):
        self._nome = nome.title()
        self._idade = idade
        self._profissao = profissao.title()
        Pessoa.pessoas.append(self)

    def __str__(self):
        return f'{self._nome} / {self._idade} / {self._profissao}'
    
    def aniversario(self):
        self._idade = self._idade + 1

    def saudacao(self):
        print(f'Bem vindo {self._profissao}.')
    
    @classmethod
    def listar_pessoas(cls):
        print(f'{'Nome'.ljust(25)} / {'idade'} / {'Profissão'.rjust(22)}')
        for pessoa in cls.pessoas:
            print(f'{pessoa._nome.ljust(25)} / {pessoa._idade} / {pessoa._profissao.rjust(25)}')


    
Jonas = Pessoa('Jonas', 25, 'Torneiro')
Matheus = Pessoa('Matheus', 29, 'Caminhoneiro')
Guilherme = Pessoa('guilherme', 30, 'topógrafo')

Jonas.saudacao()