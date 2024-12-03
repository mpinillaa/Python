import csv

with open("Practica9ficheros/csv/AlumnosFP.csv", "r", encoding="latin-1") as fichero:
    nombres=list(csv.reader(fichero, delimiter=";"))
    nombres=nombres[1:]
    
    
    
correos=[]

for i in nombres:
    correos.append(i[1])

print(correos)
    
with open("Practica9ficheros/csv/ListadoAlumnosFP.csv", "r", encoding="latin-1") as fichero:
    nombre=list(csv.reader(fichero, delimiter=";"))
    nombre=nombre[1:]
    
    print(nombre)
    
    
correoAlumno=[]

for i in nombre:
    correo=i[0].lower()+"."+i[1].lower()+"@plazacastilla.salesianas.org"
    if correo in correos:
        correo=i[0].lower()+"."+i[1].lower()+"."+i[2].lower()+"@plazacastilla.salesianas.org"
        correoAlumno.append(correo)
    else:
        correoAlumno.append(correo)
        
print(correoAlumno)

"""con el writer y con append no se puede poner un with open, tienes que poner fichero=open"""

fichero=open("Practica9ficheros/csv/AlumnosFP.csv", "a")
contenido=csv.writer(fichero, delimiter=";")

nombreUnido=[]

for i in nombre:
    nombreUnido.append(" ".join(i))
    
for i in range(0, len(nombre)):
    contenido.writerow([nombreUnido[i], correoAlumno[i], 'Ventajas de uso de Microsoft 365 A3 para estudiantes'])

    
print(nombreUnido)

"""te pilla las 6 filas de nombre(es del fichero listadoAlumnos) va recorriendo cada linea"""