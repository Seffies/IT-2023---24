import os
import sys
import time
import json
from pokemon import Pokemon


def rens_terminal():
    if sys.platform == "Windows":
        os.system("cls")
    else: 
        os.system("clear")

#1. Oppsett
with open("pokedex_1stgen.json", "r", encoding="utf-8") as fil:
    data = json.load(fil)
pokedex = data

pokemon = []
for pokemon_ordbok in pokedex:
    ny_pokemon = Pokemon(pokemon_ordbok)
    pokemon.append(ny_pokemon)

for guy in pokemon:
    print(guy)
