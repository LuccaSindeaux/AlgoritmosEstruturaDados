'''Implemente uma fila de carros num lava-jato, contendo métodos para:
1 - registrar a entrada dos carros;
2 - para lavar os carros.
O carro deve conter os atributos modeos ano e placa; desenvolva também um método para imprimir a fila de carros'''

class Carro:
    def __init__(self, modelo, ano, placa):
        self.modelo = modelo
        self.ano = ano
        self.placa  = placa
        self.inicio = None
        self.fim = None
        self.prox = None