from tarjeta import Tarjeta

t=Tarjeta("1111A")
q=Tarjeta("2222B", 2000)

#print(t.consultar_saldo())

#print(t.consultar_saldo)
print(t.saldo)
t.saldo=3000

#print(t._Tarjeta__saldo)

print(Tarjeta.comision)

t.ingresar(500)

print(t)
print(q)
