from No import No

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
    
    def add(self, valor):
        nodo = No(valor)
        if self.inicio == None: 
            self.inicio = nodo
        elif self.inicio.prox == None:
            self.inicio.prox = nodo 
        else:
            aux = self.inicio
            while aux.prox:
                aux = aux.prox
            aux.prox = nodo 
        self.fim = nodo
        self.imprimir()

    def remover(self):
        if self.inicio is not None:
            self.inicio = self.inicio.prox
            if self.inicio == None:
                self.fim = None
            print("Elemento removido")
        self.imprimir()

    def imprimir(self):
        print("-" * 20)
        if self.inicio == None:
            print("fila vazia")
        else:
            aux = self.inicio
            txt = ""
            while aux != None: 
                txt += str(aux.dado) + " - "
                aux = aux.prox 
            print(txt)