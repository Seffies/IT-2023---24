#Algoritme 1: høyeste tall i liste
def hoyeste(liste:list[int]):
    highest = liste[0]
    for objekt in liste:
        if objekt > highest:
            highest = objekt
    return highest

#Algoritme 2: gjennomsnitt
def gjennomsnitt(liste: list[int]):
    total = 0
    antall = 0
    for tall in liste:
        total += tall
        antall += 1
    return total/antall

#Algoritme 3: nest høyeste
def nest_hoyest(liste: list[int]):
    hoyest = -9999
    nest_hoyest = -9999
    for tall in liste:
        if tall > hoyest:
            nest_hoyest = hoyest
            hoyest = tall
        elif tall > nest_hoyest:
            nest_hoyest = tall
    return nest_hoyest 

#Algoritme 4: n hoyeste - komplisert
def n_hoyeste_komplisert(liste: list[int], n:int):
    n_hoyeste = []
    for i in range(0, n):
        hoyest = hoyeste(liste)
        liste.remove(hoyest)
        n_hoyeste.append(hoyest)
    return n_hoyeste

#Algoritme 4: n hoyeste - enkel
def n_hoyeste_enkel(liste: list[int], n):
    liste = liste.sort(reverse=True)
    return liste[-n]


#Algoritme 5: høyeste tall i liste


#Algoritme 6: høyeste tall i liste

