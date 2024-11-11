def encontrarNombre(nombres,nom):
    for i in nombres:
        if(i==nom):
            return True
        else:
            return False



nombres=list()
nombresEncontrados=list()

while True:
    nombre=input("Anota un nombre:   ")
    if nombre =="-1":
        break
    nombres.append(nombre)
    
for i in nombres:    
    if encontrarNombre(i, nombresEncontrados):
        continue
    
    x=nombres.count(i)  
    
    nombresEncontrados.append((i,x))
    
    

print(nombresEncontrados)
    
'''te cuenta los nombres(i) de la lista nombres'''
'''No poner While True: porque te pone un 0 en el examen'''