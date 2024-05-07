import pygame as pg
from spillobjekt import Spillobjekt
from menneske import Menneske
from sau import Sau

class Spillebrett:
    def __init__(self, hoyde, bredde) -> None:
        self.hoyde: int = hoyde
        self.bredde: int = bredde
        self.objekter: list[Spillobjekt] = []
    
        self.surface = pg.Surface((self.bredde, self.hoyde))
        self.rect = self.surface.get_rect()

        self.rect.topleft = (0,0)

        self.surface.fill("white")

        self.spiller1 =  Menneske()
        for i in range(3):
            self.objekter.append(Sau())
        
        
    
    def legg_til_objekt(self, nytt_objekt: Spillobjekt):
        self.objekter.append(nytt_objekt)

    def fjern(self, objekt: Spillobjekt):
        self.objekter.remove(objekt)
    
    def tegn(self, vindu: pg.Surface):
        for objekt in self.objekter:
            objekt.tegn(self.surface)
        self.spiller1.tegn(self.surface)
        vindu.blit(self.surface, self.rect) # tegner spillbrettets surface i posisjonen til spillbrettets rect på vinduet
