import pygame as pg

class Objekt():
    """
    En Klasse for objekter

    attributter: 
        bildesti (str) = sti til sprite
        scale (flt) = float som definerer forholdet objektet har til resten, brukes for å komprimere til 64x64 for det meste
    metoder
        Tegn() = tegner objektet på flaten
    """
    def __init__(self, bildesti:str, scale:float) -> None:
        self.bilde = pg.image.load(bildesti).convert_alpha()
        self.bilde = pg.transform.scale_by(self.bilde, scale)
        self.ramme = self.bilde.get_rect()

    def tegn(self, vindu:pg.Surface):
        vindu.blit(self.bilde, self.ramme)