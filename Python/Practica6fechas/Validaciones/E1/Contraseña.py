import re
def validarContraseña(c):
    cont=0
    cont2=0
    if len(c)<8:
        print("La contraseña debera tener al menos 8 caracteres")
        return False
    if re.search(r"/ [A-Z] /",c)==False:
        print("La contraseña debera tener al menos una letra en mayusculas")
        return False    
    if re.search(r"/ [a-z] /",c)==False:
        print("La contraseña debera tener al menos una letra en minusculas")
        return False    
    if re.search(r"/ \d /",c)==False:
        print("La contraseña debera tener al menos un digito")
        return False
    if c.isalnum()==True:
        print("La contraseña no debera ser alfanumerico")
        return False
    if c.isspace()==True:
        print("La contraseña no puede tener espacios")
        return False
    return True