from Validaciones.E1.Usuario import validarUsuario
from Validaciones.E1.Contraseña import validarContraseña

usuario=input("Introduce el nombre de usuario, introdue '*' para terminar   ")
dicUsuarios={}
validar=True
while usuario != "*":
    validar=validarUsuario(usuario)
    print(validar)
    if validar==True:
        contraseña=input("Introduce la contraseña del usuario   ")
        validar=validarContraseña(contraseña)   
        print(validar)     
        if validar==True:
            if usuario not in dicUsuarios:
                dicUsuarios[usuario]=contraseña
                print("El usuario se ha creado correctamente    ")
            else:
                print("El usuario ya existe")
    usuario=input("Introduce el nombre de usuario, introdue '*' para terminar   ")

print(dicUsuarios)