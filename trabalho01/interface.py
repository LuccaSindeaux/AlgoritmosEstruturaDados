import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QComboBox, QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox

from Categoria import Categoria
from Desktop import Desktop
from Notebook import Notebook

class ProdutoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cadastro de Produtos")
        self.setGeometry(100, 100, 400, 300)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Campos básicos
        self.tipo_combo = QComboBox()
        self.tipo_combo.addItems(["Desktop", "Notebook"])
        self.tipo_combo.currentIndexChanged.connect(self.alternarCampoExtra)

        self.modelo_input = QLineEdit()
        self.cor_input = QLineEdit()
        self.preco_input = QLineEdit()
        self.categoria_input = QLineEdit()
        self.extra_label = QLabel("Potência da Fonte:")
        self.extra_input = QLineEdit()

        layout.addWidget(QLabel("Tipo de Produto:"))
        layout.addWidget(self.tipo_combo)

        layout.addWidget(QLabel("Modelo:"))
        layout.addWidget(self.modelo_input)

        layout.addWidget(QLabel("Cor:"))
        layout.addWidget(self.cor_input)

        layout.addWidget(QLabel("Preço:"))
        layout.addWidget(self.preco_input)

        layout.addWidget(QLabel("Categoria:"))
        layout.addWidget(self.categoria_input)

        layout.addWidget(self.extra_label)
        layout.addWidget(self.extra_input)

        # Botão de cadastrar
        self.botao = QPushButton("Cadastrar")
        self.botao.clicked.connect(self.cadastrarProduto)
        layout.addWidget(self.botao)

        self.setLayout(layout)

    def alternarCampoExtra(self):
        tipo = self.tipo_combo.currentText()
        if tipo == "Desktop":
            self.extra_label.setText("Potência da Fonte:")
        else:
            self.extra_label.setText("Tempo de Bateria:")

    def cadastrarProduto(self):
        tipo = self.tipo_combo.currentText()
        modelo = self.modelo_input.text()
        cor = self.cor_input.text()
        preco = self.preco_input.text()
        categoria_nome = self.categoria_input.text()
        extra = self.extra_input.text()

        if not all([modelo, cor, preco, categoria_nome, extra]):
            QMessageBox.warning(self, "Erro", "Todos os campos devem ser preenchidos.")
            return

        try:
            preco = float(preco)
        except ValueError:
            QMessageBox.warning(self, "Erro", "Preço deve ser um número.")
            return

        categoria = Categoria(1, categoria_nome)

        if tipo == "Desktop":
            produto = Desktop(modelo, cor, preco, categoria, extra)
        else:
            produto = Notebook(modelo, cor, preco, categoria, extra)

        QMessageBox.information(self, "Sucesso", produto.getInformacoes())
        produto.cadastrar()

def main():
    app = QApplication(sys.argv)
    janela = ProdutoApp()
    janela.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()