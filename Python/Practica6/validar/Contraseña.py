def validarContra(num):
    if len(num) < 8:
        print("el nombre de usuaruio debe contener al menos 6 caracteres") 
        return False
    if (num.isalnum()):
        return False
    else:
        if (num.islower()==True):
            return False
        if (num.upper()==True):
            return False
        if (num.isnumeric()==True):
            return False
        if (num.isspace()!=True):
            return False

    return True