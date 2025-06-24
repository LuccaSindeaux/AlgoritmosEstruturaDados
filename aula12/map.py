#Map chama uma função dentro de si e declara também os argumentos

#EXEMPLO 1
def getSize(a):
    return len(a)

x = map( getSize, ("maçã", "banana", "laranja")) # executa a função 3 vezes, uma para cada argumento(fruta)
print('Exemplo1:')
print(list(x)) # tem de ser convertido para lista, pois se colocar só 'print(x)' ele vai devolver a instância, e não o resultado


#EXEMPLO 2
def aumentarPreco(preco):
    return preco * 1.1 #aumento de 10%

precos = [5, 8.5, 10, 21]
novosPrecos = map(aumentarPreco, precos) #diferente do outro exemplo, eu quero que ele percorra todo o array precos
print('-'*40)
print('Exemplo2:')
print(list(novosPrecos))

#exemplo 3
def somar(valores):
    soma = 0
    for x in valores:
        soma += x
    return soma

somas = map( somar, ((10, 5, 3), [8, 2, 1,5]))
            #tupla com (tupla, array) ---> Obs.: Dicionários não podem ser passados como argumentos neste caso
            #result: [18, 16]
print('-'*40)
print('Exemplo3:')
print(list(somas))