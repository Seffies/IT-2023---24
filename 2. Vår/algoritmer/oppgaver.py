import json
with open("spotify-weekly-top-songs-global-uke2-2023.json") as fil:
    data = json.load(fil)

def flest_uker_paa_listen(liste:list):
    highest = liste[0]
    for objekt in liste:
        if objekt["uker_paa_listen"] > highest["uker_paa_listen"]:
            highest = objekt
    return highest

print(flest_uker_paa_listen(data))