from Cidade import Cidade
from Pessoa import Pessoa
from Produto import Produto
from Pedido import Pedido

c1 = Cidade()
c2 = Cidade("Porto Alegre")

p1 = Pessoa()
p2 = Pessoa("Lisiane", cidade = c1)

# print(p2.cidade.nome)
print(p2)


prod01 = Produto()
prod02 = Produto("Elden Ring", qtd = 100)
prod03 = Produto("Metaphor",250.00, 200)

ped01 = Pedido()
ped02 = Pedido(cli = p2)

ped02.addProd(prod02)
ped02.addProd(prod03)

print(ped02)