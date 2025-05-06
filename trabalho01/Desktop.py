from Produto import Produto

class Desktop(Produto):
    def __init__(self, modelo, cor, preco, categoria ,potenciaDaFonte):
        super().__init__( modelo, cor, preco, categoria)
        self._potenciaDaFonte = potenciaDaFonte

    def cadastrar(self) -> str:
        self.modelo = input("Digite o modelo: ")
        self.cor = input("Digite a cor: ")
        self.preco = input("Digite o preco: ")
        self.categoria = input("Digite a categoria: ")
        self._potenciaDaFonte = input("Digite a potência da fonte: ")     
    
    @property
    def getInformacoes(self):
        return super().getInformacoes + f"\nPotência da fonte: {self._potenciaDaFonte} wats."