from Controle.classConexao import Conexao

con = Conexao()

class Biblioteca:
    def __init__(self, livro_id, livro_nome, livro_paginas, livro_ano, livro_autor):
        self.id = livro_id
        self.nome = livro_nome
        self.paginas = livro_paginas
        self.ano = livro_ano
        self.autor = livro_autor

    def listarLivro(self):
        print("Livros disponiveis na biblioteca:")
        livros = self.getLivros()
        for livro in livros:
            print(f"ID: {livro[0]}")
            print(f"Nome: {livro[1]}")
            print(f"Páginas: {livro[2]}")
            print(f"Ano: {livro[3]}")
            print(f"Autor: {livro[4]}")
            print("\n=====================================\n")

    def getLivros(self):
        query = "SELECT * FROM livros"
        livros = con.querySelect(query)        
        return livros
    
    def cadastrarLivro(self):
        self.nome = input("Digite o nome do livro: ")
        self.paginas = int(input("Digite a quantidade de páginas: "))
        self.ano = int(input("Digite o ano de lançamento: "))
        self.autor = input("Digite o nome do autor: ")
        query = f"INSERT INTO livros (livro_nome, livro_paginas, livro_ano, livro_autor) VALUES ('{self.nome}', {self.paginas}, {self.ano}, '{self.autor}')"
        con.queryExecute(query)
        print("Livro cadastrado com sucesso")
        

    def atualizarLivro(self):
        self.id = int(input("Digite o ID do livro que deseja atualizar: "))
        while not self.validacaoBuscaLivro(self.id):
            print("ID inválido")
            self.id = int(input("Digite o ID do livro que deseja atualizar: "))
        self.nome = input("Digite o novo nome do livro: ")
        self.paginas = int(input("Digite a nova quantidade de páginas: "))
        self.ano = int(input("Digite o novo ano de lançamento: "))
        self.autor = input("Digite o novo nome do autor: ")
        query = f"UPDATE livros SET livro_nome='{self.nome}', livro_paginas={self.paginas}, livro_ano={self.ano}, livro_autor='{self.autor}' WHERE livro_id={self.id}"
        con.queryExecute(query)
        print("Livro atualizado com sucesso")

    def deletarLivro(self):
        self.id = int(input("Digite o ID do livro que deseja deletar: "))
        while not self.validacaoBuscaLivro(self.id):
            print("ID inválido")
            self.id = int(input("Digite o ID do livro que deseja deletar: "))
            query = f"DELETE FROM livros WHERE livro_id={self.id}"
        con.queryExecute(query)
        print("Livro deletado com sucesso")
    
    def validacaoBuscaLivro(self, id):
        livros = self.getLivros()
        for livro in livros:
            if livro[0] == id:
                return True
        return False
    
    def closeConnection(self):
        return con.db.close()