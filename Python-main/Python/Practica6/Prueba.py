from Validar.Ej1.Usuarios import validarUsu
from Validar.Ej1.Contraseña import validarContra

usuarios=input("introduce el usuario, introduce '*' para salir:   ")
contraseña=input("introduce la contraseña del usuario:   ")
dicUsuarios={}

validar=True  
"""no es necesario creo"""
while usuarios != "*":
    validar= validarUsu(usuarios)
    print(validar)
    if validar==True:
        validar=validarContra(contraseña)
        if validar==True:
            dicUsuarios[usuarios]=contraseña
            print("la contraseña se ha creado correctamente")
            
    usuarios=input("introduce el usuario, introduce '*' para salir:   ")
    contraseña=input("introduce la contraseña del usuario:   ")     
    
print(dicUsuarios)

