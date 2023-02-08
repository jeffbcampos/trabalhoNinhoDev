from Controle.classConexao import Conexao
from pwinput import pwinput

class Empresa:
    def __init__(self) -> None:
        pass

    def signin(self):
        con = Conexao()
        cursor = con.db.cursor()
        while True:
            id = input("Digite o seu ID: ")
            cursor.execute(f'''SELECT login, senha from signin where func_id = '{id}'; ''')
            loginBanco = cursor.fetchall()
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
                            cursor.execute(f'''SELECT * FROM funcionarios where func_id = '{id}' ''')
                            funcDados = cursor.fetchall()[0]
                            func = Funcionario(funcDados[0],funcDados[1],funcDados[2],funcDados[3],funcDados[4],funcDados[5])
                            cursor.close()
                            con.db.close()
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
