numeros=list()

while True:
    num = int(input("anota un numero, para salir negativo  "))
    numeros.append(num)    
    
    if (num < 0):
        break
    
print("NUmeros pares: ")
for i in range(len(numeros)):
    if numeros[i]%2  == 0:
        print(str(numeros[i]))
    
    
    
print("el numero maximo de la lista es:" + str(max(numeros)))

    
  
    
    
    





"""append te añade una variable a la lista"""