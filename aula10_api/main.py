import requests
from pydantic import BaseModel



class PokemonSchema(BaseModel):
    name: str
    type: str

    class Config:
        orm_mode = True

def pegar_pokemon(id: int):
    
    URL = f'https://pokeapi.co/api/v2/pokemon/{id}'
    response = requests.get(url=URL)

    data = response.json() 
    data_types = data['types']
    types_list = []

    for type_info in data_types:
        types_list.append(type_info['type']['name'])
    types = ', '.join(types_list)
    return PokemonSchema(name=data['name'], type=types)


if __name__ == '__main__':
    pegar_pokemon(20)