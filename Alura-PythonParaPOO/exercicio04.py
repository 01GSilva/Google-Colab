class Livro:
    livros = []

    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo.title()
        self._autor = autor.title()
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        Livro.livros.append(self)

    def __str__(self):
        return f'Título: {self._titulo} - Autor: {self._autor} - Ano de publicação: {self._ano_publicacao}'
    
    def emprestar(self):
        self._disponivel = False

    @classmethod
    def verificar_disponibilidade(cls, ano):
        for livro in cls.livros:
            if livro._ano_publicacao == ano:
                print(f'{livro._titulo}')

    @classmethod
    def listar_livros(cls):
        print(f'{'Título'.ljust(27)} | {'Autor'.ljust(27)} | {'Ano de Publicação'.ljust(27)} | {'Disponivel'}')
        for livro in cls.livros:
            if livro._disponivel == True:
                status = '☑'
            else:
                status = '☐'
            print(f'{livro._titulo.ljust(27)} | {livro._autor.ljust(27)} | {str(livro._ano_publicacao).ljust(27)} | {status}')


livro1 = Livro('senhor dos aneis', 'Tolkien', 1900)
livro2 = Livro('As cronicas de gelo e fogo', 'George martin', 1990)

Livro.listar_livros()