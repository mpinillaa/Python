from Validar.Ej1.Usuarios import validarUsu
from Validar.Ej1.Contraseña import validarContra

from Validar.Ej2.Dni import validarDni
from Validar.Ej2.Edad import validarEdad

dicUsuarios={}
usuario=input("introduce un usuario:  ")
while usuario != "*":
    while (validar := validarUsu(usuario))!=True :
        print(validar)
        usuario = input("introduce usuario:  ")
        
    contraseña=input("Introduce contraseña:  ")
 
    while (validar := validarContra(contraseña))!=True :
        print(validar)
        contraseña=input("introduce contraseña:  ")
    print("Datos introducidos correctamente" + str("usuario:  "+usuario)+ str("contraseña:  "+contraseña))
    
    if usuario in dicUsuarios:
        print("el usurio ya existe")
    else:
        dicUsuarios[usuario] = contraseña
        print("usuario añadido correctamente")
    usuario = input("introduce usuario:  ")
    
    dni = input("introduce dni:  ")
    
    while (validar := validarDni(dni))!=True:
        print(validar)
        dni = input("introduce dni:  ")
   