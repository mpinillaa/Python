from functools import reduce

def crearDiccionario(nombres):
    dic={}
    contenido=nombres.split(";")
    contenido=contenido[0:-1]
    
    for i in contenido:
        fila=i.split(",")
        clave=fila[0]
        total=int(fila[1])+int(fila[2])+int(fila[3])
        if clave in dic:
            dic[clave].append(total)
        else:
            dic[clave]=[total]
    
    return dic
        
def ordenar_diccionario(dic):
    dic=dict(sorted(dic.items()))
    """    lista=[]
    for clave, valores in dic.items():
    lista.append((clave, max(valores)))
    lista.sort(key=lambda x:x[1], reverse=True)
    return lista"""
    return dic


def menor_num_tiradas(dic):
    
    for i in dic:
        valor=dic[i]
      
        if len(valor)>1:
            if(valor[1]>valor[0]):
                dic[i]=[valor[1]]
            else:
                dic[i]=[valor[0]]
                
    return dic

def igualar_tiradas_diccionario(dic):
      for i in dic:
        valor=dic[i]
      
        if len(valor)>1:
            if(valor[1]>valor[0]):
                dic[i]=[valor[1]]
            else:
                dic[i]=[valor[0]]
        return dic

def generar_lista_tuplas(dic):
    lista=[]
    for clave, valor in dic.items():
        suma=reduce(lambda x,y: x+y, valor)
        lista.append((clave, suma))
    mayor=[("," ,0)]
    for i, k in lista:
        if mayor[0][1]<int(k):
            mayor=[(i, k)]
        
    return mayor