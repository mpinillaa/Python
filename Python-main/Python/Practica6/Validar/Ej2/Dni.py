def validarDni(num):
    if len(num)!=9:
        print("El dni debe tener 9 digitos")
        return False
    if num[-1].isalpha()==False:
        print("debe ser un numero")
        return False
    if num[0:-1].isdigit()==False:
        print("los primeros 8 numeros deben ser numeros")
        return False
    return True    
