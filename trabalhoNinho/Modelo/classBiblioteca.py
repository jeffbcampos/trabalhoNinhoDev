class Biblioteca:
    def __init__(self, livro_id, livro_nome, livro_paginas, livro_ano, livro_autor):
        self.id = livro_id
        self.nome = livro_nome
        self.paginas = livro_paginas
        self.ano = livro_ano
        self.autor = livro_autor

    def listarLivro(self, cursor):
        print("Livros disponiveis na biblioteca:")
        livros = self.getLivros(cursor)
        for livro in livros:
            print(f"ID: {livro[0]}")
            print(f"Nome: {livro[1]}")
            print(f"Páginas: {livro[2]}")
            print(f"Ano: {livro[3]}")
            print(f"Autor: {livro[4]}")
            print("=====================================")

    def getLivros(self, cursor):
        cursor.execute("SELECT * FROM livros")
        livros = cursor.fetchall()
        return livros
    
    def cadastrarLivro(self, cursor):
        self.nome = input("Digite o nome do livro: ")
        self.paginas = int(input("Digite a quantidade de páginas: "))
        self.ano = int(input("Digite o ano de lançamento: "))
        self.autor = input("Digite o nome do autor: ")
        cursor.execute(f"INSERT INTO livros (livro_nome, livro_paginas, livro_ano, livro_autor) VALUES ('{self.nome}', {self.paginas}, {self.ano}, '{self.autor}')")
        print("Livro cadastrado com sucesso")
        

    def atualizarLivro(self, cursor):
        self.id = int(input("Digite o ID do livro que deseja atualizar: "))
        self.nome = input("Digite o novo nome do livro: ")
        self.paginas = int(input("Digite a nova quantidade de páginas: "))
        self.ano = int(input("Digite o novo ano de lançamento: "))
        self.autor = input("Digite o novo nome do autor: ")
        cursor.execute(f"UPDATE livros SET livro_nome='{self.nome}', livro_paginas={self.paginas}, livro_ano={self.ano}, livro_autor='{self.autor}' WHERE livro_id={self.id}")
        print("Livro atualizado com sucesso")

    def deletarLivro(self, cursor):
        self.id = int(input("Digite o ID do livro que deseja deletar: "))
        cursor.execute(f"DELETE FROM livros WHERE livro_id={self.id}")
        print("Livro deletado com sucesso")