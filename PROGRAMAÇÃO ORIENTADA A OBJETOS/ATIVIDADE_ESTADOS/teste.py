from estado import Estado
from cidade import Cidade

goias = Estado ("Goiás", "GO")

cidade_goias = Cidade("Goiânia", 2.848000)
cidade_goias2 = Cidade("Poranga", 44.317)
cidade_goias3 = Cidade("Anapolis", 398.817)

goias.add_cidade(cidade_goias)
goias.add_cidade(cidade_goias2)
goias.add_cidade(cidade_goias3)

santa_catarina = Estado("Santa Catarina", "SC")

cidade_SC = Cidade("Florianópolis",537.213)
cidade_SC2 = Cidade("Joinville",616.323)
cidade_SC3 = Cidade("Blumenau",361.261)

santa_catarina.add_cidade(cidade_SC)
santa_catarina.add_cidade(cidade_SC2)
santa_catarina.add_cidade(cidade_SC3)

minas_gerais = Estado("Minas Gerais", "MG")

cidade_minas = Cidade("Belo Horizonte",2.315560)
cidade_minas2 = Cidade("Uberlândia",713.232)
cidade_minas3 = Cidade("Contagem",621.865)

minas_gerais.add_cidade(cidade_minas)
minas_gerais.add_cidade(cidade_minas2)
minas_gerais.add_cidade(cidade_minas3)

# print("------------------------------------------------------------------------------------------------------------")
# print(f'O estado {goias.nome} - {goias.sigla} tem {goias.cidade_goias} uma população total de: {goias.populacao_total()} habitantes')
# print("------------------------------------------------------------------------------------------------------------")
# print(f'O estado {santa_catarina.nome} - {santa_catarina.sigla} tem uma população total de: {santa_catarina.populacao_total()} habitantes')
# print("------------------------------------------------------------------------------------------------------------")
# print(f'O estado {minas_gerais.nome} - {minas_gerais.sigla} tem uma população total de: {minas_gerais.populacao_total()} habitantes')
# print("------------------------------------------------------------------------------------------------------------")

for estado in [goias, santa_catarina, minas_gerais]:
    print(f"\nCidades do {estado.nome}:")
    for cidade in estado.cidades:
        print(f" - {cidade.nome}: População {cidade.populacao}")
    print(f"População total das 3 cidades de {estado.nome}: {estado.populacao_total()} habitantes\n")