import csv 
from itertools import groupby

def ler_csv(arquivo_csv: str) -> list[dict]:
    """
    Função que le um arquivo csv e retorna uma lista de dicionarios
    """
    lista = []
    with open(arquivo_csv, mode='r', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
        return lista
    
vendas = ler_csv('vendas.csv')

def key_produto(key):
    return key['Produto']

vendas = sorted(vendas, key=key_produto)

for key, produto in groupby(vendas, key_produto):
    print(key)
    print(list(produto))

