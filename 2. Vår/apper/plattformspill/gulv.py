import random
import pygame as pg
from objekt import Objekt

class Gulv(Objekt):
    def __init__(self, x:int, y:int, type:str) -> None:
        """
        En Klasse for underlagsklosser

        attributter: 
            x (int) = x kodrinatet til boksen
            y (int) = y kodrinatet til boksen
            type (str) = Bestemmer om brikken er gress (G) eller blomst (F), eller ingenting (O)

        metoder
            Tegn(), arvet fra super = tegner objektet
            Draw() = bruker superen til forrige, men sjekker først om objektet har en type eller om det er innaktivt, kan ikke tegne innaktive objekter

        """
        self.type = type
        if self.type == "G":
            self.bilde = f"bilder/Sprites/Tiles/Grass{random.randint(1,4)}.png" #random.randint(1,4)
        elif self.type == "F":
            self.bilde = f"bilder/Sprites/Tiles/Flowers{random.randint(1,4)}.png" #f"bilder/Sprites/Tiles/Flowers{random.randint(1,4)}.png" 
        else:
            self.bilde = None
        
        if self.bilde != None:
            super().__init__(self.bilde,  1) #finne ut hvordan bruke super sin self.skala
            self.ramme.x = x
            self.ramme.y = y

    def draw(self, vindu):
        if self.bilde != None:
            self.tegn(vindu)
        else:
            pass


