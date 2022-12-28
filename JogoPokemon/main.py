from pokedex import pokemons
from random import randint
import classPokemon

treinadorInimigo = []
pokemonsJogador = []
opcao = ''

def pokemonsInimigos(treinadorInimigo):    
    for p in range(0, 3):
        treinadorInimigo.append(pokemons[randint(0, 149)]) #Laço for pra gerar a lista de 6 pokemons de cada treinador inimigo
    print(f'''Os pokemons do seu Inimigo são:
            1- {treinadorInimigo[0]['nome']}
            2- {treinadorInimigo[1]['nome']}
            3- {treinadorInimigo[2]['nome']}
            ''')
    return treinadorInimigo

def escolherPokemons(pokemonsJogador): #Função Jogador escolher seus pokemons!
    for p in range(0, 3):
        pokemonJogador = input(f'Digite o {p + 1}º pokemon da sua equipe: ').capitalize()
        for pokemon in pokemons:
            if pokemonJogador == pokemon['nome']:
                if pokemon['tipo'] == 'Elétrico':
                    pokemonsJogador.append(classPokemon.PokemonEletrico(pokemon['nome'], pokemon['tipo'], pokemon['hp'], pokemon['level']))
                elif pokemon['tipo'] == 'Fogo':
                    pokemonsJogador.append(classPokemon.PokemonFogo(pokemon['nome'], pokemon['tipo'], pokemon['hp'], pokemon['level']))
                elif pokemon['tipo'] == 'Água':
                    pokemonsJogador.append(classPokemon.PokemonAgua(pokemon['nome'], pokemon['tipo'], pokemon['hp'], pokemon['level']))
                elif pokemon['tipo'] == 'Grama':
                    pokemonsJogador.append(classPokemon.PokemonGrama(pokemon['nome'], pokemon['tipo'], pokemon['hp'], pokemon['level']))
                else:
                    pokemonsJogador.append(classPokemon.Pokemon(pokemon['nome'], pokemon['tipo'], pokemon['hp'], pokemon['level']))                       
    
    while(len(pokemonsJogador) < 3):
        pokemonsJogador.clear()
        print("Algum dos pokemons não foi digitado corretamente!Escolha Novamente!")        
        escolherPokemons(pokemonsJogador)

    return pokemonsJogador


def batalhaPokemon(pokemonInimigo):
    pokemonEscolhido = int(input(f'''
    Escolha qual pokemon usar:
    1- {pokemonsJogador[0]._nome}
    2- {pokemonsJogador[1]._nome}
    3- {pokemonsJogador[2]._nome}
    '''))
    pokemonEscolhido = pokemonsJogador[pokemonEscolhido - 1]
    print(f"Você escolheu {pokemonEscolhido._nome}")
    opcao = ''
    while(pokemonInimigo['hp'] > 0):
        opcao = input('''
        O que deseja realizar?
        1- Atacar
        2- Defender
        3- Fugir
        ''')
        if opcao == '1':
            print(f"{pokemonEscolhido._nome} atacou {pokemonInimigo['nome']}!")
            pokemonEscolhido.checarVantagem(pokemonInimigo)
            print(f"{pokemonInimigo['nome']} sofreu dano e está com {pokemonInimigo['hp']} de HP")
    return print("Você venceu!")

def batalhaInimigo(pokemonsJogador, treinadorInimigo):
    treinadorInimigo = []    
    pokemonsInimigos(treinadorInimigo)
    inimigoEscolhido = treinadorInimigo[randint(0, 2)]
    print(f"O Pokemon que seu inimigo escolhe é: \n{inimigoEscolhido['nome']}")
    # pokemonEscolhido = int(input(f'''
    # Escolha qual pokemon usar:
    # 1- {pokemonsJogador[0]['nome']}
    # 2- {pokemonsJogador[1]['nome']}
    # 3- {pokemonsJogador[2]['nome']}
    # '''))
    # pokemonEscolhido = pokemonsJogador[pokemonEscolhido - 1]
    # print(f"\nVocê escolheu {pokemonEscolhido['nome']}")
    # inimigoEscolhido = treinadorInimigo[randint(0, 2)]     
    # print(f"O Pokemon que seu inimigo escolhe é: \n{inimigoEscolhido['nome']}")
    batalhaPokemon(inimigoEscolhido)

def menu():
    opcao = ''
    while(opcao != '4'):
        opcao = input('''
        Digite a opção desejada: 
        1- Capturar Pokemon
        2- Procurar batalha pokemon
        3- Exibir seus pokemons
        4- Sair
        ''')
        if opcao ==  '1':
            print("Caçando Pokemon...")
            pokemonSelvagem = pokemons[randint(0, 149)]
            print(f"{pokemonSelvagem['nome']} apareceu!")
            batalhaPokemon(pokemonSelvagem)
            print(f"Você capturou {pokemonSelvagem['nome']}")
        elif opcao == '2':            
            print("Procurando Treinador pokemon...")
            print("Inimigo: - Prepara-se para batalha!")                        
            batalhaInimigo(pokemonsJogador, treinadorInimigo)
        elif opcao == '3':
            print(f'''
            Estes são os seus pokemons:
            1- {pokemonsJogador[0]._nome}
            2- {pokemonsJogador[1]._nome}
            3- {pokemonsJogador[2]._nome}
            ''')
        elif opcao == '4':
            print("Fim de programa")
        else:
            print("Opção Inválida! Tente novamente.")

                    
escolherPokemons(pokemonsJogador)
        
# print(f'''
#     Você escolheu:
#     1- {pokemonsJogador[0]['nome']}
#     2- {pokemonsJogador[1]['nome']}
#     3- {pokemonsJogador[2]['nome']}
#     ''')
print(f'''
    Você escolheu:
    1- {pokemonsJogador[0]._nome}
    2- {pokemonsJogador[1]._nome}
    3- {pokemonsJogador[2]._nome}
    ''')
menu()           