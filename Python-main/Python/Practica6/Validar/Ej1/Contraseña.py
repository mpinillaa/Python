def validarContra(num):
    if len(num) < 8:
        print("el nombre de usuaruio debe contener al menos 6 caracteres")
        return False
    if (num.isalnum()):
        return False
    else:
        if (num.islower()==True):
            print("Debe tener mayusculas")
            return False
        if (num.upper()==True):
            print("debe tener mayusculas")
            return False
        if (num.isnumeric()==True):
            print("debe ser un numero")
            return False
        if (num.isspace()==True):
            print("no pudede tener espacios")
            return False
    return True