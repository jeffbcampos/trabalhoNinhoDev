from Controle.classConexao import Conexao
from pwinput import pwinput
from psycopg2 import Error
  

class Empresa:
    def __init__(self) -> None:
        pass

    def signin(self):            
        while True:
            id = input("Digite o seu ID: ")
            query = f'''SELECT login, senha from signin where func_id = '{id}'; '''
            loginBanco = Conexao().querySelect(query)
            if loginBanco == []:
                print("ID inválido. Digite Novamente!")
            else:
                while True:
                    login = loginBanco[0][0]
                    senha = loginBanco[0][1]
                    loginUser = input("Digite seu login: ")
                    if loginUser == login:
                        senhaUser = pwinput("Digite sua senha: ")
                        if senhaUser == senha:
                            print("Login realizado com sucesso!")
                            query = f'''SELECT * FROM funcionarios where func_id = '{id}' '''
                            funcDados = Conexao().querySelect(query)[0]
                            if funcDados[5] == "Gerente":
                                func = Gerente(funcDados[0],funcDados[1],funcDados[2],funcDados[3],funcDados[4],funcDados[5])                                                  
                                return func
                            else:
                                func = Funcionario(funcDados[0],funcDados[1],funcDados[2],funcDados[3],funcDados[4],funcDados[5])                                               
                                return func                                                      
                        else:
                            print("Senha Inválida!")
                    else:
                        print("Login Inválido!")     
                break

class Funcionario(Empresa):
    def __init__(self, login, senha):
        super().__init__(login, senha)        
    def __init__(self, func_id, func_nome, func_cpf, func_salario, dept_id, func_cargo):
        self.id = func_id
        self.nome = func_nome
        self.cpf = func_cpf
        self.salario = func_salario
        self.dept_id = dept_id
        self.cargo = func_cargo

    def getNome(self):
        return self.nome
    
    def getCpf(self):
        return self.cpf
    
    def getSalario(self):
        return self.salario
    
    def getDept(self):
        return self.dept_id

    def getCargo(self):
        return self.cargo

    def funcDados(self):
        print("\nImprimindo Dados do Funcionario:\n")
        print(f"ID: {self.id}")
        print(f"Nome: {self.getNome()}")
        print(f"CPF: {self.getCpf()}")
        print(f"Salário: {self.getSalario()}")
        print(f"ID Departamento: {self.getDept()}")
        print(f"Cargo: {self.getCargo()}\n")
    
    def queryUpdateName(self, func):
        novoNome = input("Digite o novo nome: ")
        query = f'''UPDATE funcionarios SET func_nome = '{novoNome}' where func_id = '{func.id}'; '''    
        Conexao().queryExecute(query)                        
        print("Nome atualizado com sucesso!")
        
        
    def queryUpdateCpf(self, func):
        novoCpf = input("Digite o novo cpf: ")
        query = f'''UPDATE funcionarios SET func_cpf = '{novoCpf}' where func_id = '{func.id}'; '''    
        Conexao().queryExecute(query)                        
        print("CPF atualizado com sucesso!")
        
        
    def queryUpdateLogin(self, func):        
        novoLogin = input("Digite o novo login: ")                      
        val = self.verifyPwd(func)
        if val == True:
            query = f'''
            UPDATE signin SET login = '{novoLogin}' where func_id = '{func.id}'; '''
            Conexao().queryExecute(query)                                
            print("Atualização de Login realizado com sucesso!")
        else:
            print("Cancelando operação...")
            
    def queryUpdatePwd(self, func):        
        novaSenha = pwinput("Digite a nova senha: ")                       
        val = self.verifyPwd(func)
        if val == True:
            query = f'''
            UPDATE signin SET senha = '{novaSenha}' where func_id = '{func.id}'; '''
            Conexao().queryExecute(query)                                
            print("Atualização de Senha realizada com sucesso!")
            
        else:
            print("Cancelando operação...")
            
    
    def verifyPwd(self, func):            
            query = f'''SELECT senha from signin where func_id = {func.id};'''            
            senhaBanco = Conexao().querySelect(query)[0][0]            
            senha = pwinput("Digite sua senha para confirmar as alterações: ")
            if senha == senhaBanco:                                               
                return True                                
            else:
                cancelar = input("Senha incorreta! Deseja tentar novamente?[s/n]: ")
                if cancelar == "s":
                    self.verifyPwd(func)                    
                    return True                    
                else:                                        
                    return False
        
