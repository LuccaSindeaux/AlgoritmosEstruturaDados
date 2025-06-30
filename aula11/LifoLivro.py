from Livro import Livro

class PilhaLivros: 
    def __init__(self):
        self.topo = None

    def add(self, book):
        book.prox = self.topo
        self.topo = book
        print("\nLivro cadastrado com sucesso!")

    def imprimir(self):
        print("\n--- Pilha de Livros ---")
        if self.topo is None:
            print("Pilha está vazia!")
        else:
            aux = self.topo
            while aux:
                print("------------------------")
                print(f"Título: {aux.titulo}")
                print(f"Autor: {aux.autor.nome}") 
                print(f"Páginas: {aux.paginas}")
                aux = aux.prox
        print("*************************")

    def remover(self):
        if self.topo is None:
            print("\nPilha de Livros vazia!")
            return None
        else:
            livro_removido = self.topo
            self.topo = self.topo.prox
            print(f"\nLivro '{livro_removido.titulo}' foi removido!")
            return livro_removido