import pygame as pg
class Spillobjekt():
    def __init__(self, farge:str) -> None:
        self.surface: pg.Surface = pg.Surface((50, 50))
        self.rect = self.surface.get_rect()
        self.surface.fill(farge)
    
    def plassering(self, x:int, y: int):
        self.rect.center = (x,y)

    def flytt(self, dx:int, dy: int):
        self.rect.move_ip(dx,dy)

    def tegn(self, surface: pg.Surface):
        surface.blit(self.surface, self.rect)