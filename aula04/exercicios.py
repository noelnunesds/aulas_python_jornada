livro: dict = {
    "Titulo": "Game of Thrones",
    "Autor": "Noel",
    "Ano": 2005
}

for chave, valor in livro.items():
    print(f'{chave}: {valor}')

print(livro.items())
