import requests
from .db import SessionLocal, engine, Base
from .models import Pokemon
from .schema import PokemonSchema
from random import randint

Base.metadata.create_all(bind=engine)

def gerar_numero_aleatorio():
    return randint(1, 350)

def fetch_pokemon_data(pokemon_id: int):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    if response.status_code == 200:
        data = response.json()
        types = ', '.join(type['type']['name'] for type in data['types'])
        return PokemonSchema(name=data['name'], type=types)
    else:
        return None

def add_pokemon_to_db(pokemon_schema: PokemonSchema) -> dict:
    with SessionLocal() as db:
        db_pokemon = Pokemon(name=pokemon_schema.name, type=pokemon_schema.type)
        db.add(db_pokemon)
        db.commit()
        db.refresh(db_pokemon)
        
        # Converta o objeto Pokemon para um dicionário
        pokemon_dict = {
            "id": db_pokemon.id,
            "name": db_pokemon.name,
            "type": db_pokemon.type,
            "created_at": db_pokemon.created_at.isoformat() if db_pokemon.created_at else None
        }
    
    return pokemon_dict