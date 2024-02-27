import os
import sys
import time
import json
from politiker import Politiker

def hovedmeny():
    print("1: Vis politiker oversikt")
    print("2: Avslutt")

def rens_terminal():
    if sys.platform == "win32":
        os.system("cls")
    else: 
        os.system("clear")

#1. Oppsett
with open("representanter.json", "r", encoding="utf-8") as fil:
    data = json.load(fil)
representanter = data["dagensrepresentanter_liste"]

politikere = []
for politiker_ordbok in representanter:
    ny_politiker = Politiker(politiker_ordbok)
    politikere.append(ny_politiker)


rens_terminal()
print("------------------------------------\n\n\n    Velkommen til Fantasi-tinget    \n\n\n------------------------------------")
time.sleep(2)
rens_terminal()
time.sleep(1)

while True:
    print("           Fantasi-tinget           ")
    print("------------------------------------")
    for politker in politikere:
        print(politker)
    hovedmeny()
    brukervalg = input("\n> ")
    if brukervalg == "2":
        rens_terminal()
        print("Avslutter")
        break

print("Takk for nå!")