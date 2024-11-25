def validarEdad(edad):
    if int(edad)<18:
        print("la edad debe ser mayor de 18 años")
        return False
    return True