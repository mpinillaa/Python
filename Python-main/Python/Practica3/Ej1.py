
altura=int(input("Altura: "))
anchura=int(input("Anchura: "))


def dibujarRectan (altura,anchura):
    resultado=""
    for i in range(altura):
        resultado+= "\n  #  "
        for j in range(anchura-1):
            resultado+= "  #  "
    return resultado

resultado= dibujarRectan(altura,anchura)

print(resultado)