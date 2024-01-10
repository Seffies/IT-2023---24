# Oppgaver
>
## Oppgave 1
Hva er en while-løkke i programmering? (ett riktig svar)

- [ ] en løkke som kjører et bestemt antall ganger
- [ ] en løkke som kjører til en bestemt hendelse intreffer
- [x] en løkke som kjører så lenge en bestemt betingelse er sann
- [ ] en løkke som kjører så lenge en tilfeldig betingelse er sann

## Opgave 2
Hvilken av de følgende påstandene er riktig om for- og while-løkker innen programmering? Velg riktig alternativ.

- [ ] en for-løkke kan bare brukes med tallsekvenser
- [ ] en while-løkke kjører alltid et bestemt antall ganger
- [x] en for-løkke er best egnet når du vet hvor mange ganger du vil at løkken skal kjøre
- [ ] en while-løkke kan ikke bruke en teller for å holde rede på hvor mange ganger den har kjørt

## Oppgave 3
Hva er hovedprinsippet bak objektorientert programmering (OOP)? Velg riktig alternativ.

- [ ] å lage lineære og sekvensielle programkoder
- [ ] å bryte ned et problem i et sett med funksjoner
- [x] å representere data og funksjoner som objekter
- [ ] å minimere bruken av variabler

## Oppgave 4
Hvilket av følgende er ikke et typisk kjennetegn på pseudokode? Velg riktig alternativ.

- [ ] den har uformell syntaks.
- [ ] den ligner på vanlig menneskespråk.
- [x] den kan kjøres direkte på en datamaskin.
- [ ] den brukes ofte i planleggingsfasen av programmering.

##  Oppgave 5
Hvor mange ganger blir teksten "Lykkelig dag!" skrevet ut?

```pseudo
SET m TO 3
SET i TO 1
WHILE i GREATER THAN m
  DISPLAY "Lykkelig dag!"
  INCREMENT i
ENDWHILE
```
- [ ] tre ganger
- [ ] to ganger
- [ ] én gang
- [x] ingen ganger

## Oppgave 6
Hvilke av de følgende sekvensene med pseudokode skriver ut tallene fra og med 1 til og med 5? Flere alternativer kan være riktige. Velg riktige svar.

```pseudo
1.
SET i TO 1
FOR hver i LESSER OR EQUAL 5
  PRINT i
ENDFOR

2.
SET i TO 1
WHILE i < 5
  PRINT i
  INCREMENT i 
ENDWHILE

3.
SET i TO 0
FOR hver i LESSER OR EQUAL 4
  PRINT i+1
ENDFOR

4.
SET i TO 1
WHILE i <= 5
  PRINT i
  INCREMENT i BY 2
ENDWHILE
```

- [x] 1
- [ ] 2
- [x] 3
- [ ] 4

## Oppgave 7
Et system som beregner billettprisen avhengig av kjøperens alder, bruker følgende regler for billettkategorier:

- Hvis brukeren er 15 år gammel eller yngre, skal brukeren få barnebillett til 30 kroner.

- Hvis brukeren er 16 år gammel eller eldre, skal brukeren få voksenbillett til 50 kroner.

- Hvis brukeren er 67 år gammel eller eldre, skal brukeren få pensjonistbillett til 35 kroner.

Lag et flytdiagram for et program der brukeren skriver inn alderen på kjøperen og programmet regner ut og skriver ut riktig billettpris.

Lag flytdiagrammet i et egnet program, og lagre det i et allment lesbart format (f.eks. pdf eller png) og legg det ved i samme mappe som filen oppgaver-doa.md.

![Oppgave 7](../databehandling%20og%20algoritmer/Oppgave-7.png)
## Oppgave 8

Tallene 1, 3, 6, 10, 15, 21 og så videre kalles for trekanttall. De tilsvarer antallet prikker som vil vises i en likesidet trekant når man bruker et grunnleggende trekantmønster for å bygge trekanten.

Den følgende pseudokoden beskriver en funksjon som regner ut og returner trekanttallet nummer n:

```pseudo
FUNCTION trekanttall (n)
  SET tn TO n * (n+1)/2
  RETURN tn
ENDFUNCTION
```

Bruk funksjonen som er beskrevet ovenfor, og skriv pseudokoden til et program som regner sammen og skriver ut totalsummen av de ti første trekanttallene. Bruk dobbelt mellomrom for innrykk i koden der det er aktuelt. Skriv svaret ditt nedenfor.

```python
def trekantall(n):
    tn = n * (n+1/2)
    return tn
```

```pseudo
Bruk forrgie funksjon også setter du inn i en forløkke


```
> OBS: Du kan bruke din egen standard for pseudokode, bare den er hensiktsmessig.

