def buscarEmpleado(dic, lista):
    print("APARTADO 2:")
    no_duplicados=[]
    [no_duplicados.append(x) for x, y in dic.items() for v in y if v not in lista and x not in no_duplicados]
    print(no_duplicados)
    print('--------------------')