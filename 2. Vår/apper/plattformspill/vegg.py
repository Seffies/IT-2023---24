import random
import pygame as pg
from objekt import Objekt


class Vegg(Objekt):
    def __init__(self, x:int, y:int, type:str, data:str, ind: int) -> None:
        #super().__init__(bildesti, 1)
        """
        En Klasse vegger

        attributter: 
            x (int) = x kodrinatet til boksen
            y (int) = y kodrinatet til boksen
            type (str) = Bestemmer om brikken er gress (G) eller blomst(B)
            data (str) = kartet med alle typene, sjekker om naboene til klossen kan ha vegger
            ind (int) = forteller relative posisjon i datafeltet

        metoder
            Tegn(), arvet fra super =  
        """
        self.aktiv = False
        self.type = type
        if self.type != "O":
            if data[ind + 16] == "O":
                self.aktiv = True
                super().__init__(f"bilder/Sprites/Walls/Wall{1}.png",  1) #random.randint(1,4)
                self.ramme.x = x 
                self.ramme.y = y + 64

    def draw(self, vindu):
        if self.aktiv == True:
            self.tegn(vindu)
        else:
            pass

        


