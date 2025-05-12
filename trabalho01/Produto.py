from abc import ABC, abstractmethod

class Produto(ABC):
    def __init__(self, modelo, cor, preco, categoria):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
        self.categoria = categoria
    

    def getInformacoes(self):
        infos = f'''
            Modelo: {self.modelo}.
            Cor: {self.cor}.
            Preço: {self.preco}.
            Categoria: {self.categoria.nome}.
        '''
        return infos

    @abstractmethod
    def cadastrar(self):
        pass

    

# Construa getters e setters para os atributos que não forem públicos. Todas as classes devem ter um método construtor.
# Construa uma interface gráfica que permita ao usuário cadastrar Desktops e Notebooks.