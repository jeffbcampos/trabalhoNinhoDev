from pokedex import pokemons
from random import randint
import classPokemon

treinadorInimigo = []
pokemonsJogador = []
opcao = ''

def pokemonsInimigos(treinadorInimigo):   #Laço for pra gerar a lista de 6 pokemons de cada treinador inimigo 
    for p in range(0, 3):
        pokemonAleatorio = pokemons[randint(0, 149)]        
        treinadorInimigo.append(classPokemon.adicionarClassePokemon(pokemonAleatorio))
    print(f'''Os pokemons do seu Inimigo são:
            1- {treinadorInimigo[0].getNome()}
            2- {treinadorInimigo[1].getNome()}
            3- {treinadorInimigo[2].getNome()}
            ''')
    return treinadorInimigo

def escolherPokemons(pokemonsJogador): #Função Jogador escolher seus pokemons!
    for p in range(0, 3):
        pokemonJogador = input(f'Digite o {p + 1}º pokemon da sua equipe: ').capitalize()
        for pokemon in pokemons:
            if pokemonJogador == pokemon['nome']:
                pokemonsJogador.append(classPokemon.adicionarClassePokemon(pokemon))                      
    
    while(len(pokemonsJogador) < 3):
        pokemonsJogador.clear()
        print("Algum dos pokemons não foi digitado corretamente!Escolha Novamente!")        
        escolherPokemons(pokemonsJogador)

    return pokemonsJogador


def batalhaPokemon(pokemonInimigo):
    pokemonEscolhido = int(input(f'''
    Escolha qual pokemon usar:
    1- {pokemonsJogador[0].getNome()}
    2- {pokemonsJogador[1].getNome()}
    3- {pokemonsJogador[2].getNome()}
    '''))
    pokemonEscolhido = pokemonsJogador[pokemonEscolhido - 1]
    print(f"Você escolheu {pokemonEscolhido.getNome()}")
    opcao = ''
    while(pokemonInimigo._hp > 0):
        opcao = input('''
        O que deseja realizar?
        1- Atacar
        2- Defender
        3- Fugir
        ''')
        if opcao == '1':
            print(f"{pokemonEscolhido.getNome()} atacou {pokemonInimigo.getNome()}!")
            pokemonEscolhido.checarVantagem(pokemonInimigo)
            if pokemonInimigo._hp >= 0:
                print(f"{pokemonInimigo.getNome()} sofreu dano e está com {pokemonInimigo._hp} de HP")
            else:
                pokemonInimigo._hp = 0
                print(f"{pokemonInimigo.getNome()} sofreu dano e está com {pokemonInimigo._hp} de HP")
    return print("Você venceu!")

def batalhaInimigo(pokemonsJogador, treinadorInimigo):
    treinadorInimigo = []    
    pokemonsInimigos(treinadorInimigo)
    inimigoEscolhido = treinadorInimigo[randint(0, 2)]
    print(f"O Pokemon que seu inimigo escolhe é: \n{inimigoEscolhido.getNome()}")    
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
            pokemonSelvagem = classPokemon.adicionarClassePokemon(pokemonSelvagem)                       
            print(f"{pokemonSelvagem.getNome()} apareceu!")
            batalhaPokemon(pokemonSelvagem)
            print(f"Você capturou {pokemonSelvagem.getNome()}")
        elif opcao == '2':            
            print("Procurando Treinador pokemon...")
            print("Inimigo: - Prepara-se para batalha!")                        
            batalhaInimigo(pokemonsJogador, treinadorInimigo)
        elif opcao == '3':
            print(f'''
            Estes são os seus pokemons:
            1- {pokemonsJogador[0].getNome()}
            2- {pokemonsJogador[1].getNome()}
            3- {pokemonsJogador[2].getNome()}
            ''')
        elif opcao == '4':
            print("Fim de programa")
        else:
            print("Opção Inválida! Tente novamente.")

                    
escolherPokemons(pokemonsJogador)

print(f'''
    Você escolheu:
    1- {pokemonsJogador[0].getNome()}
    2- {pokemonsJogador[1].getNome()}
    3- {pokemonsJogador[2].getNome()}
    ''')

menu()           