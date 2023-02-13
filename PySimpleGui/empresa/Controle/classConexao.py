from psycopg2 import connect
from psycopg2 import Error
from dotenv import load_dotenv
load_dotenv()
import os



class Conexao:
    def __init__(self):
        try:
            self.db = connect(host=os.getenv("HOST"), user=os.getenv("USER"), password=os.getenv("PASSWORD"), port=os.getenv("PORT"), database=os.getenv("DATABASE"))            
        except Error as err:
            print(f"Error: {err}")
            
    def querySelect(self, query):                       
        cursor = self.db.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        Conexao().db.close()                
        return result
    
    def queryExecute(self, query):
        con = self.db                       
        cursor = self.db.cursor()
        cursor.execute(query)
        con.commit()        
        cursor.close()
        Conexao().db.close()
              
    

    