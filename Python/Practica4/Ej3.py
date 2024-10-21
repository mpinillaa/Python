palabra = input("escribe una palabra, si pones FIN, el programa termina  ")
lista=[]
cont=0

while palabra!=("FIN"):
    lista.append(palabra)
    palabra = input("escribe una palabra , si pones FIN, el programa termina ")


palabra = input("que palabra quieres buscar  ")
if palabra in lista:
    print("encontrada  " + (palabra))
else:
    print("no encontrada  " + (palabra))
    
    
print(" La palabra " + str(palabra) + "  aparece " + str(lista.count(palabra)) + " veces ")

print(lista)


palabra2 = input("que palabra quieres reemplazar: " + str(palabra) )

