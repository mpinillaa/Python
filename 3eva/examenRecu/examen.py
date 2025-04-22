
from utilidades import get_datos, get_charlasaforo, venta_entradas

datos = get_datos()


filtradas = get_charlasaforo(datos, 20) 
print("estas son las charlas con aforo inferior al 20%:")
print(filtradas)


venta = venta_entradas(datos, "Ciberseguridad en la Era Digital", 10)
print("Venta realizada:", venta)


