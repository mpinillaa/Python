def esVocal(e):
    vocal=['a', 'e', 'i', 'o', 'u']
    if e.lower() in vocal:
        return True
    return False

def estaLista(letra, lista):
    letra=letra.upper()
    if letra in lista:
        posicion=lista.index(letra)
        return posicion
    else:
        return  -1

def transformar(lista):
   
    li = []
    for i in lista:
        li.append((i[0], i[1]))
    return li

def ordenar(e):
    e.sort(key=lambda x: x[1], reverse=True) 
    return e 