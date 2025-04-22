dicFacturas={
    '1234':100,
    '1432':200,
    '1928':300
}
opc=int(input("1.Añadir\n2.Pagar\n3.Salir\n"))

while(opc<3):
    if(opc==1):
        nfac = input("Introduce el nuevo número de factura: ")
        if nfac in dicFacturas:
            print("esta factura existe")
        else:
            coste = int(input("Introduce el coste: "))
            dicFacturas[nfac] = coste
            print("Factura añadida:", dicFacturas)
    elif(opc==2):
        nfac=input("introduce el número de factura   ")
        del(dicFacturas[nfac])
        print(dicFacturas)
        
    opc=int(input("1.Añadir\n2.Pagar\n3.Salir\n"))