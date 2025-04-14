class Conta:

    logado = True
    tarifa = 1.99

    def __init__ (self):
        self.saldo = 0.0

    def getSaldo(self):
        if self.logado:
            return self.__saldo
        else:
            return None

    def setSaldo(self, valor):
        if valor > self.__saldo:
            self.__saldo = valor

    def __descontartarifa(self):
        self.__saldo -= self.tarifa

    def sacar(self, valor):
        if self.__saldo >= valor + self.tarifa:
            self.__saldo -= valor
            self.__descontartarifa()
            print("Saque realizado")
        else: 
            print("Valor para saque insuficiente")
