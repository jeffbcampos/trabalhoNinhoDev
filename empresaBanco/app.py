from Controle.classConexao import Conexao
from Modelo.classFuncionario import Funcionario
from Modelo.classEmpresa import Empresa


con = Conexao()

cursor = con.db.cursor

query = con.querySelect(cursor, 7)[0]

func = Funcionario(query[0],query[1],query[2],query[3],query[4],query[5])

func.funcDados()

