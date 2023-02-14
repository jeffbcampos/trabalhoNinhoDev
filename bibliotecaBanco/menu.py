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
        biblioteca = Biblioteca(0, "", 0, 0, "")
        
        match (opcao):
            case 1:               
                biblioteca.listarLivro()
            case 2:               
                biblioteca.cadastrarLivro()
            case 3:               
                biblioteca.atualizarLivro()
            case 4:               
                biblioteca.deletarLivro()
            case 5:
                print("Saindo...")
                biblioteca.closeConnection()
            case _:
                print("Opção inválida")
