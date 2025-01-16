def validarUsuario(u):
    if(len(u)<6):
        print("El nombre de usuario debe contener al menos 6 caracteres")
        return False
    elif(len(u)>12):
        print("El nombre de usuario no puede contener más de 12 caracteres")
        return False
    if(u.isalnum()==False):
        print("El nombre de usuario puede contener solo letras y números")
        return False
    
    return True