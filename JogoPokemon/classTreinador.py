from pokedex import pokemons
import classPokemon
from random import choice

class Treinador:
    def __init__(self, nome, listaPokemons = []):
        self._nome = nome
        self._listaPokemons = listaPokemons

    def getNome(self):
        return self._nome

    def mostrarPokemons(self):
        print("\nSeus pokemons são: \n\n")
        for i in range(len(self._listaPokemons)):
            print(f"{i + 1} - {self._listaPokemons[i].getNome()}")

    def pokemonInicial(self):
        primeiroPokemon = input('''
        Digite com qual pokemon você quer começar:\n
        1 - Charmander
        2 - Bulbasaur
        3 - Squirtle
        ''')
        if primeiroPokemon == '1':
            print("Parabéns você escolheu o Charmander!")
            primeiroPokemon = "Charmander"
            for pokemon in pokemons:
                if primeiroPokemon == pokemon['nome']:
                    self._listaPokemons.append(classPokemon.adicionarClassePokemon(pokemon))
        if primeiroPokemon == '2':
            print("Parabéns você escolheu o Bulbasaur!")
            primeiroPokemon = "Bulbasaur"
            for pokemon in pokemons:
                if primeiroPokemon == pokemon['nome']:
                    self._listaPokemons.append(classPokemon.adicionarClassePokemon(pokemon))
        if primeiroPokemon == '3':
            print("Parabéns você escolheu o Squirtle!")
            primeiroPokemon = "Squirtle"
            for pokemon in pokemons:
                if primeiroPokemon == pokemon['nome']:
                    self._listaPokemons.append(classPokemon.adicionarClassePokemon(pokemon))
        return self._listaPokemons

class TreinadorInimigo(Treinador):
    def __init__(self, nome, listaPokemons=[]):
        super().__init__(nome, listaPokemons)
    
    def pokemonInicial(self):        
        for p in range(0, 3):
            pokemonAleatorio = choice(pokemons)#pokemons[randint(0, 149)]        
            self._listaPokemons.append(classPokemon.adicionarClassePokemon(pokemonAleatorio))
        print(f'''Os pokemons do seu Inimigo são:\n
                1- {self._listaPokemons[0].getNome()}
                2- {self._listaPokemons[1].getNome()}
                3- {self._listaPokemons[2].getNome()}
                ''')
        return self._listaPokemons