from flask import Flask
import requests
from flask_cors import CORS
from flask_restful import Resource, Api
from apispec import APISpec
from marshmallow import Schema, fields
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs

app = Flask(__name__)
api = Api(app)
CORS(app, support_credentials=True)


app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Get PokeMon starting with S',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/swagger/',  # URI to access API Doc JSON
    'APISPEC_SWAGGER_UI_URL': '/swagger-ui/'  # URI to access UI of API Doc
})
docs = FlaskApiSpec(app)


class ResponseSchema(Schema):
    message = fields.Str(default='Success')



class API(MethodResource, Resource):
    @doc(description='Get Pokemons that start with S', tags=['Pokemon Data'])
    # @marshal_with(ResponseSchema)
    def get(self):
        '''
        Get method represents a GET API method
        '''
        pokemons = get_pokemons()
        return {'pokemons': pokemons}, 200



api.add_resource(API, '/get-pokemon')
docs.register(API)


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


if __name__ == '__main__':
    app.run(debug=True, port=5000)
