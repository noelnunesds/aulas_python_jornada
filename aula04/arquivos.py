import csv 

caminho = "aula04/dananda.csv"

dados: list = []

# Gerenciador de contexto
with open(caminho, mode="r", encoding='utf-8') as arquivo: 
    leitor_csv = csv.DictReader(arquivo)

    for linha in leitor_csv:
        dados.append(linha)

print(dados)


lista = [1, 1, 2, 2,31,2, 323, 52, 4,1,12 ,42, 41,41]

print(lista.sort())
