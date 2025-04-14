

#Property - deixa o código mais limpo, declarado dentro da classe, é uma notação do Pyhton que nos permite "apelidar" nossos métodos; não se deve construir arquivos Python com o método get e set + propertys; ou faz um ou faz o outro.@property # Ficou convencionado que o @property é um sinalizador getter
class Conta:

    logado = True
    tarifa = 1.99

    def __init__ (self):
        self.saldo = 0.0
        
    def saldo(self):
        if self.logado:
            return self.__saldo
        else:
            return None

    @saldo.setter # Diferentemente do getter, o setter tem de ser @nomeDaNotação.setter
    def saldo(self, valor):
        if valor > self.__saldo:
            self.__saldo = valor


# sem a Property
x = Conta()
x.setSaldo( 100 )
print(x.getSaldo())


# Com a Property
y = Conta()
y.saldo = 100
print(y.saldo)

