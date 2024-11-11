def comprobarOrdenado(x):
    y=list(x)
    y.sort()
    if x==y:
        print("esta ordenado")
    else:
        print("no esta ordenado")
        
listaBien=[1,2,3,4,5,6,7,8,9]
listaMal=[1,4,2,6,3,5,7,8,9]

comprobarOrdenado(listaBien)
comprobarOrdenado(listaMal)