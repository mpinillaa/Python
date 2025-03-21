cadena = "que lindo dia que hace hoy"
print(cadena)
cadena= cadena.lower()
print(cadena)
cadenaSeparada=cadena.split()
print(cadenaSeparada)
dicc={}

for i in cadenaSeparada:
    if i in dicc:
        dicc[i]+=1
    else:
        dicc[i]=1
        
print(dicc)