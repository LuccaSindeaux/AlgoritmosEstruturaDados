soldado1 = {
    'nome': 'Lucca',
    'idade': 27,
    'Sexo': 'Masculino',
    'Altura': 1.75,
    'Efetivado': True
}

soldado2 = {
    'nome': 'Butiá',
    'idade': 22,
    'Sexo': 'Masculino',
    'Altura': 1.74,
    'Efetivado': True
}

tropa = soldado1, soldado2 #isto aqui é uma tupla, não pode ser alterado

print("-"*180)
print(tropa)
print(tropa[1])
soldado2['altura'] = 1.73 # O dicionário dentro da tupla de dicionários pode ser alterado
print(tropa)
print("-"*180)



print(soldado1)
for chave, valor in soldado1.items():
    print(chave, ":", valor )