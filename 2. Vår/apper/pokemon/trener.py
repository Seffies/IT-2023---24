from pokemon import Pokemon

class Trener():
    def __init__(self, navn) -> None:
        self.navn: str = navn
        self.pokemons: list[Pokemon] = []

    def __str__(self) -> str:
        return f"{self.navn}: {len(self.pokemons)} pokemoner"