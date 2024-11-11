def filtrarPalabras(lista,n):
    for i in lista:
        if len(i) >= n:
            print(i)
            
original=["a","dffddffff","aaa"]


filtrarPalabras(original,5)
