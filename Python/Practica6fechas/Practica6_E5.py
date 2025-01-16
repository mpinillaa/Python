from Fechas.A1 import year
from Fechas.B2 import month
from Fechas.C3 import monthName


fecha=input("introduce una fecha en este formato 'yyyymmdd'     ")
año=year(fecha[0:4])
mes=month(fecha[4:6])
dia=monthName(fecha[6:])

print(año)
print(mes)
print(dia)
