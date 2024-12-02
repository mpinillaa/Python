dicPesronas={}
with open("Practica9ficheros/Ficheros/Personas.txt", "r") as fichero:
    for linea in fichero:
        datos=linea.split(";")
        dicPesronas[datos[0]]={
            "nombre" :datos[1],
            "apellido" : datos[2],
            "fecha" : datos[3]
        }
        
print(dicPesronas)