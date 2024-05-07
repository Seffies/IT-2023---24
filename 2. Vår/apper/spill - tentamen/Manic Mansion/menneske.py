from spillobjekt import Spillobjekt
from sau import Sau
class Menneske(Spillobjekt):
    def __init__(self) -> None:
        """
        En klasse for spillobjektet menneske

        
        # metoder og atributter som har (-) foran er arvet fra super
        atributter
        - xPosisjon:int
        - yPosisjon:int
        fart: int
        poeng: int
        løfterSau: bool

        metoder
        - plassering (x:int, y:int)
        beveg
        oekPoeng (poeng:int) = øker poengscoren med følgende int
        reduserFart (fart:int) = øker farten med følgende int
        bærSau (objekt: Sau) = plukker opp en sau og gjør spilleren innaktiv for å plukke andre
        
        """
        super().__init__("green")
        self.fart_x: int = 4
        self.fart_y: int = 0
        self.poeng: int = 0
        self.løftersau: bool = False
        self.plassering(75, 300)
    
    def beveg(self):
        if self.løftersau:
            self.flytt(self.fart_x*0.8, self.fart_y*0.8)
        else:
            self.flytt(self.fart_x, self.fart_y)
    
 