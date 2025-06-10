from Carros import Carro

class carrosFIFO:
    def __init__(self):
        self.inicio = None
        self.fim =  None
    
    def imprimir(self):
        print("-" * 20)
        if self.inicio == None:
            print("Fila para o lava-jato vazia.")
        else:
            aux = self.inicio
            txt = ""
            while aux != None: 
                txt += str(f"Carro: {aux.modelo}, {aux.ano}, {aux.placa}") + " - "
                aux = aux.prox 
            print(txt)
    
    def addCarro(self, modelo, ano, placa):
        carro = Carro(modelo, ano, placa)
        if self.inicio == None:
            self.inicio = carro
        elif self.inicio.prox == None:
            self.inicio.prox = carro
        else:
            aux = self.inicio
            while aux.prox:
                aux = aux.prox
            aux.prox = carro 
        self.fim = carro
        self.imprimir()
    
    def removerCarro(self):
        if self.inicio is not None:
            self.inicio = self.inicio.prox
            if self.inicio == None:
                self.fim = None
            print(f"Carro lavado, próximo {self.inicio.modelo}")
        self.imprimir()