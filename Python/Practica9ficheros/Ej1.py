nombre=""
telefono=""

opcion=int(input("1.Añadir\n2.Consulta\n3.Eliminar\n"))
while opcion<4 | opcion>0:
    if opcion==1:
        nombre=input("mete un nombre:  ")
        telefono=input("mete un telefono:  ")
    with open ("Practica9ficheros/Ficheros/listin.txt", "a") as fichero:
        fichero.write("\n"+nombre + "," + telefono +"\n")
        print("añadido correctamente") 
        fichero.close()
        
    if opcion==2:
        nombre=input("Anota un nombre:  ")
        fichero=open("Practica9ficheros/Ficheros/listin.txt", "r")
        for lineas in fichero:
            if nombre in lineas:
                telefono=lineas.strip().split(":")
                print(telefono[1])
                break