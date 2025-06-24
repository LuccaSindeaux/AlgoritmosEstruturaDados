def calcular(x,y):
    return (x+y, x-y, x*y, x/y)

result = calcular(10, 5)

print(result)
for x in result:
    print(x)
a, b, c ,d = result
print(f'''
Soma: {a}
Subtração: {b}
Multiplicação: {c}
Divisão: {d}
''')