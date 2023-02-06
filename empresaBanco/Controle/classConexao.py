from psycopg2 import connect
from psycopg2 import Error
from dotenv import load_dotenv
load_dotenv()
import os

class Conexao:
    def __init__(self):
        try:
            self.db = connect(host=os.getenv("HOST"), user=os.getenv("USER"), password=os.getenv("PASSWORD"), port=os.getenv("PORT"), database=os.getenv("DATABASE"))
            print("Conexão realizada com sucesso")
        except Error as err:
            print(f"Error: {err}")

    def querySelect(self, cursor, id):
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

    def queryCreate(self, cursor, nome, cpf, salario, dept, cargo):
        cursor = self.db.cursor()
        cursor.execute(f'''
            INSERT INTO funcionarios (func_nome, func_cpf, func_salario, dept_id, func_cargo) VALUES (
	        '{nome}', '{cpf}', {salario}, {dept}, '{cargo}');
        ''')
    
    def queryUpdate(self, cursor, novoNome, novoCpf, novoSalario, novoDept, novoCargo):
        cursor = self.db.cursor()
        cursor.execute(f'''
            UPDATE funcionarios SET func_nome = '{novoNome}',
            func_cpf = '{novoCpf}',
            func_salario = {novoSalario},
            dept_id = {novoDept},
            func_cargo = {novoCargo}
        ''')


