from Produto import Produto
from Pessoa import Pessoa
from datetime import date


class Pedido:
    def __init__(self, data = date.today(), cli = Pessoa("Fulano de Souza")):
        self.id = None
        self.data = data
        self.cli = cli
        self.produtos = []


    
    def addProd(self, prod):
        if prod :
            self.produtos.append(prod)
            soma = 0.0
        for p in self.produtos: 
            soma += p.preco
        return soma

    def __str__(self):
        txt = "Data: " + str(self.data)
        txt += "Nome: " + str(self.cli)
        txt += "Produtos: "
        for p in self.produtos:
            txt += "\nNome do produto: " + p.nome
            txt += "\nPreço: " + str(p.preco)
            txt += "\n---------------------------------"
        return txt

