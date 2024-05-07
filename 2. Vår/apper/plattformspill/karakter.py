import math
import pygame as pg

class Karakter():
    def __init__(self, navn:str, x:int, y:int, kart_bredde:int, kart_hoyde:int) -> None:
        self.navn = navn
        self.liv = 10
        self.x = x
        self.y = y
        self.fart = 2
        self.gac = 2
        self.kart_bredde = kart_bredde
        self.kart_hoyde = kart_hoyde
        self.status = 1

    def move(self, taster):
        if taster[pg.K_w] and taster[pg.K_d]:
            self.x += math.sqrt(self.fart)
            self.y += -math.sqrt(self.fart)
        elif taster[pg.K_d] and taster[pg.K_s]:
            self.x += math.sqrt(self.fart)
            self.y += math.sqrt(self.fart)
        elif taster[pg.K_s] and taster[pg.K_a]:
            self.x += -math.sqrt(self.fart)
            self.y += math.sqrt(self.fart)
        elif taster[pg.K_a] and taster[pg.K_w]:
            self.x += -math.sqrt(self.fart)
            self.y += -math.sqrt(self.fart)
        elif taster[pg.K_w]:
            self.y -= self.fart
        elif taster[pg.K_d]:
            self.x += self.fart
        elif taster[pg.K_s]:
            self.y += self.fart
        elif taster[pg.K_a]:
            self.x -= self.fart



    
    def __str__(self) -> str:
        return(f"{self.navn}, {self.x, self.y}")
    
    def draw(self, vindu):
        pg.draw.circle(vindu, "white", (self.x, self.y), 10)
