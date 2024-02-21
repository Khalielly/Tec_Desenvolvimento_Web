class Conta:
    def __init__ (self,clientes, numero, saldo = 0):
        self.saldo = 0
        self.cleintes = clientes
        self.numero = numero
        self.operacoes = []
        self.deposito(saldo)
    
    def resumo(self):
        print(f'CC Número: {self.numero} saldo: {self.saldo: .2f}')
        for cliente in self.cleintes:
            print(f"Nome: {cliente.nome}\ntelefone: {cliente.telefone}\n")
    
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operacoes.append(["SAQUE", valor])
        else:
            print("Saldo insuficiente")
    
    def deposito(self,valor):
        self.saldo += valor
        self.operacoes.append(["DEPÓSITO", valor])
    
    def extrato(self):
        print(f'Extrato CC N° {self.numero}\n')
        for o in self.operacoes:
            print(f'{o[0]:10s} {o[1]:10.2f}')
        print(f'\n Saldo: {self.saldo:10.2f}\n')
