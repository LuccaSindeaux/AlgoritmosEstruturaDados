'''
Implemente uma pilha de livros e uma Lista Encadeada de autores, ordenada pelo nome do autor.
A classe Livro deve conter os atributos:
    titulo: String
    autor: Autor
    paginas: Int

A classe Autor deve conter os atributos:
    nome: String
    nacionalidade: String

Monte um menu que permita adicionar e remover livros, adicionar autores e imprimir tanto a lista de autores quanto a pilha de livros. 
'''
from ListaEncAutor import ListaAutores
from LifoLivro import PilhaLivros
from Livro import Livro
from Autor import Autor

def main():
    lista_autores = ListaAutores()
    pilha_livros = PilhaLivros()

    while True:
        print("\n=============== MENU ===============")
        print("1. Adicionar autor")
        print("2. Listar autores (em ordem alfabética)")
        print("------------------------------------")
        print("3. Adicionar livro (empilhar)")
        print("4. Remover livro (desempilhar)")
        print("5. Listar pilha de livros")
        print("------------------------------------")
        print("0. Sair")
        print("====================================")
        
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do autor: ")
            nacionalidade = input("Nacionalidade: ")
            lista_autores.adicionar_autor_ordenado(nome, nacionalidade)

        elif opcao == "2":
            lista_autores.imprimir()

        elif opcao == "3":
            if lista_autores.inicio is None:
                print("\nERRO: Cadastre um autor antes de adicionar um livro.")
                continue

            nome_autor = input("Digite o nome do autor do livro: ")
            autor_obj = lista_autores.buscar_autor(nome_autor)
            
            if autor_obj:
                titulo = input("Título do livro: ")
                paginas = int(input("Número de páginas: "))
                livro = Livro(titulo, autor_obj, paginas)
                pilha_livros.add(livro)
            else:
                print("\nAutor não encontrado! Cadastre o autor antes ou verifique o nome.")

        elif opcao == "4":
            pilha_livros.remover()

        elif opcao == "5":
            pilha_livros.imprimir()

        elif opcao == "0":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()