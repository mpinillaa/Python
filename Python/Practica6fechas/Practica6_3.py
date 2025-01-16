from Validaciones.E1.Usuario import validarUsuario
from Validaciones.E1.Contraseña import validarContraseña

from Validaciones.E2.DNI import validarDni
from Validaciones.E2.Edad import validarEdad


usuario=""
dicUsuarios={}
validar=True
usuario=input("Introduce el nombre de usuario, introdue '*' para terminar   ")
while usuario != "*":
    validar=validarUsuario(usuario)
    print(validar)
    if validar==True:       
        contraseña=input("Introduce la contraseña del usuario   ")
        validar=validarContraseña(contraseña)   
        print(validar)
        if validar==True:
            dni=input("Introduce tu DNI     ")
            validar=validarDni(dni)
            print(validar)
            if validar==True:
                edad=input("Introduce tu edad   ")
                validar=validarEdad(edad)
                print(validar)
                if validar==True:
                    if  usuario not in dicUsuarios:
                        dicUsuarios[usuario]={
                            "contraseña":contraseña,
                            "DNI":dni,
                            "Edad":edad
                        }
                        print("El usuario se ha creado correctamente    ")
                    else:
                        print("El usuario ya existe")
    usuario=input("Introduce el nombre de usuario, introdue '*' para terminar   ")

print(dicUsuarios)