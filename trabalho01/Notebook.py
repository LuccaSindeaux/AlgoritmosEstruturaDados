from Produto import Produto


class Notebook(Produto):
    def __init__(self,  modelo, cor, preco, categoria, tempoDeBateria):
        super().__init__( modelo, cor, preco, categoria)
        self.__tempoDeBateria = tempoDeBateria

    def getTempoDeBateria(self):
        return self.__tempoDeBateria

    def setTempoDeBateria(self, tempo):
        self.__tempoDeBateria = tempo

    def getInformacoes(self):
        base_info = super().getInformacoes()
        return f"{base_info}, Tempo de Bateria: {self.__tempoDeBateria} horas"

    def cadastrar(self):
        print("Notebook cadastrado!")
        print(self.getInformacoes())

    # def cadastrar(self):
    #     self.modelo = input("Digite o modelo: ")
    #     self.cor = input("Digite o cor: ")
    #     self.preco = input("Digite o preco: ")
    #     self.categoria = input("Digite o categoria: ")
    #     self.__tempoDeBateria = input("Digite quantos minutos dura a bateria: ")

    
    # @__tempoDeBateria.setter
    # def __tempoDeBateria(self, valor):
    #     self.__tempoDeBateria = valor       

    # @property
    # def getInformacoes(self):
    #     return super().getInformacoes + f"\nTempo de bateria: {self.__tempoDeBateria} minutos."