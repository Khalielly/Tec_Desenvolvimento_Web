class Estado:
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        self.cidades = []

    def add_cidade (self, cidade):
        self.cidades.append(cidade)

    def populacao_total(self):
        return sum(cidade.populacao for cidade in self.cidades)

