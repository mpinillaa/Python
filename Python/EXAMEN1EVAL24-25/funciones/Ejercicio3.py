import csv

def crearDicTrabajo(ruta):
    dic = {}
    contenido = csv.reader(ruta, delimiter="|")
    with open("EXAMEN1EVAL24-25/assets/sitios_trabajo.txt", "r", encoding='latin-1') as f:
        lista=f.read()
        for fila in contenido:
            clave = fila[0]
            valor = fila[1:]
            if clave in dic:
                if valor not in dic[clave]:
                    dic[clave].append(valor)
                else:
                    min=int(valor[1])
                    for i in dic[clave]:
                        min+=int(i[1])
                        print(min)
                        total=i[0]+", "+str(min)
                        dic[clave]=[total]
            else:
                dic[clave] = [valor]
                
    print("APARTADO 3")
    for i in dic:
        print(i+": "+str(dic[i]))
    print("--------------------")  
    
    return dic