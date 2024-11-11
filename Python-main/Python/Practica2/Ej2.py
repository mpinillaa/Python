
mes=int(input("numero a sacar del 1 al 12:  "))
while mes<=0 | mes>12:
    mes= int(input("  Debes intriducir un mes valido del 1 al 12  "))
    
fecha31 = (1,3,5,7,8,10,12)
fecha30 = (4,6,9,11)
feb = 2
    
if mes in fecha31:
    print("tiene 31 dias")
elif mes in fecha30:
    print("tiene 30 dias ")
else:
    print("tiene 28 dias")
    
    
