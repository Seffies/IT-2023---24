from politiker import Politiker
class Fantasiparti:
    def __init__(self, navn: str, eier:str) -> None:
        self.navn: str = navn
        self.eier: str = eier
        self.poeng: int = 0
        self.saldo:int = 0
        self.politiker_leder: Politiker = None
        self.politikere: list[Politiker] = []
    
    def selg_politiker(self, politiker = Politiker):
        if politiker in self.politikere:
            self.saldo += politiker.verdi
            self.politikere.remove(politiker)
        else: 
            print("Feil! Du eier ikke denne politikeren")


    def kjoep_politiker(self, politiker = Politiker):
        if self.saldo >= politiker.verdi and politiker not in self.politikere:
            self.saldo -= politiker.verdi
            self.politikere.append(politiker)
        else:
            print("Avvist! Politikeren du prøver å kjøpe er ikke mulig å kjøpe akkuratt nå.")

if __name__ == "__main__":
    print("Tester Fantasiparti")
    testparti = Fantasiparti("Apolitisk testparti", "Tester")
    print(testparti)