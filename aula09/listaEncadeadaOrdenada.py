from No import No

class ListaEncadeadaOrdenada():
    def __init__ (self):
        self.inicio = None
    
    def add(self, valor):
        nodo =  No(valor)
        if self.inicio == None:
            self.inicio = nodo
        elif valor < self.inicio.dado:
            nodo.prox = self.inicio
            self.inicio = nodo
        else:
            ant = self.inicio # anterior recebe o primeiro valor
            aux = self.inicio.prox #variável auxiliar, recebe inicialmente o segundo elemento -> próximo do início
            while aux:
                if valor < aux.dado: # aux é um nó, para a comparação ser possível ele deve ser comparado com o dado presente no nó
                    ant.prox = nodo
                    nodo.prox = aux
                    break
                else:
                    ant = aux
                    aux = aux.prox
            if aux == None:
                ant.prox = nodo 
        self.imprimir()

    def imprimir(self):
        print("-" * 20)
        if self.inicio == None:
            print("Lista encadeada vazia")
        else:
            aux = self.inicio
            while aux != None: 
                print(aux.dado) 
                aux = aux.prox 

    def remover(self, valor):
        removeu = False
        if self.inicio != None:
            if valor == self.inicio.dado:
                self.inicio = self.inicio.prox
                removeu = True
            else:
                ant = self.inicio
                aux = self.inicio.prox
                while aux:
                    if valor == aux.dado:
                        ant.prox = aux.prox
                        removeu = True
                        break
                    else:
                        ant = aux
                        aux = aux.prox
            if removeu:
                print(f"Elemento {valor} removido da lista")
            else:
                print(f"Elemento {valor} não foi encontrado")
        self.imprimir()

