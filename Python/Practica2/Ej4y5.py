import random

numero = int(random.randint(0,10))
i=int(input("Escribe un numero  "))
intentos=0

while i!=numero:            
    if i < numero:
        print("el numero tiene que ser mayor")       
    else:
        print("el numero tiene que ser menor")       
    intentos+=1    
    if intentos>4:
        break
    i=int(input("Escribe un numero  "))    
        
if intentos<4:  
    print("ese es el numero")      
        
else:
    print("has superado el numero de intentos este era el numero: " + str(numero))
