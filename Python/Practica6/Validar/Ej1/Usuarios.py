def validarUsu(num):
    if len(num) < 6:
        print("el nombre de usuaruio debe contener al menos 6 caracteres") 
        return False
    elif len(num) > 12:
        print("el nombre de usuaruio debe contener  menos de 12 caracteres") 
        return False
        
    if (num.isalnum()==False):
        print("el nombre de usuaruio  puede contener solo l y nums") 
        return False
    
    return True