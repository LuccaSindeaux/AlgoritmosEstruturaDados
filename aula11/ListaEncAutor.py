from Autor import Autor

class ListaAutores:
    def __init__(self):
        self.inicio = None

    def adicionar_autor_ordenado(self, nome, nacionalidade):
        novo_autor = Autor(nome, nacionalidade)

        # Caso 1: A lista está vazia ou o novo autor vem antes do primeiro
        if self.inicio is None or novo_autor.nome < self.inicio.nome:
            novo_autor.prox = self.inicio
            self.inicio = novo_autor
        else:
            # Caso 2: Percorrer a lista para achar a posição correta
            aux = self.inicio
            while aux.prox is not None and novo_autor.nome > aux.prox.nome:
                aux = aux.prox
            
            novo_autor.prox = aux.prox
            aux.prox = novo_autor
        
        print(f"Autor '{nome}' adicionado com sucesso!")

    def buscar_autor(self, nome_autor):
        aux = self.inicio
        while aux is not None:
            if aux.nome.lower() == nome_autor.lower():
                return aux 
            aux = aux.prox
        return None

    def imprimir(self):
        print("\n--- Lista de Autores Cadastrados ---")
        if self.inicio is None:
            print("Nenhum autor cadastrado.")
            return
            
        aux = self.inicio
        while aux is not None:
            print(f"Nome: {aux.nome}, Nacionalidade: {aux.nacionalidade}")
            aux = aux.prox
        print("------------------------------------")