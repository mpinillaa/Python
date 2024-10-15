anchura = int(input("Anchura: "))
caracter = (input("Carcater: "))

def dibujarTrian(anchura,caracter):
    resultado=""
    for i in range(anchura):
        resultado += str(caracter*i + "\n")
        
    return resultado

def dibujarTrian2(anchura,caracter):
    resultado=""
    
    while anchura > 0:
        for j in range(anchura):
            resultado += str(caracter*anchura+ "\n")
            anchura -= 1
    return resultado
    
resultado= dibujarTrian(anchura,caracter)
resultado+= dibujarTrian2(anchura,caracter)

print(resultado)