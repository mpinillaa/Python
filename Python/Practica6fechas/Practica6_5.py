from Fechas import A1, B2, C3, D4, E5, F6


fecha=input("introduce una fecha en este formato 'yyyymmdd'     ")
año=A1.year(fecha[0:4])
mes=B2.month(fecha[4:6])
nombreMes=C3.monthName(fecha[4:6])
dia=D4.day(fecha[6:], mes)
date=E5.date2text(fecha)
dateName=F6.date2textName(dia, nombreMes, año)

print(año)
print(mes)
print(nombreMes)
print(dia)
print(date)
print(dateName)