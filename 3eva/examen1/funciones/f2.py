def estaLista(letra, lista):
    letra=letra.upper()
    if letra in lista:
        posicion=lista.index(letra)
        return [letra, posicion]
    else:
        return [letra, -1]

lista=['E', 'J', 'P', 'A']
listas=[]
cadena=input("introduce cadena      ")

for i in cadena:
    listas.append(estaLista(i, lista))

print(listas)