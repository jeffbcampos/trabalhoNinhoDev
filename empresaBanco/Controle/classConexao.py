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

    def querySelectAllFuncs(self, cursor, id):
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

    def queryCreateFunc(self, cursor, nome, cpf, salario, dept, cargo):
        cursor = self.db.cursor()
        cursor.execute(f'''
            INSERT INTO funcionarios (func_nome, func_cpf, func_salario, dept_id, func_cargo) VALUES (
	        '{nome}', '{cpf}', {salario}, {dept}, '{cargo}');
        ''')
        self.db.commit()
    
    def queryUpdateFunc(self, cursor, novoNome, novoCpf, novoSalario, novoDept, novoCargo):
        cursor = self.db.cursor()
        cursor.execute(f'''
            UPDATE funcionarios SET func_nome = '{novoNome}',
            func_cpf = '{novoCpf}',
            func_salario = {novoSalario},
            dept_id = {novoDept},
            func_cargo = {novoCargo}
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
        cursor.execute(f"SELECT senha FROM signin WHERE func_id = '{func.id}'")
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
        
    


