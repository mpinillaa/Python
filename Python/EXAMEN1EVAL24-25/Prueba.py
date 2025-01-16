from funciones.Ejercicio1A import crearDiccionario
from funciones.Ejercicio1B import mostrarInfo
from funciones.Ejercicio2A import mostrarSitios
from funciones.Ejercicio2B import buscarEmpleado
from funciones.Ejercicio3 import crearDicTrabajo

ruta=open("EXAMEN1EVAL24-25/assets/sitios_empleados.csv", "r", encoding='latin-1')
p=crearDiccionario(ruta)

i=mostrarInfo(p)


ruta2="EXAMEN1EVAL24-25/assets/sitios_trabajo.txt"
print(ruta2[0])
s=mostrarSitios(ruta2)

print("Lista: ")
print(s)

print("---------------")

b=buscarEmpleado(p, s)

ruta3=open("EXAMEN1EVAL24-25/assets/sitios_empleados.csv", "r", encoding='latin-1')

c=crearDicTrabajo(ruta3)