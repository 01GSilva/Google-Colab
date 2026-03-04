class ContaBancaria:
    def __init__(self, titular='', saldo=0.00):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'Titular: {self._titular} / Saldo: R${self._saldo}'

    def ativar_conta(self):
        self._ativo = True

    def titular(self):
        print(f'Titular: {self._titular}')

class ContaBancaraPythonica:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def ativo(self):
        return self._ativo
    
    def ativar_conta(self):
        self._ativo = True

class ClienteBanco:
    @classmethod
    def criar_conta(cls, titular, saldo_inicial):
        conta = ContaBancaraPythonica(titular, saldo_inicial)
        return conta
    
conta_cliente1 = ClienteBanco.criar_conta("Ana", 2000)
print(f"Conta de {conta_cliente1.titular} criada com saldo inicial de R${conta_cliente1.saldo}")