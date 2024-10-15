
caracter = input("Anota un caracter  ")
    
if len(caracter) ==1:
    if caracter >="a" and caracter <="z":   #isnumeric()
        print("es minusula")
    elif caracter >="A" and caracter <="Z": #upper()
        print("es mayuscula")
    elif caracter >="0" and caracter <="9": #
        print("es un numero")
        
else:
    print("escribe solo un caracter")