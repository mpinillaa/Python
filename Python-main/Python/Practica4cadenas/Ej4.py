cadena= input("anota una cadena  ")

vuelta = cadena[::-1] 
"""lo que hace es qwue te coge desde el principio de la cadena y el final y le da la vuelta """
if cadena==vuelta:
    print("palindormo")
else:
    print("No palindormo")