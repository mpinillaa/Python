horas = int(input("introduce las horas"))
min = int(input("introduce los minutos"))
seg = int(input("introduce los segundos"))

def calcularsegundos(horas,min,seg):

    resultado=(horas*3600) + (min*60) + (seg)
    return resultado
    
print(calcularsegundos(horas,min,seg))


def calcularHoras(seg):

    horas= seg//3600
    min= (seg%3600)//60
    seg= (seg%3600)%60
    
    return " horas: " + str(horas) +" minutos: " + str(min) +" segundos:   "+ str(seg)

print(calcularHoras(seg))