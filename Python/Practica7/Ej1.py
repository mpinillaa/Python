lista=[1,2,3,4,5,6]
listaPares=list(filter(lambda x: x%2==0, lista))
print(listaPares)


lista2=[1,2,3,4,5,6]
listaPares2=list(map(lambda x: x%2==0, lista))
print(listaPares2)