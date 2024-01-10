## Pseudokode 
- Gjør det lettere å koomunisere og sammarbeide med andre programerere, samt å teste og feilsøke algoritmer før de blir kodet
- En god måte å lære grunnlegende programeringskonsepter på, da det kan hjelpe deg med å forstå hvordan ulike instruksjoner og logiske uttrykk ufungerer sammen for å løse et bestemt problem

## eksempel 

> En algoritme som regner ut hvor mye penger vi tjener på spotify

```pseudo
Hent inn antall streams 

Hvis antall streams er større enn 30 000 000:
    Returner antall streams gange 0.7
Ellers hvis antall streams er større enn 1 400 000:
    Returner antall streams gange 0.4
Ellers
    Returner 0
```

> En algoritme som regner ut hvor mye penger vi tjener på spotify(med nøkkelord)

```pseudo
SET antall_streams TO READ "hvor mange streams" 

IF antall_streams GREATER THAN 30 000 000:
    THEN DISPLAY antall_streams * 0.7
ELSE IF antall_streams GREATER THAN 1 400 000:
    THEN DISPLAY antall_streams * 0.4
ELSE
    THEN DISPLAY 0
```

```python
streams = int(input("..."))

if streams > 30_000_000:
    return streams * 0.7
elif streams > 1_400_000:
    return streams * 0.4
else:
    retun 0
``````