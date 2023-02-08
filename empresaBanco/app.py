from Controle.classConexao import Conexao
import pandas as pd
from pwinput import pwinput

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
                con = Conexao()
                cursor = con.db.cursor()
                cursor.execute(f'''SELECT f.func_id, f.func_nome as Nome, f.func_cpf as CPF, f.func_salario as Salário, f.func_cargo as Cargo from funcionarios f inner join departamentos d on f.dept_id = d.dept_id where f.dept_id = '{func.dept_id}' and f.func_cargo != 'Gerente';''')
                funcionarios = cursor.fetchall()
                for func in funcionarios:
                    funcionario = Funcionario(func[0], func[1], func[2], func[3], None, func[4])
                    print(f'''
            Nome: {funcionario.nome}
            CPF: {funcionario.cpf}
            Salário: {funcionario.salario}
            Cargo: {funcionario.cargo}''')                              
            case '2':
                con = Conexao()
                cursor = con.db.cursor()
                id = input("\nDigite o ID do funcionário que quer alterar: ")
                funcionario = Funcionario(con.querySelectFunc(cursor, id)[0][0], con.querySelectFunc(cursor, id)[0][1], con.querySelectFunc(cursor, id)[0][2], con.querySelectFunc(cursor, id)[0][3], con.querySelectFunc(cursor, id)[0][4], con.querySelectFunc(cursor, id)[0][5])
                print("\nDigite qual dado você deseja alterar: \n")
                print("1- Nome")
                print("2- CPF")
                print("3- Salario")
                print("4- Departamento")
                print("5- Cargo")
                opcao = input()
                if opcao == '1':
                    novoNome = input(f"Digite o novo nome para {funcionario.nome}: ")
                    val = con.verifyPwd(cursor, func)                     
                    if val == True:
                        con.queryUpdateFunc(cursor, novoNome, funcionario.cpf, funcionario.salario, funcionario.dept_id, funcionario.cargo, funcionario)
                        con.db.commit()
                        cursor.close()
                        con.db.close()
                        print("Alteração realizada com sucesso!")
                    else:
                        print("Cancelando operação...")
            case '3':
                con = Conexao()
                cursor = con.db.cursor()
                nome = input("Digite o nome do funcionário: ")
                cpf = input("Digite o CPF do funcionário: ")
                salario = input("Digite o salário do funcionário: ")
                dept = input("Digite o departamento do funcionário: ")
                cargo = input("Digite o cargo do funcionário: ")
                login = input("Digite o login do funcionário: ")
                senha = input("Digite a senha do funcionário: ")
                val = con.verifyPwd(cursor, func)
                if val == True:
                        con.queryCreateFunc(cursor, nome, cpf, salario, dept, cargo, login, senha)                     
                        cursor.close()
                        con.db.close()
                        print("Funcionário criado com sucesso!")
                else:
                    print("Cancelando operação...")
            case '4':
                con = Conexao()
                cursor = con.db.cursor()
                id = input("\nDigite o ID do funcionário que quer demitir: ")
                funcionario = Funcionario(con.querySelectFunc(cursor, id)[0][0], con.querySelectFunc(cursor, id)[0][1], con.querySelectFunc(cursor, id)[0][2], con.querySelectFunc(cursor, id)[0][3], con.querySelectFunc(cursor, id)[0][4], con.querySelectFunc(cursor, id)[0][5]) 
                con.queryDismiss(cursor, funcionario)
                cursor.close()
                con.db.close()  
            case '5':
                print("Saindo...")

login()
    