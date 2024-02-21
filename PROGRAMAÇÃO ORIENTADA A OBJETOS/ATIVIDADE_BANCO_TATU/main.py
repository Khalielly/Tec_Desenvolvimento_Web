from cliente import Cliente
from contas import Conta
from banco import Banco
from conta_especial import Conta_Especial

# pedro = Cliente ('Pedrinho noiado', 165414651645)

# maria = Cliente('Maria da Butina', 41651565 )
# joao = Cliente('Joao do gas', 51651654)
# maria = Cliente('Maria vai com as outras', 1156156)

# cont_pedro = Conta(pedro, 157, 33)
# cont_joao = Conta(joao, 123, 10000)
# cont_maria = Conta(maria, 190, 100000)

# print(f'A conta {cont_maria.clientes.nome} foi criada e tem o n° {cont_maria.numero} com saldo de R$ {cont_maria.saldo}')

# #print(pedro.nome, pedro.telefone)
# cont_maria.resumo()
# cont_maria.saque(1000)
# cont_maria.resumo()
# cont_maria.deposito(50000)
# cont_maria.resumo()
# cont_maria.saque(500000)
# cont_maria.resumo()
# cont_maria.extrato()


# print(pedro.nome, pedro.telefone)

# joao = Cliente("Jao do Mandioca", "999995552")
# maria = Cliente("Mariana conta 1", "97777888")
# jose = Cliente("Jose do Paeiro", "445468798")

# contaJM = Conta([joao, maria], 100)
# contaJ = Conta([jose], 10)

# tatu = Banco("Tatu")
# tatu.abre_conta(contaJM)
# tatu.abre_conta(contaJ)
# tatu.lista_contas()

joao = Cliente("João de Silva", "8904-5656")
maria = Cliente("Maria Lurdes", "5478-9800")

conta_1 = Conta([joao], 1, 1000)
conta_2 = Conta_Especial([joao, maria], 2, 500, 1000)

conta_1.saque(50)
conta_2.deposito(300)
conta_1.saque(190)
conta_2.deposito(95.15)
conta_2.saque(1500)
conta_1.saque(800)
conta_1.extrato()
conta_2.extrato()