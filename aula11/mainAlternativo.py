from ListaEncAutor import ListaAutores
from LifoLivro import PilhaLivros
from Livro import Livro
from Autor import Autor

def main_teste():
    """
    Função de teste não interativa que demonstra as funcionalidades
    com valores pré-definidos ("chumbados").
    """
    print("--- INICIANDO TESTE AUTOMATIZADO ---")

    # Instanciando as classes
    lista_autores = ListaAutores()
    pilha_livros = PilhaLivros()

    # Adicionando autores (propositalmente fora de ordem alfabética)
    print("\nAdicionando autores...")
    lista_autores.adicionar_autor_ordenado("Machado de Assis", "Brasileiro")
    lista_autores.adicionar_autor_ordenado("Clarice Lispector", "Ucraniana/Brasileira")
    lista_autores.adicionar_autor_ordenado("Jorge Amado", "Brasileiro")
    lista_autores.adicionar_autor_ordenado("José Saramago", "Português")
    
    lista_autores.imprimir()

    # Adicionando livros na pilha
    print("\nAdicionando livros na pilha...")
    
    # Busca o objeto de cada autor para associar ao livro
    autor_machado = lista_autores.buscar_autor("Machado de Assis")
    autor_clarice = lista_autores.buscar_autor("Clarice Lispector")
    autor_saramago = lista_autores.buscar_autor("José Saramago")

    if autor_machado and autor_clarice and autor_saramago:
        livro1 = Livro("Dom Casmurro", autor_machado, 256)
        pilha_livros.add(livro1)
        
        livro2 = Livro("A Hora da Estrela", autor_clarice, 88)
        pilha_livros.add(livro2)
        
        livro3 = Livro("Ensaio sobre a Cegueira", autor_saramago, 310)
        pilha_livros.add(livro3)

    pilha_livros.imprimir()

    # Removendo o livro do topo da pilha
    print("\nRemovendo o livro do topo...")
    pilha_livros.remover()

    pilha_livros.imprimir()

    autor_inexistente = lista_autores.buscar_autor("George Orwell")
    if autor_inexistente is None:
        print("Teste de autor inexistente bem-sucedido: 'George Orwell' não foi encontrado.")

if __name__ == "__main__":
    main_teste()