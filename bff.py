from flask import Flask, request, render_template
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
    return render_template('response.html', resp=resp)

@app.route('/aleatorio')
def aleatorio():
    return render_template('aleatorio.html')

@app.route('/')
def say_hello():
    return render_template('index.html')


app.run(debug=True)