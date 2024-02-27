import os
import sys
import time
import json
from pokemon import Pokemon
from trener import Trener

with open("pokedex_1stgen.json", "r", encoding="utf-8") as fil:
    data = json.load(fil)


def rens_terminal():
    if sys.platform == "win32":
        os.system("cls")
    else:
        os.system("clear")
    
pokemon_liste = []
for pokemon_ordbok in data:
    ny_pokemon = Pokemon(pokemon_ordbok)
    pokemon_liste.append(ny_pokemon)

trenerliste = []
sleeptimer = 10

while True:
    rens_terminal()
    print("-- Velkommen til Pokémon --")
    print("1. Se pokémonoversikt")
    print("2. Se treneroversikt")
    print("3. Lag trener")
    print("4. Innstillinger")
    print("5. Avslutt")
    brukerinput = input("> ")

    if brukerinput == "1":
        rens_terminal()
        print("Pokémonoversikt: \n")
        time.sleep(1)
        for pokemon in pokemon_liste:
            print(pokemon)
        
        print(f"\nSender deg tilbake etter {sleeptimer} sekunder,  dette kan endres i innstillinger")
        time.sleep(sleeptimer)

    elif brukerinput == "2":
        rens_terminal()
        print("Treneroversikt\n")
        time.sleep(1)
        if len(trenerliste) == 0:
            print("Det finnes desverre ikke noen trenere lagret på denne spillfilen")
        else:
            for trener in trenerliste:
                print(trener)

        print(f"\nSender deg tilbake etter {sleeptimer} sekunder, dette kan endres i innstillinger")
        time.sleep(sleeptimer)

    elif brukerinput == "3":
            rens_terminal()
            print("Lager ny trener")
            time.sleep(1)
            print("Hva heter treneren?")
            trenernavn = input("> ")
            trenerliste.append(Trener(trenernavn))
        
    elif brukerinput == "4":
        rens_terminal()
        print("Innstillinger \n")
        time.sleep(1)
        print(f"Velg ny sleeptimer per meny. Nåverende: {sleeptimer}")
        sleeptimer = int(input("> "))
        

    elif brukerinput == "5":
        rens_terminal()
        print("Avslutter spill")
        time.sleep(1)
        break


        
    