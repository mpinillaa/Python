dicNombres={
    'Persona1':{
        'Nombre':'Sergio',
        'Gustos': 'Comer'
            }, 
    'Persona2':{
        'Nombre':'Juan',
        'Gustos': 'Bailar ', 
                },
    'Persona3':{
        'Nombre':'Enzo',
        'Gustos': 'Ver Series', 
    }
    }
count=5
exist=True
nombre=input("Introuce el nombre    ")

while nombre!="END":
    gustos=input("Introduce los gustos que quiere añadir    ")
    for p in dicNombres:
        if dicNombres[p]['Nombre']==nombre:
            dicNombres[p]['Gustos']+=", "+gustos
            exist=True
            break
        else:
            exist=False

    if exist==False:
        dicNombres[f'Persona{count}']={
                                    'Nombre':nombre,
                                    'Gustos':gustos,
                                        }
        count+=1
        exist=True
        
    print(dicNombres)
    nombre=input("Introuce el nombre    ")