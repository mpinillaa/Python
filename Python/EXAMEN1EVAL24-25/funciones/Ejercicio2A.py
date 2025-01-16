def mostrarSitios(ruta):
    with open(ruta, "r") as f:
        contenido=f.read().split("\n")
        
    return contenido
        