class Gerente(Empresa):
    def __init__(self, login, senha):
        super().__init__(login, senha)                              
    
    def __init__(self, func_id, func_nome, func_cpf, func_salario, dept_id, func_cargo):
        self.id = func_id
        self.nome = func_nome
        self.cpf = func_cpf
        self.salario = func_salario
        self.dept_id = dept_id
        self.cargo = func_cargo        
        
        
    def verificaEquipe(self, func):       
        query = f'''SELECT func_id, func_nome, func_cpf, func_salario, func_cargo from funcionarios where dept_id = '{func.dept_id}' and func_cargo != 'Gerente';'''        
        funcionarios = Conexao().querySelect(query)        
        for func in funcionarios:
            funcionario = Funcionario(func[0], func[1], func[2], func[3], None, func[4])
            print(f'''
        Nome: {funcionario.nome}
        CPF: {funcionario.cpf}
        Salário: {funcionario.salario}
        Cargo: {funcionario.cargo}''')                
        
    def querySelectFunc(self, id):        
        query = f'''SELECT * FROM funcionarios WHERE func_id = '{id}';'''        
        func = Conexao().querySelect(query)                              
        return func
    
    def verifyPwd(self, func):            
        query = f'''SELECT senha from signin where func_id = {func.id};'''            
        senhaBanco = Conexao().querySelect(query)[0][0]            
        senha = pwinput("Digite sua senha para confirmar as alterações: ")
        if senha == senhaBanco:                               
            return True                                
        else:
            cancelar = input("Senha incorreta! Deseja tentar novamente?[s/n]: ")
            if cancelar == "s":
                self.verifyPwd(func)                
                return True                    
            else:                                    
                return False            
                
    def queryUpdateFunc(self, novoNome, novoCpf, novoSalario, novoDept, novoCargo, funcionario):        
        query = f'''
            UPDATE funcionarios SET func_nome = '{novoNome}',
            func_cpf = '{novoCpf}',
            func_salario = '{novoSalario}',
            dept_id = '{novoDept}',
            func_cargo = '{novoCargo}'
            WHERE func_id = '{funcionario.id}'            
        '''
        Conexao().queryExecute(query)
        
        
    def queryCreateFunc(self, func):
        nome = input("Digite o nome do funcionário: ")
        cpf = input("Digite o CPF do funcionário: ")
        salario = input("Digite o salário do funcionário: ")
        dept = input("Digite o departamento do funcionário: ")
        cargo = input("Digite o cargo do funcionário: ")
        login = input("Digite o login do funcionário: ")
        senha = pwinput("Digite a senha do funcionário: ")
        val = self.verifyPwd(func)
        if val == True:
            query = f'''
            INSERT INTO funcionarios (func_nome, func_cpf, func_salario, dept_id, func_cargo) VALUES (
	        '{nome}', '{cpf}', {salario}, {dept}, '{cargo}');'''
            Conexao().queryExecute(query)
            query = f'''SELECT func_id FROM funcionarios WHERE func_cpf = '{cpf}';'''
            id = Conexao().querySelect(query)[0][0]
            query =  f'''INSERT INTO signin (func_id, login, senha) VALUES ('{id}', '{login}', '{senha}');'''
            Conexao().queryExecute(query)                     
            print("Funcionário criado com sucesso!")
        else:
            print("Cancelando operação...")
        
            
    def queryDismiss(self, func):
        id = input("\nDigite o ID do funcionário que quer demitir: ")        
        funcionario = Funcionario(self.querySelectFunc(id)[0][0], self.querySelectFunc(id)[0][1], self.querySelectFunc(id)[0][2], self.querySelectFunc(id)[0][3], self.querySelectFunc(id)[0][4], self.querySelectFunc(id)[0][5])      
        print(f"Funcionário {funcionario.nome} selecionado")
        val = self.verifyPwd(func)
        if val == True:      
            query = f'''UPDATE funcionarios SET func_nome = '{funcionario.nome} (demitido)',
                func_cpf = '{funcionario.cpf}',
                func_salario = NULL,
                dept_id = NULL,
                func_cargo = NULL
                WHERE func_id = '{funcionario.id}';'''
            Conexao().queryExecute(query)
            query = f'''DELETE FROM signin WHERE func_id = '{funcionario.id}';'''        
            Conexao().queryExecute(query)        
            print("Funcionário demitido com sucesso!")
        else:
            print("Cancelando operação...")
                   