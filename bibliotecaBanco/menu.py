from Controle.classConexao import Conexao
from Modelo.classBiblioteca import Biblioteca



def menu():
    opcao = ''
    while opcao != 5:
        print("1 - Listar livros")
        print("2 - Cadastrar livro")
        print("3 - Atualizar livro")
        print("4 - Deletar livro")
        print("5 - Sair")

        opcao = int(input("\nDigite a opção desejada: "))
        
        
        match opcao:
            case 1:
                con = Conexao()
                cursor = con.db.cursor()
                biblioteca = Biblioteca(0, "", 0, 0, "")
                biblioteca.listarLivro(cursor)
                cursor.close()
                con.db.close()
                            
            case 2:
                con = Conexao()
                cursor = con.db.cursor()
                biblioteca = Biblioteca(0, "", 0, 0, "")
                biblioteca.cadastrarLivro(cursor)
                con.db.commit()
                cursor.close()
                con.db.close()
                            
            case 3:
                con = Conexao()
                cursor = con.db.cursor()
                biblioteca = Biblioteca(0, "", 0, 0, "")
                biblioteca.atualizarLivro(cursor)
                con.db.commit()
                cursor.close()
                con.db.close()
                            
            case 4:
                con = Conexao()
                cursor = con.db.cursor()
                biblioteca = Biblioteca(0, "", 0, 0, "")
                biblioteca.deletarLivro(cursor)
                con.db.commit()
                cursor.close()
                con.db.close()
                            
            case 5:
                print("Saindo...")                        
            case _:
                print("Opção inválida")