from Controle.classConexao import Conexao

from Modelo.classEmpresa import Empresa
from Modelo.classEmpresa import Funcionario


con = Conexao()

cursor = con.db.cursor()

cursor.execute('''SELECT * FROM funcionarios where func_id = '7'; ''')

dadosFunc = cursor.fetchall()[0]

func = Funcionario(dadosFunc[0], dadosFunc[1], dadosFunc[2], dadosFunc[3], dadosFunc[4], dadosFunc[5])

func.signin()


