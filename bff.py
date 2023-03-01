from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/pokemon')
def pokemon():
    idSearch = request.args.get('id')
    respPoke = requests.get('https://pokeapi.co/api/v2/pokemon/' + idSearch)
    jsonPoke = respPoke.json()
    respDigi = requests.get('https://digi-api.com/api/v1/digimon/' + idSearch)
    jsonDigi = respDigi.json()
    resp = {'Pokemon': jsonPoke['forms'][0].get('name'), 'id': jsonPoke.get('order'), 'PokeImage': jsonPoke['sprites'].get('front_default'), 'Digimon': jsonDigi.get('name'), 'DigiImage' : jsonDigi['images'][0]['href']}
    # resp = {'Pokemon':id,'name': jsonPoke['name'][0].get('forms').get('name')}
    return resp


app.run(debug=True)