from Cidade import Cidade

class Pessoa:
    def __init__(self, nome = None, cpf = None, cidade = Cidade("PossoMudarNomeDefaultAtravesInstancia") ):
        self.id = None                           #criação de instância da classe Cidade, que possui id e nome
        self.nome = nome
        self.cpf = cpf
        self.cidade = cidade
        self.salario = 1518.00

    def setSalario(self, valor):
        if valor > self.salario:
            self.salario = valor

    def __str__(self):
        txt = "Nome: " + str(self.nome)
        txt += "\nCPF: " + str(self.cpf)
        txt += "\nSalário: " + str(self.salario)
        txt += "\nCidade: " + str(self.cidade)
        return txt

             
