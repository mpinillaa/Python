class Tarjeta():
    comision=0.05
    
    def __init__(self,id,cantidad=1000):
        self.__id=id
        self.__saldo=cantidad
        
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self,cantidad):
        self.__saldo=cantidad 
        
    @property
    def identificador(self):
        return self.__id    
    
    def __str__(self):
        return "id" + self.__id + "\n" + "saldo: " + str(self.__saldo)
    

        
   # def consultar_saldo(self):
    #    return self.saldo
    
    def ingresar(self,cantidad):
        self.__saldo+=cantidad
        
    def reintegrar(self,cantidad):
        if (cantidad+cantidad*Tarjeta.comision>self.__saldo):
            return False
        self.__saldo-=cantidad+cantidad*self.comision