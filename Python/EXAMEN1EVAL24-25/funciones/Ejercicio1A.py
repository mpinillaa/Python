import csv

def crearDiccionario(ruta):
    dic = {}

   
    contenido = csv.reader(ruta, delimiter="|")

       
    for fila in contenido:
            clave = fila[0]
            valor = fila[1]
            
            if clave in dic:
                if valor not in dic[clave]:
                    dic[clave].append(valor)
            else:
                dic[clave] = [valor]

    return dic