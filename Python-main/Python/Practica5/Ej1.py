cadena= input("introduce una cadena  ")
cadena = cadena.lower()
palabras=cadena.split() 
"""lo que hace es separar la cadena EJ:cadena: hola que tal     "hola",  "que" , "tal"  """

vecesRepetidas={}
"""Diccionarioooo"""
for i in palabras:
    if i in vecesRepetidas:
       vecesRepetidas[i]+=1
    else:
        vecesRepetidas[i]=1

print(vecesRepetidas)