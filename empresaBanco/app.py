from Controle.classConexao import Conexao

from Modelo.classEmpresa import Empresa
from Modelo.classEmpresa import Funcionario

def login():    
    print("Olá, bem vindo a tela de login: ")
    func = Empresa().signin()
    definitionUser(func)
    
def definitionUser(func):
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
                    con = Conexao()
                    cursor = con.db.cursor()
                    print("Digite qual dado deseja atualizar: ")
                    print('''
                        1- Nome
                        2- CPF                                     
                        ''')
                    opcao = input()
                    if opcao == '1':
                        novoNome = input("Digite o novo nome: ")
                        cursor.execute(f'''UPDATE funcionarios SET func_nome = '{novoNome}' where func_id = '{func.id}'; ''')
                        con.db.commit()
                        print("Nome atualizado com sucesso!")
                        cursor.close()
                        con.db.close()
                        
                    elif opcao == '2':
                        novoCpf = input("Digite o novo CPF: ")
                        cursor.execute(f'''UPDATE funcionarios SET func_cpf = '{novoCpf}' where func_id = '{func.id}'; ''')
                        con.db.commit()
                        print("CPF atualizado com sucesso!")
                        cursor.close()
                        con.db.close()
                case '3':
                    con = Conexao()
                    cursor = con.db.cursor()
                    con.queryUpdateLogin(cursor, func)
                    cursor.close()
                    con.db.close()
                case '4':
                    con = Conexao()
                    cursor = con.db.cursor()
                    con.queryUpdatePassword(cursor, func)
                    cursor.close()
                    con.db.close()
                case '5':
                    print("Saindo...")                    
                    return False        
                case _:
                    print("Opção inválida!")


login()
    
