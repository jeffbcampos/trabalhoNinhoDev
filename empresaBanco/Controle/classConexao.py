from psycopg2 import connect
from psycopg2 import Error
from dotenv import load_dotenv
load_dotenv()
import os
from pwinput import pwinput


class Conexao:
    def __init__(self):
        try:
            self.db = connect(host=os.getenv("HOST"), user=os.getenv("USER"), password=os.getenv("PASSWORD"), port=os.getenv("PORT"), database=os.getenv("DATABASE"))            
        except Error as err:
            print(f"Error: {err}")

    def querySelectFunc(self, cursor, id):
        cursor = self.db.cursor()
        cursor.execute(f'''
        SELECT * FROM funcionarios WHERE func_id = '{id}';
        ''')               
        return cursor.fetchall()
    
    def queryDelete(self, cursor, id):
        cursor = self.db.cursor()
        cursor.execute(f'''
            DELETE FROM funcionarios WHERE func_id = '{id}';
        ''')

    def queryCreateFunc(self, cursor, nome, cpf, salario, dept, cargo, login, senha):
        cursor = self.db.cursor()
        cursor.execute(f'''
            INSERT INTO funcionarios (func_nome, func_cpf, func_salario, dept_id, func_cargo) VALUES (
	        '{nome}', '{cpf}', {salario}, {dept}, '{cargo}');            
        ''')
        self.db.commit()
        cursor.execute(f'''SELECT func_id FROM funcionarios WHERE func_cpf = '{cpf}';''')
        id = cursor.fetchall()[0][0]
        cursor.execute(f'''INSERT INTO signin (func_id, login, senha) VALUES ('{id}', '{login}', '{senha}');''')
        self.db.commit()
    
    def queryUpdateFunc(self, cursor, novoNome, novoCpf, novoSalario, novoDept, novoCargo, funcionario):
        cursor = self.db.cursor()
        cursor.execute(f'''
            UPDATE funcionarios SET func_nome = '{novoNome}',
            func_cpf = '{novoCpf}',
            func_salario = '{novoSalario}',
            dept_id = '{novoDept}',
            func_cargo = '{novoCargo}'
            WHERE func_id = '{funcionario.id}'            
        ''')
        
    def queryUpdateLogin(self, cursor, func):
        cursor = self.db.cursor()
        novoLogin = input("Digite o novo login: ")
        confirmarSenha = pwinput("Digite a senha para confirmar: ")
        cursor.execute(f"SELECT senha FROM signin WHERE func_id = '{func.id}'")
        senha = cursor.fetchall()[0][0]
        if senha == confirmarSenha:            
            cursor.execute(f'''UPDATE signin SET login = '{novoLogin}' where func_id = '{func.id}';''')
            self.db.commit()
            print("Login atualizado com sucesso!")
        else:
            print("Senha incorreta!")
            cancelar = input("Deseja cancelar a operação? (s/n)")
            if cancelar == "s":
                return
            else:
                self.queryUpdateLogin(cursor, func)
    
    def queryUpdatePassword(self, cursor, func):
        cursor = self.db.cursor()
        senha = pwinput("Confirme sua senha antiga: ")
        cursor.execute(f'''SELECT senha FROM signin WHERE func_id = '{func.id}';''')
        senhaAntiga = cursor.fetchall()[0][0]
        if senha == senhaAntiga:
            novaSenha = pwinput("Digite a nova senha: ")
            confirmarSenha = pwinput("Confirme a nova senha: ")
            if novaSenha == confirmarSenha:
                cursor.execute(f'''UPDATE signin SET senha = '{novaSenha}' where func_id = '{func.id}';''')
                self.db.commit()
                print("Senha atualizada com sucesso!")
            else:
                print("Senhas não conferem!")
                cancelar = input("Deseja cancelar a operação? (s/n)")
                if cancelar == "s":
                    return
                else:
                    self.queryUpdatePassword(cursor, func)
    
    def verifyPwd(self, cursor, func):            
            cursor = self.db.cursor()
            cursor.execute(f'''SELECT senha from signin where func_id = {func.id};''')
            senhaBanco = cursor.fetchall()[0][0]            
            senha = pwinput("Digite sua senha para confirmar as alterações: ")
            if senha == senhaBanco:                
                return True                
            else:
                cancelar = input("Senha incorreta! Deseja tentar novamente?[s/n]: ")
                if cancelar == "s":
                    self.verifyPwd(cursor, func)
                    return True                    
                else:
                    return False
    def queryDismiss(self, cursor, func):
        cursor = self.db.cursor()
        cursor.execute(f'''UPDATE funcionarios SET func_nome = '{func.nome} (demitido)',
            func_cpf = '{func.cpf}',
            func_salario = NULL,
            dept_id = NULL,
            func_cargo = NULL
            WHERE func_id = '{func.id}';''')
        self.db.commit()
        cursor.execute(f'''DELETE FROM signin WHERE func_id = '{func.id}';''')
        self.db.commit()
        print("Funcionário demitido com sucesso!")            
    

