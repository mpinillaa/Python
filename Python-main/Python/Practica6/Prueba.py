from validar.Usuarios import validarUsu
from validar.Contraseña import validarContra


usuario=input("usuario:  ")

usuarios="Albertostas"
validar=validarUsu(usuarios)
print(validar)


contraseña="CAngre*  jo23*"
validar= validarContra(contraseña)
print(validar)