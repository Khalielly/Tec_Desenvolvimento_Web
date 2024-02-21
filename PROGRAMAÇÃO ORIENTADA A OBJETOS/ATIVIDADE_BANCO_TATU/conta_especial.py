from contas import Conta

class Conta_Especial(Conta):
    def __init__(self, cliente, numero, saldo = 0, limite = 0):
        Conta.__init__(self, cliente, numero, saldo)
        self.limite = limite

    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operacoes.append(["Saque", valor])
