import math

minutos=int(input("Dime cuantos minutos: "))
horas=math.trunc(int(minutos/60))
resto= minutos%60
print ((str(horas))+ " horas " + str(resto)+"minutos")

