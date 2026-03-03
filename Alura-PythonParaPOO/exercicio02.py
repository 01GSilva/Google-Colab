class Carro:
    def __init__(self, modelo='', cor='', ano=0):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
    
    def __str__(self):
        return f'{self.modelo} - {self.cor} - {self.ano}'

voyage = Carro('Voyage GL', 'Azul prateado', 1989)
print(voyage)

class Restaurante:
    def __init__(self, nome='', categoria=''):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
    
    def __str__(self):
        return f'{self.nome} - {self.categoria}'
    
Cara = Restaurante('Restaurante do Cará', 'Variado')
print(Cara)

class Cliente:
    clientes=[]
    
    def __init__(self, nome='', pedido='', mesa=0, valor=0.00):
        self.nome = nome
        self.pedido = pedido
        self.mesa = mesa
        self.valor = valor
        Cliente.clientes.append(self)

    def __str__(self):
        return f'{self.nome} - {self.pedido} -Mesa {self.mesa} - R$ {self.valor}'
    
    def listar_clientes():
        for cliente in Cliente.clientes:
            print(cliente)

cliente1 = Cliente('João', 'Parmegiana', 3, 25.00)
cliente2 = Cliente('Jonas','Sushi', 7, 30.00)
cliente3 = Cliente('Marcos','Frango', 5, 20.00)

Cliente.listar_clientes()