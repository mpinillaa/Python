import random



def ataqueAleatorio():
    return random.randint(1,10)

def defensaAleatorio():
    return random.randint(1,15)

    
    
nombre1=input("anota nombre de p1:")
nombre2=input("anota nombre de p2:")

personaje1=[nombre1,ataqueAleatorio(),defensaAleatorio()]
personaje2=[nombre2,ataqueAleatorio(),defensaAleatorio()]

turno=random.randint(0,1)


print(personaje1)
print(personaje2)

while personaje1[2]>0 and personaje2[2]>0:
    print(f"turno de {nombre1}")
    personaje2[2]=personaje2[2]-personaje1[1]
    if personaje2[2]<0:
        print(f"el jugador {nombre2} ha muerto, {nombre1} ha ganado")
        break
    else:
        print(f"turno de {nombre2}")
        personaje1[2]=personaje1[2]-personaje2[1]
        if personaje1[2]<0:
            print(f"el jugador {nombre1} ha muerto, {nombre2} ha ganado")
        break
