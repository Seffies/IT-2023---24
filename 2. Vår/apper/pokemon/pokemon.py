class Pokemon:
    def __init__(self, pokemon_ordbok: dict) -> None:
        self.id: int = pokemon_ordbok["id"]
        self.navn: str = pokemon_ordbok["name"]["english"]
        self.hp: int = pokemon_ordbok["base"]["HP"]
        self.attack: int = pokemon_ordbok["base"]["Attack"]
        self.defense: int = pokemon_ordbok["base"]["Defense"]
        self.sp_attack: int = pokemon_ordbok["base"]["Sp. Attack"]
        self.sp_defense: int = pokemon_ordbok["base"]["Sp. Defense"]
        self.speed: int = pokemon_ordbok["base"]["Speed"]
        self.type: list[str] = pokemon_ordbok["type"]

    def __str__(self) -> str:
        return f"{self.id}. {self.navn}, {self.type}"