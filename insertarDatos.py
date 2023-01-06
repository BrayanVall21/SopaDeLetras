import random
from pymongo import MongoClient
def pedir_palabra():
    while True:
        palabra = input("Ingrese una palabra (máximo 6 caracteres): ")
        if len(palabra) > 6:
            print("La palabra ingresada es demasiado larga, por favor ingrese una palabra de 6 caracteres o menos.")
        else:
            return palabra

def crear_sopa(palabra1, palabra2, palabra3, palabra4):
    sopa = []
    for i in range(15):
        fila = []
        for j in range(15):
            fila.append("")
        sopa.append(fila)

    for i in range(len(palabra1)):
        sopa[0][i] = palabra1[i]
    for i in range(len(palabra2)):
        sopa[14][i] = palabra2[i]
    for i in range(len(palabra3)):
        sopa[i][0] = palabra3[i]
    for i in range(len(palabra4)):
        sopa[i][14] = palabra4[i]

    for i in range(15):
        for j in range(15):
            if sopa[i][j] == "":
                sopa[i][j] = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    return sopa
palabra1 = pedir_palabra()
palabra2 = pedir_palabra()
palabra3 = pedir_palabra()
palabra4 = pedir_palabra()
sopa = crear_sopa(palabra1, palabra2, palabra3, palabra4)

client = MongoClient()

db = client["sopas"]
coleccion = db["sopas"]
documento = {"palabra1": palabra1, "palabra2": palabra2, "palabra3": palabra3, "palabra4": palabra4, "sopa": sopa}

coleccion.insert_one(documento)

print(coleccion.find_one())
