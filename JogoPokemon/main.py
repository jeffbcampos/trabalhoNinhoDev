# Jogo Pokemon simples em python baseado em classes e subclasses 

from pokedex import pokemons
from random import randint
import classPokemon
from random import choice
import classTreinador

nomes_esquisitos = ['Xanthe', 'Uvularia', 'Mephitis', 'Jyoti', 'Huxley', 'Flaminia', 'Eurydice', 'Quirinus', 'Pemba', 'Oread']
treinadorInimigo = []
pokemonsJogador = []
opcao = ''
vencedor = False
pcDoBill = []

# def pokemonsInimigos(treinadorInimigo):   #Laço for pra gerar a lista de 6 pokemons de cada treinador inimigo 
#     for p in range(0, 3):
#         # pokemonAleatorio = pokemons[randint(0, 149)]
#         pokemonAleatorio = choice(pokemons)        
#         treinadorInimigo.append(classPokemon.adicionarClassePokemon(pokemonAleatorio))
#     print(f'''Os pokemons do seu Inimigo são:\n
#             1- {treinadorInimigo[0].getNome()}
#             2- {treinadorInimigo[1].getNome()}
#             3- {treinadorInimigo[2].getNome()}
#             ''')
#     return treinadorInimigo

# def escolherPokemons(pokemonsJogador): #Função Jogador escolher seus pokemons!
#     for p in range(0, 3):
#         pokemonJogador = input(f'Digite o {p + 1}º pokemon da sua equipe: ').capitalize()
#         for pokemon in pokemons:
#             if pokemonJogador == pokemon['nome']:
#                 pokemonsJogador.append(classPokemon.adicionarClassePokemon(pokemon))                      
    
#     while(len(pokemonsJogador) < 3):
#         pokemonsJogador.clear()
#         print("Algum dos pokemons não foi digitado corretamente!Escolha Novamente!")        
#         escolherPokemons(pokemonsJogador)

#     return pokemonsJogador

def evase(pokemonJogador, pokemonAdversario):
    sorteJogador = randint(0, 10)
    sorteInimigo = randint(0, 10)
    if sorteJogador > sorteInimigo:
        pokemonJogador.checarVantagem(pokemonAdversario)
    else:
        print("Errou o ataque!")

def escolherPokemon():
    controle = 0    
    while controle == 0:
        print("Escolha qual pokemon usar:\n")        
        for i in range(len(pokemonsJogador)):
                print(f"{i + 1} - {pokemonsJogador[i].getNome()}")
        print("4 - Fugir")
        pokemonEscolhido = input("")        
        # pokemonEscolhido = input(f'''
        # Escolha qual pokemon usar:\n
        # 1- {pokemonsJogador[0].getNome()}
        # 2- {pokemonsJogador[1].getNome()}
        # 3- {pokemonsJogador[2].getNome()}        
        # 4- Fugir
        # ''')
        if pokemonEscolhido == '1' or pokemonEscolhido == '2' or pokemonEscolhido == '3':
            if pokemonsJogador[int(pokemonEscolhido) - 1]._hp == 0:
                print(f"{pokemonsJogador[int(pokemonEscolhido) - 1].getNome()} está desmaiado, não pode ser usado!")
            else:
                controle = 1
        elif pokemonEscolhido == '4':
            print("\nVocê fugiu!")
            global vencedor
            vencedor = False
            break        
        else:
            print("\nOpção Inválida!")
        
    return int(pokemonEscolhido)
            

