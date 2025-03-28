def findName(names, n):
    for i in names:
        if(i==n):
            return True

    return False


dicc={
    'hola':'hello',
    'adios':'goodbye',
    'pene':'dick',
    'puño':'punch',
    'en':'in',
    'la':'the',
    'cara':'face'   
}
cadena=input('Escribe una frase     ')
exist=True
palabra=cadena.split(" ")
traduccion=""

for i in palabra:
    if i in dicc:
        print(dicc[i], end=' ')
    else:
        print(i, end=' ')