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
        oekPoeng (poeng:int) = øker poengscoren med følgende int
        reduserFart (fart:int) = øker farten med følgende int
        bærSau (objekt: Sau) = plukker opp en sau og gjør spilleren innaktiv for å plukke andre
        
        """
        super().__init__("green")
        self.fart: int = 0
        self.poeng: int = 0
        self.løftersau: bool = False
        self.plassering(75, 300)
    
    def reduserFart(self, fart):
        self.fart = fart

    def oekPoeng(self, poeng):
        self.poeng += poeng

    def bærSau(self, objekt: Sau):
        self.løftersau = True
    
    def sjekkKolisjon(self):
        pass



class Hindring(Spillobjekt):
    def __init__(self) -> None:
        super().__init__()

class spøkelse(Spillobjekt):
    def __init__(self) -> None:
        super().__init__()
    
    def endreRettning(self):
        pass
