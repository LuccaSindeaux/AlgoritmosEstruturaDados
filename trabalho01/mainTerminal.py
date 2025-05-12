#Testando getters em terminal

from Categoria import Categoria
from Desktop import Desktop
from Notebook import Notebook

# Criar categoria
categoria1 = Categoria(1, "Gamer")

# Criar e testar Desktop
desktop = Desktop("Dell XPS", "Preto", 4500.0, categoria1, "500W")
print("Desktop - Potência da Fonte:", desktop.getPotenciaDaFonte())
desktop.setPotenciaDaFonte("600W")
print("Potência Atualizada:", desktop.getPotenciaDaFonte())
desktop.cadastrar()

# Criar e testar Notebook
notebook = Notebook("Acer Aspire", "Prata", 3200.0, categoria1, "8h")
print("Notebook - Tempo de Bateria:", notebook.getTempoDeBateria())
notebook.setTempoDeBateria("10h")
print("Tempo Atualizado:", notebook.getTempoDeBateria())
notebook.cadastrar()

