from pokemon import Pokemon

class Trener:
    def __init__(self, navn: str, ) -> None:
        self.navn: str = navn
        self.pokemonliste: list[Pokemon] = []

    def legg_til_pokemon(self, pokemon: Pokemon):
        self.pokemonliste.append(pokemon)

    def fjern_pokemon(self, pokemon: Pokemon):
        self.pokemonliste.remove(pokemon)

    def __str__(self) -> str:
        return f"{self.navn} - {len(self.pokemonliste)}"