from No import No

class ListaEncadeada:
    def __init__ (self):
        self.inicio = None

    def addNoInicio(self, valor):
        nodo = No(valor)
        if self.inicio is not None: # Se o inicio não é nulo... 
            nodo.prox = self.inicio # ...O próximo elemento do nó é  o novo início
        self.inicio = nodo  # Independentemente de ser nulo ou não, o inicio será o nó/dado adicionado
        self.imprimir()

    def addNoFim(self, valor):
        nodo = No(valor)
        if self.inicio is None: # Se minha lista estiver vazia
            self.inicio = nodo # O inicio será o nó
        elif self.inicio.prox is None: # se existir o próximo elemento depois do inicio for nulo (lista só tem um elemento)
            self.inicio.prox = nodo # o próximo elemento do início receberá o nó
        else:
            aux = self.inicio # criei uma variável auziliar
            while aux.prox: # enquanto o próximo valor da auxiliar NÃO for nulo faz o laço abaixo
                aux = aux.prox # navegará toda a lista
            aux.prox = nodo # quando chegar no último elemento, o próximo elemento depois do último será o nó declarado
        self.imprimir()

    def removerDoInicio(self):
        if self.inicio is not None:
            self.inicio = self.inicio.prox
            print("Elemento removido")
        self.imprimir()

    def removerDoFim(self):
        if self.inicio != None:
            if self.inicio.proximo == None:
                self.inicio = None
            else:
                ant = self.inicio
                aux = self.inicio.prox
                while aux.prox: # enquanto o próximo elemento não for nulo
                    ant = aux
                    aux = aux.prox # auxiliar recebe o próximo elemento de auxiliar
                ant.prox - None
            print("Elemento removido")
        self.imprimir()


    def imprimir(self):
        print("-" * 20)
        if self.inicio == None:
            print("Lista encadeada vazia")
        else:
            aux = self.inicio
            while aux != None: 
                print(aux.dado) # printa o dado auxiliar
                aux = aux.prox # Vai pro próximo, repete o laço
            





    