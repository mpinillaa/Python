from Validaciones.E2.DNI import validarDni
from Validaciones.E2.Edad import validarEdad

dni="72007249E"
validar=validarDni(dni)
print(validar)

validar=validarEdad("18")
print(validar)