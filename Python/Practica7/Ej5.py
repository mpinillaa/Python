alumnos={"Carlos": 4, "sergio": 3, "Alberto": 6 }

listaaprobados=list(filter(lambda x: x[1]>=5,alumnos.items()))
print("Aprobados:   " +str(listaaprobados))


listaasuspensos=list(filter(lambda x: x[1]<5,alumnos.items()))
print("suspensos:   "+str(listaasuspensos))

nota=int(input("Anota la nota que quieres buscar:\n=>"))
buscaNota=list(filter(lambda x: x[1]>=nota, alumnos.items()))
print(buscaNota)

"""TE PONE LAS NOTAS SUPERIORIORES A LAS QUE HAS INTRODUCIDO"""