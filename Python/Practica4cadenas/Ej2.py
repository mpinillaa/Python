def primeraLetra(cadena):
    salida= ""
    
    palabras=cadena.split()
    for i in range(len(palabras)):
        salida+=(palabras[i])[0]
    print(salida)    
    
primeraLetra("Universal Series Bus")

def mayuscula(cadena):
    
    salida=""
    palabras=cadena.split()
    
    for i in range(len(palabras)):
        salida+=(palabras[i][0].upper() + (palabras[i])[1:]+ " ")
    print(salida)    
    
mayuscula("republica  argentina")


def a(cadena):
    salida=""
    palabras=cadena.split()
    for i in range(len(palabras)):
        if(palabras[i][0]=="A")|(palabras[i][0]=="a"):
            salida+=palabras[i]+" "
    print(salida)    
    
a("Antes de Ayer")