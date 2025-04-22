import json
import csv


def get_datos():
 with open("/home/administrador/Escritorio/Python-main (2)/Python/3eva/examenRecu/assets/datos.json", "r", encoding="utf-8") as fichero:

        datos = json.load(fichero)
        return datos


def get_charlasaforo(datos, porcentaje):
    resul = {}
    for sala in datos:
        limite = sala["aforo"] * (porcentaje / 100)   
        charlasfilt = list(filter(lambda charla: charla["entradasvendidas"] < limite, sala["charlas"]))
        if charlasfilt:
            resul[sala["numero_sala"]] = charlasfilt

    return resul


def venta_entradas(datos, tema, entradasvender):
    for sala in datos:
        for charla in sala["charlas"]:
            if charla["tema"].lower() == tema.lower():
                disponibles = sala["aforo"] - charla["entradasvendidas"]
                if entradasvender <= disponibles:
                    charla["entradasvendidas"] += entradasvender
                    sala["recaudacion"] += entradasvender * charla["precio"]
                    return True
                else:
                    return False
    return False


#def generar_csv(datos):
 #   with open("assets/generar.csv", "w", newline="", encoding="utf-8") as archivo:
  #      writer = csv.writer(archivo)
   