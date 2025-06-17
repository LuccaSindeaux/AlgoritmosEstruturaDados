from Autor import Autor 

class ListaEncAutor:
    def __init__ (self):
        self.inicio: None
    
    def addInicio(self, valor):
        autor = Autor(valor)
        if self.inicio != None:
            autor.prox = self.inicio
        self.inicio = autor
        self.imprimir()
    
    def addFim(self, valor):
        autor = Autor(valor)
        if self.inicio == None:
            self.inicio = autor
        elif self.inicio.prox == None:
            self.inicio.prox = autor
        else:
            aux = self.inicio
            while aux.prox:
                aux = aux.prox
            aux.prox = autor
        self.imprimir()
    
    def removeInicio(self):
        if self.inicio == None:
            self.inicio = self.inicio.prox
            print("Elemento removido.")
        self.imprimir()

    def removeFim(self):
        if self.inicio != None:
            if self.inicio.prox == None:
                self.inicio = None
            else:
                ant = self.inicio
                aux = self.inicio.prox
                while aux.prox:
                    ant = aux
                    aux = aux.prox
                ant.prox = None
            print("Elemento removido.")
        self.imprimir()
    
    def imprimir(self):
        print("-" * 40)
        if self.inicio == None:
            print("Lista encadeada de autores:")
        else:
            aux = self.inicio
            while aux != None:
                print(f'''Autor; ${aux.autor}\nNacionalidade: ${aux.nacionalidade}''') #mudar
                aux = aux.prox

