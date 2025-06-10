from No import No

class ListaDuplamenteEncadeada():
    def __init__ (self):
        self.inicio = None
        self.fim = None

    def add(self, valor):
        nodo = No(valor)
        if self.inicio == None and self.fim == None:
            self.inicio = nodo
        elif valor < self.inicio.dado:
            nodo.prox = self.inicio
            self.inicio = nodo
        else:
            return valor # terminar
            
