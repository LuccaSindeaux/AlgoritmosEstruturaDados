from Apartamento import Apartamento

class FilaApartamento:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def imprimir(self):
        print("-" * 20)
        if self.inicio == None:
            print("Fila de espera para vagas está vazia")
        else:
            aux = self.inicio
            txt = ""
            while aux != None: 
                txt += str(f"Apartamento: {aux.numero}, {aux.torre}, {aux.vaga}") + "\n"
                aux = aux.prox 
            print(txt)
    
    def AddAptoFila(self, numero, torre, vaga):
        apartamento= Apartamento(numero, torre, vaga)
        if self.inicio == None:
            self.inicio = apartamento
        elif self.inicio.prox == None:
            self.inicio.prox = apartamento
        else:
            aux = self.inicio
            while aux.prox:
                aux = aux.prox
            aux.prox = apartamento
        self.fim = apartamento
        self.imprimir()

    def removerApto(self):
        if self.inicio is not None:
            self.inicio = self.inicio.prox
            if self.inicio == None:
                self.fim = None
            print(f"Apartamento removido, próximo da fila: AP {self.inicio.numero} esperando a vaga {self.inicio.vaga}.")