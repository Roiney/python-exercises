import json

with open('pokemon.json') as file:
   content = file.read()
   pokemons = json.loads(content)["results"]
   
print(pokemons[0])

with open('pokemon.json') as file:
   pokemon = json.load(file)["results"]

print(pokemon[0])

