def validarDni(e):
   if len(e)!=9:
       print("Error en la longitud del DNI")
       return False
   if e[-1].isalpha()==False:
       print("La ultima posicion tiene que ser una letra")
       return False
   if e[0:-1].isdigit()==False:
       print("Todas las posiciones menos la utlima tienen que ser numeros")
       return False
   return True