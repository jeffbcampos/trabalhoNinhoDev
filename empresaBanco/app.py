from Modelo.classEmpresa import Empresa
from Modelo.classEmpresa import Funcionario

def login():    
    print("Olá, bem vindo a tela de login: ")
    func = Empresa().signin() # A FUNÇÃO SIGNIN RETORNARÁ UM FUNCIONÁRIO DO BANCO DE DADOS VALIDANDO LOGIN E SENHA 
    definitionUser(func) 
    
def definitionUser(func): # ESTA FUNÇÃO DEFINIRÁ SE O USUÁRIO É GERENTE OU FUNCIONÁRIO QUALQUER PARA DETERMINAR QUAL MENU SERÁ ATIVADO
    
    if func.cargo == 'Gerente':
        menuGerente(func)
    else:
        menuFunc(func)
        
        
def menuFunc(func):    
        print(f"Olá, {func.nome}, bem vindo ao Sistema!")
        while True:
            print("O que deseja fazer?")
            print('''
                1- Ver Salário
                2- Atualizar Dados
                3- Alterar login
                4- Alterar senha
                5- Sair
                ''')
            opcao = input()
            match opcao:
                case '1':
                    print(f"Seu salário atual é {func.salario}")                
                case '2':                   
                    print("Digite qual dado deseja atualizar: ")
                    print('''
                        1- Nome
                        2- CPF                                     
                        ''')
                    opcao = input()
                    if opcao == '1':
                        func.queryUpdateName(func)                                           
                    elif opcao == '2':
                        func.queryUpdateCpf(func)                       
                case '3':                    
                    func.queryUpdateLogin(func)                    
                case '4':                    
                    func.queryUpdatePwd(func)                    
                case '5':
                    print("Saindo...")
                    func.closeConnection()                                       
                    break        
                case _:
                    print("Opção inválida!")

def menuGerente(func):
    print(f"Bem vindo {func.nome}")
    while True:
        print("\nO que deseja realizar: ")
        print('''
              1- Ver sua equipe
              2- Alterar Dados de um funcionário
              3- Adicionar funcionáro
              4- Desligar funcionário da Empresa
              5- Sair''')
        opcao = input()
        match opcao:
            case '1':
                func.verificaEquipe(func)                              
            case '2':                
                id = input("\nDigite o ID do funcionário que quer alterar: ")
                dadosFunc = func.querySelectFunc(id)
                funcionario = Funcionario(dadosFunc[0][0], dadosFunc[0][1], dadosFunc[0][2], dadosFunc[0][3], dadosFunc[0][4], dadosFunc[0][5])
                print("\nDigite qual dado você deseja alterar: \n")
                print("1- Nome")
                print("2- CPF")
                print("3- Salario")
                print("4- Departamento")
                print("5- Cargo")
                opcao = input()
                if opcao == '1':
                    novoNome = input(f"Digite o novo nome para {funcionario.nome}: ")
                    val = func.verifyPwd(func)                     
                    if val == True:
                        func.queryUpdateFunc(novoNome, funcionario.cpf, funcionario.salario, funcionario.dept_id, funcionario.cargo, funcionario)                        
                        print("Alteração realizada com sucesso!")
                    else:
                        print("Cancelando operação...")
                if opcao == '2':
                    novoCpf = input(f"Digite o novo CPF para {funcionario.nome}: ")
                    val = func.verifyPwd(func)                     
                    if val == True:
                        func.queryUpdateFunc(funcionario.nome, novoCpf, funcionario.salario, funcionario.dept_id, funcionario.cargo, funcionario)                        
                        print("Alteração realizada com sucesso!")
                    else:
                        print("Cancelando operação...")
                if opcao == '3':
                    novoSalario = input(f"Digite o novo salário para {funcionario.nome}: ")
                    val = func.verifyPwd(func)                     
                    if val == True:
                        func.queryUpdateFunc(funcionario.nome, funcionario.cpf, novoSalario, funcionario.dept_id, funcionario.cargo, funcionario)                        
                        print("Alteração realizada com sucesso!")
                    else:
                        print("Cancelando operação...")
                if opcao == '4':
                    novoDept = input(f"Digite o id do novo departamento para {funcionario.nome}: ")
                    val = func.verifyPwd(func)                     
                    if val == True:
                        func.queryUpdateFunc(funcionario.nome, funcionario.cpf, funcionario.salario, novoDept, funcionario.cargo, funcionario)                        
                        print("Alteração realizada com sucesso!")
                    else:
                        print("Cancelando operação...")
                if opcao == '5':
                    novoCargo = input(f"Digite o novo cargo de {funcionario.nome}: ")
                    val = func.verifyPwd(func)                     
                    if val == True:
                        func.queryUpdateFunc(funcionario.nome, funcionario.cpf, funcionario.salario, funcionario.dept_id, novoCargo, funcionario)                        
                        print("Alteração realizada com sucesso!")
                    else:
                        print("Cancelando operação...")
            case '3':                
                func.queryCreateFunc(func)
            case '4':                
                func.queryDismiss(func)                  
            case '5':
                print("Saindo...")
                func.closeConnection()
                break
            
login()
    