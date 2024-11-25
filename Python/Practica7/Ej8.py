nombres=["carlos:","alberto:","judio:","albertojudio:","sergis:"]
saludos=["gay","ultragay","badgyal","megagay","si"]

resultado=([x.title().split()+y.split() for x in nombres for y in saludos])
print(resultado)


"""el y.split() es lo que pinta los slaudos es importante es igual que la i en los for"""