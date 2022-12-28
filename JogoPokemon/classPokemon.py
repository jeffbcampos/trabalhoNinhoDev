class Pokemon:
    def __init__(self, nome, tipo, hp, level):
        self._nome = nome
        self._tipo = tipo
        self._hp = hp
        self._level = level

    def checarVantagem(self, pokemonInimigo):
        if self._tipo == 'Normal':
            if pokemonInimigo['tipo'] == 'Elétrico':
                pokemonInimigo['hp'] -= 5
            elif pokemonInimigo['tipo'] == 'Fogo':
                pokemonInimigo['hp'] -= 5
            elif pokemonInimigo['tipo'] == 'Água':
                pokemonInimigo['hp'] -= 5
            elif pokemonInimigo['tipo'] == 'Grama':
                pokemonInimigo['hp'] -= 5            
            else:
                pokemonInimigo['hp'] -= 10
        else:
            pokemonInimigo['hp'] -= 10



class PokemonEletrico(Pokemon):
    def __init__(self, nome, tipo, hp, level):
        super().__init__(nome, tipo, hp, level)
    
    def checarVantagem(self, pokemonInimigo):
        if self._tipo == 'Elétrico':
            if pokemonInimigo['tipo'] == 'Elétrico':
                pokemonInimigo['hp'] -= 10
            elif pokemonInimigo['tipo'] == 'Normal':
                pokemonInimigo['hp'] -= 15
            elif pokemonInimigo['tipo'] == 'Água':
                pokemonInimigo['hp'] -= 15
            else:
                pokemonInimigo['hp'] -= 10



class PokemonFogo(Pokemon):
    def __init__(self, nome, tipo, hp, level):
        super().__init__(nome, tipo, hp, level)

    def checarVantagem(self, pokemonInimigo):
        if self._tipo == 'Fogo':
            if pokemonInimigo['tipo'] == 'Fogo':
                pokemonInimigo['hp'] -= 10
            elif pokemonInimigo['tipo'] == 'Normal':
                pokemonInimigo['hp'] -= 15
            elif pokemonInimigo['tipo'] == 'Água':
                pokemonInimigo['hp'] -= 5
            elif pokemonInimigo['tipo'] == 'Grama':
                pokemonInimigo['hp'] -= 15
            else:
                pokemonInimigo['hp'] -= 10

class PokemonAgua(Pokemon):
    def __init__(self, nome, tipo, hp, level):
        super().__init__(nome, tipo, hp, level)

    def checarVantagem(self, pokemonInimigo):
        if self._tipo == 'Água':
            if pokemonInimigo['tipo'] == 'Água':
                pokemonInimigo['hp'] -= 10
            elif pokemonInimigo['tipo'] == 'Normal':
                pokemonInimigo['hp'] -= 15
            elif pokemonInimigo['tipo'] == 'Terrestre':
                pokemonInimigo['hp'] -= 15
            else:
                pokemonInimigo['hp'] -= 10

class PokemonGrama(Pokemon):
    def __init__(self, nome, tipo, hp, level):
        super().__init__(nome, tipo, hp, level)

    def checarVantagem(self, pokemonInimigo):
        if self._tipo == 'Grama':            
            if pokemonInimigo['tipo'] == 'Terrestre':
                pokemonInimigo['hp'] -= 15
            elif pokemonInimigo['tipo'] == 'Fogo':
                pokemonInimigo['hp'] -= 5
            elif pokemonInimigo['tipo'] == 'Água':
                pokemonInimigo['hp'] -= 15
            else:
                pokemonInimigo['hp'] -= 10