from funciones import esVocal,estaLista,transformar


lista = []
cadena = input("Ingresa una cadena: ").lower()

for letra in cadena:
    if esVocal(letra):  
        print("Es vocal " + letra)
        index = estaLista(letra, lista)  
        if index != -1:  
            lista[index][1] += 1
        else: 
            lista.append([letra, 1])
    else:
        print("No es vocal "+  letra )

print("Lista:", lista)

t = transformar(lista)
print("Tuplas:", t)

t.sort(key=lambda x: x[1], reverse=True)
print("Ordenado de mayor a menor:", t)