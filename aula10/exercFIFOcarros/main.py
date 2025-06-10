'''Implemente uma fila de carros num lava-jato, contendo métodos para:
1 - registrar a entrada dos carros;
2 - para lavar os carros.
O carro deve conter os atributos modeos ano e placa; desenvolva também um método para imprimir a fila de carros'''

'''
Implemente a fila de um banco onde há duas fiças: uma normal e a preferencial.
'''

from CarrosFIFO import carrosFIFO

fila = carrosFIFO()
fila.addCarro("Ram", "2008", "IKT3095")
fila.addCarro("Defender", "2018", "IOP04178")
fila.addCarro("Urus", "2014", "IMH4521")
fila.addCarro("Seal", "2022", "KBT4978")
fila.addCarro("HRV", "2017", "SML1954")
fila.removerCarro()