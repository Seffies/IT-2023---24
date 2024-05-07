import random
from spillobjekt import Spillobjekt
class Sau(Spillobjekt):
    def __init__(self) -> None:
        """
        En klasse for spillobjektet menneske

        
        # metoder og atributter som har (-) foran er arvet fra super
        atributter
        - xPosisjon:int
        - yPosisjon:int
        blirBaret: bool

        metoder: 

        """
        super().__init__("yellow")
        self.blirLøftet: bool = False
        tillfeldig_y = random.randint(450, 525) #uten self. legger det bare i cache
        tillfeldig_x = random.randint(100, 500)
        self.plassering(tillfeldig_y, tillfeldig_x)

