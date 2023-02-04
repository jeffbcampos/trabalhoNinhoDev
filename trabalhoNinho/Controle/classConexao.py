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