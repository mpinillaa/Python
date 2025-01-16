def transformar(lista):
   return (lista[0], lista[1])


res=[
        ["E", 1],
        ['A', 2],
        ['C', -1]
    ]
tupla= []
for i in res:
    tupla.append(transformar(i))

print(tupla)