import pygame
import math
from karakter import Karakter
from gulv import Gulv
from vegg import Vegg

pygame.init()
BREDDE = 1024
HOYDE = 640
FPS = 50

vindu = pygame.display.set_mode((BREDDE,HOYDE))
clock = pygame.time.Clock()
x = 100
y = 100
spiller = Karakter("Spiller 1", x, y, BREDDE, HOYDE)
kloss = Gulv(0, 0, "G")
data = "OOOOOOOOOOOOOOOOOOOOOGFGGOOOOOOOOOOOGGGFFGOOOOOOOOOOGFGGFFGOOOOOOOOGGGGFGFGGOOOOOOOGFGFFFGFGOOOOOOOOGGGFFGGGOOOOOOOOOGGGGGGOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO"
floormap = []
wallmap = []
placingx = 0
placingy = 0

for i in range(len(data)):
    print(data[i], placingx, ".", placingy)
    floormap.append(Gulv(placingx, placingy, data[i]))
    wallmap.append(Vegg(placingx, placingy, data[i], data, i))
    if placingx == 960:
        placingx = 0
        placingy += 64
    else: 
        placingx += 64
"""
for objekt in data:
    print(objekt, placingx, ".", placingy)
    floormap.append(Gulv(placingx, placingy, objekt))
    if placingx == 960:
        placingx = 0
        placingy += 64
    else: 
        placingx += 64
"""

while True:
    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
    taster = pygame.key.get_pressed()
    spiller.move(taster)
    #print(spiller)
    
    if spiller.status == 0:
        pygame.quit()
        raise SystemExit
    
    vindu.fill((131, 219,242))
    for objekt in floormap:
        objekt.draw(vindu)
    for objekt in wallmap:
        objekt.draw(vindu)
    spiller.draw(vindu)
    pygame.display.flip()
    clock.tick(60)

