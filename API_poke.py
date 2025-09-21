import requests

def get_pokemon_by_type(tipo):
    """
    Generador que obtiene Pokémon de un tipo (fire, water, electric, etc.)
    desde la PokeAPI y los entrega uno por uno.
    """
    url = f"https://pokeapi.co/api/v2/type/{tipo}/"
    r = requests.get(url)
    data = r.json()
    
    print("Status Code:  ", r.status_code) # 200 = éxito

    print(f"Los pokemon de tipo {tipo} son:")
    for p in data["pokemon"]:
        print("-", p["pokemon"]["name"])

get_pokemon_by_type(tipo=input("Ingrese el tipo del pokemon en ingles: "))
