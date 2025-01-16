def day(d,m):
    
    fecha30=(4, 6, 9, 11)
    fecha31=(1, 3, 5, 7, 8, 10, 12)
    febrero=2

    if m in fecha30: dias=30
    elif m in fecha31: dias=31
    else: dias=28
    
    if int(d)>int(dias) or int(d)<1:return "ERROR"
    else:return str(d)
    