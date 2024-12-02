with open("Practica9ficheros/Ficheros/Texto4.txt", "r") as fichero:
   palabras=fichero.read().split(" ") 
   
   for i in palabras:
       print(i)