def batalhaPokemon(pokemonInimigo):    
    pokemonEscolhido = escolherPokemon()       
    while True:
        if pokemonEscolhido == 4:
            break
        pokemonEscolhido = pokemonsJogador[pokemonEscolhido - 1]     
        print(f"\nVocê escolheu {pokemonEscolhido.getNome()}")
        opcao = ''
        potion = 3    
        while(pokemonInimigo._hp > 0 and pokemonEscolhido._hp > 0):            
            while opcao != '1' or opcao != '2':                
                opcao = input("\nO que deseja realizar?\n\n1- Atacar\n2- Usar Porção(Curar 10 de HP)\n")
                if opcao == '1':                
                    print(f"\n{pokemonEscolhido.getNome()} atacou {pokemonInimigo.getNome()}!")
                    evase(pokemonEscolhido, pokemonInimigo)                    
                    if pokemonInimigo._hp > 0:                
                        print(f"\nO HP de {pokemonInimigo.getNome()} é {pokemonInimigo._hp}")
                        ataqueInimigo(pokemonEscolhido, pokemonInimigo)
                        break                 
                    else:
                        pokemonInimigo._hp = 0
                        print(f"\nO HP de {pokemonInimigo.getNome()} é {pokemonInimigo._hp}")
                        global vencedor                    
                        vencedor = True                    
                        return print("\nVocê venceu!")
                    
                elif opcao == '2':                    
                    if potion > 0:
                        for pokemon in pokemons:
                            if pokemonEscolhido.getNome() == pokemon['nome']:
                                if pokemonEscolhido._hp == pokemon["hp"]:
                                    print("Não Pode curar pois o HP está cheio!")                                                 
                                else:
                                    potion -= 1
                                    pokemonEscolhido._hp += 10
                                    if pokemonEscolhido._hp > pokemon["hp"]:
                                        pokemonEscolhido._hp = pokemon["hp"]
                                        print(f"Você curou {pokemonEscolhido.getNome()}=")
                                        print(f"O HP de {pokemonEscolhido.getNome()} é: {pokemonEscolhido._hp}")
                                        ataqueInimigo(pokemonEscolhido, pokemonInimigo)
                                    else:
                                        print(f"Você curou {pokemonEscolhido.getNome()}")
                                        print(f"O HP de {pokemonEscolhido.getNome()} é: {pokemonEscolhido._hp}")
                                        ataqueInimigo(pokemonEscolhido, pokemonInimigo)
                                        
                        break
                    else:
                        print("Suas Porções de Cura acabaram!")                        
                                                                    
                else:
                    print("\nOpção inválida!")            
            if pokemonEscolhido._hp > 0:
                print(f"\nO HP de {pokemonEscolhido.getNome()} é {pokemonEscolhido._hp}")
            else:
                pokemonEscolhido._hp = 0
                print(f"\nO HP de {pokemonEscolhido.getNome()} é {pokemonEscolhido._hp}")      
                vencedor = False                
                return print("\nVocê Perdeu!")
            # print("\nSeu Inimigo está preparando para atacar...")    
            # print(f"\n{pokemonInimigo.getNome()} atacou {pokemonEscolhido.getNome()}!")
            # evase(pokemonInimigo, pokemonEscolhido)            
            # if pokemonEscolhido._hp > 0:
            #     print(f"\nO HP de {pokemonEscolhido.getNome()} é {pokemonEscolhido._hp}")
            # else:
            #     pokemonEscolhido._hp = 0
            #     print(f"\nO HP de {pokemonEscolhido.getNome()} é {pokemonEscolhido._hp}")                
            #     vencedor = False                
            #     return print("\nVocê Perdeu!")  
                       

def ataqueInimigo(pokemonEscolhido, pokemonInimigo):
    print("\nSeu Inimigo está preparando para atacar...")    
    print(f"\n{pokemonInimigo.getNome()} atacou {pokemonEscolhido.getNome()}!")
    evase(pokemonInimigo, pokemonEscolhido)            
    

