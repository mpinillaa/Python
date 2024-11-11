ct=str(input("Cadena texto "))

def EscribirCentrado(caracter):
    cad=""
    espacios=80-round(len(caracter)/2)
    print(espacios)
    for i in range(0,espacios):
        cad=cad+" "
    print(cad+caracter)
    print(len(caracter))
    """ añadir un for que ponga una linea abajo de un caracter de  """

EscribirCentrado(ct)

def ConvertirEspaciado(ct):
    cad=""
    ct=ct.replace(" ","")
    for i in range(0,len(ct)):
        cad=cad+ct[i]+" "
    print(cad)

ConvertirEspaciado(ct)