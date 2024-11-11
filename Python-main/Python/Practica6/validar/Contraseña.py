def validarContra(num):
    if len(num) < 8:
        print("el nombre de usuaruio debe contener al menos 6 caracteres") 
        return False
    if (num.isalnum()):
        print("debe contener un alfanumerico")
        return False
    else:
        if (num.islower()==True):
            print("debe contener una minuscula")
            return False
        if (num.upper()==True):
            print("debe contener una mayuscula")
            return False
        if (num.isnumeric()==True):
            print("debe contner un digito")
            return False
        if (num.isspace()==True):
            print("no debe tener espacios")
            return False

    return True