def batalhaInimigo(treinadorInimigo):
    treinadorInimigo = []
    nomeInimigo = choice(nomes_esquisitos)
    playerInimigo = classTreinador.TreinadorInimigo(nomeInimigo, treinadorInimigo)    
    #pokemonsInimigos(treinadorInimigo)
    playerInimigo.pokemonInicial()
    print(f"Você encontrou o Treinador {playerInimigo._nome}")
    print(f"\n{playerInimigo._nome}: - Prepara-se para batalha!")
    inimigoEscolhido = choice(treinadorInimigo)#treinadorInimigo[randint(0, 2)]
    print(f"\nO Pokemon que {playerInimigo.getNome()} escolhe é: \n\n{inimigoEscolhido.getNome()}")    
    batalhaPokemon(inimigoEscolhido)


def centroPokemon(pokemonsJogador):
    for p in range(len(pokemonsJogador)):
        for pokemon in pokemons:
            if pokemonsJogador[p].getNome() == pokemon['nome']:
                pokemonsJogador[p]._hp = pokemon['hp']


def menu():
    opcaoMenu = ''
    while(opcaoMenu != '5'):
        opcaoMenu = input('''
        Digite a opção desejada:\n 
        1- Capturar Pokemon
        2- Procurar batalha pokemon
        3- Exibir seus pokemons
        4- Curar pokemons
        5- Sair
        ''')
        if opcaoMenu ==  '1':
            print("\nCaçando Pokemon...")
            pokemonSelvagem = choice(pokemons)#pokemons[randint(0, 149)]
            pokemonSelvagem = classPokemon.adicionarClassePokemon(pokemonSelvagem)                       
            print(f"\n{pokemonSelvagem.getNome()} apareceu!")
            batalhaPokemon(pokemonSelvagem)
            if vencedor == True:
                if len(pokemonsJogador) < 3:
                    print(f"Você capturou {pokemonSelvagem.getNome()}")
                    pokemonsJogador.append(pokemonSelvagem)
                else:
                    print(f"Você capturou {pokemonSelvagem.getNome()}")
                    pcDoBill.append(pokemonSelvagem)
                    print("Você não pode carregar mais de 3 pokemons. Enviado para o PC do Bill")
        elif opcaoMenu == '2':            
            print("\nProcurando Treinador pokemon...")                     
            batalhaInimigo(treinadorInimigo)
        elif opcaoMenu == '3':
            player1.mostrarPokemons()
            print("\n\nPokemons Guardados no PC do Bill:\n")
            for i in range(len(pcDoBill)):
                print(f"{i + 1} - {pcDoBill[i].getNome()}")
            # print(f'''
            # Estes são os seus pokemons:
            # 1- {pokemonsJogador[0].getNome()}
            # 2- {pokemonsJogador[1].getNome()}
            # 3- {pokemonsJogador[2].getNome()}
            # ''')
        elif opcaoMenu == '4':
            print("Curando pokemons...")
            centroPokemon(pokemonsJogador)
            print("Pokemons Curados!\n")
            for i in range(len(pokemonsJogador)):
                print(f"{i + 1} - {pokemonsJogador[i].getNome()}: {pokemonsJogador[i]._hp}")
            # print(f'''
            # {pokemonsJogador[0].getNome()}: {pokemonsJogador[0]._hp}
            # {pokemonsJogador[1].getNome()}: {pokemonsJogador[1]._hp}
            # {pokemonsJogador[2].getNome()}: {pokemonsJogador[2]._hp}
            # ''')
            
        elif opcaoMenu == '5':
            print("Fim de programa")            
        else:
            print("\nOpção Inválida! Tente novamente.")

                    
#escolherPokemons(pokemonsJogador)
nomeJogador = input("Parabéns, você é o mais novo treinador pokemon de Pallet, me diga qual é o seu nome: ")
player1 = classTreinador.Treinador(nomeJogador, pokemonsJogador)
player1.pokemonInicial()
print(f'Seu primeiro pokemon é: {pokemonsJogador[0].getNome()}')
# print(f'''
#     Você escolheu:\n
#     1- {pokemonsJogador[0].getNome()}
#     2- {pokemonsJogador[1].getNome()}
#     3- {pokemonsJogador[2].getNome()}
#     ''')

menu()           
