import json
from flask import Flask
import requests
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, support_credentials=True)

def get_pokemons():
    check_val = 'S'
    data = requests.get('https://pokeapi.co/api/v2/type/11/').json()
    pokemons = data['pokemon']
    pokemon_data = list()
    for val in pokemons:
        pokemon = val['pokemon']['name']
        if pokemon.startswith(check_val.lower()):
            pokemon_data.append(pokemon)
    return pokemon_data


@app.route('/get-pokemon', methods=['POST', 'GET', 'OPTIONS'])
@cross_origin()
def get_pokemon():
    pokemons = get_pokemons()
    return json.dumps({
        'pokemons': pokemons
    }), 200


if __name__ == '__main__':
    app.run(debug=True, port=5000)
