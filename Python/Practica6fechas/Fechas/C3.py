def monthName(fecha):
    mes=["enero", "febrero", "marzo", "abril", "mayo", "junio", "agosto", "septiembre",
         "octubre", "nobiembre", "diciembre"]
    if mes[int(fecha)-1]: return(str(mes[int(fecha)-1]))
    else: return "ERROR"