horas = int(input("introduce las horas"))
min = int(input("introduce los minutos"))
seg = int(input("introduce los segundos"))

def calcularsegundos(horas,min,seg):

    
    min = horas*60    
    seg = min*60
    
    print("esta es la cantidad en segundos" + int(seg))