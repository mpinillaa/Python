def contador(envio): 
   with open("Practica9ficheros/Ficheros/Contador.txt", "r") as fichero:
       contador=fichero.read()
       
   if contador=="":
        contador=0
   else:
        contador=int(contador)
        
   if envio == "Inc":
       contador+=1
       print(contador)
   elif envio == "Dec":
       contador-=1
       print(contador)
       
   with open("Practica9ficheros/Ficheros/Contador.txt", "w") as fichero:
       fichero.write(str(contador))
       
contador("Inc")