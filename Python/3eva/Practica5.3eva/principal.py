
from funciones import esVocal
from funciones import estaLista
from funciones import transformar
from funciones import ordenar 

lista = []
cadena = input("Ingresa una cadena: ").lower()

for letra in cadena:
    if esVocal(letra):  
        print("Es vocal " + letra)
        lista.append(estaLista(letra, cadena) )
        
    else:
        print(f"No es vocal {letra}")

print("Lista:", lista)

t = transformar(lista)
print("Tuplas:", t)

o=ordenar(t)
print(o)
