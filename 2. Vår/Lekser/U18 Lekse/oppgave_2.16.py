import json
with open("data/Global YouTube Statistics.json") as fil:
    data = json.load(fil)
fil.close()

Countries = {
    "none": 0
}

for kanal in data:
    land = kanal["Country"]
    if land in Countries:
        Countries[land] += 1
    else:
        Countries[land] = 1

Land_sortert = sorted(Countries.items(), key=lambda person: person[1], reverse=True)
top10 = Land_sortert[:10]
print(top10) # -> [('Ravi', 39), ('Thor', 33)]

#Format: {"navn": "none", "antall kanaler": 0, "antall visninger": 0, "antall abonnenter": 0, "gjenomsnittlig abonnenter": 0, "gjenomsnittlig videovisninger": 0 }
top_10_land = []

for i in range(0, len(top10)):
    top_10_land.append({})
    top_10_land[i]["navn"] = top10[i][0]
    top_10_land[i]["antall kanaler"] = top10[i][1]
    top_10_land[i]["antall visninger"] = 0
    top_10_land[i]["antall abonnenter"] = 0

    for kanal in data:
        if kanal["Country"] == top_10_land[i]["navn"]:
            top_10_land[i]["antall visninger"] += kanal["video views"]
            top_10_land[i]["antall abonnenter"] += kanal["subscribers"]
    
    top_10_land[i]["gjennomsnittlig visninger"] = top_10_land[i]["antall visninger"]/top_10_land[i]["antall kanaler"]
    top_10_land[i]["gjennomsnittlig abonnenter"] = top_10_land[i]["antall abonnenter"]/top_10_land[i]["antall kanaler"]



print(top_10_land)


