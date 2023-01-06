import tkinter as tk
from pymongo import MongoClient

ventana = tk.Tk()
ventana.title("Sopa de letras")

client = MongoClient()

db = client["sopas"]
coleccion = db["sopas"]

documento = coleccion.find().sort("_id", -1).limit(1)

sopa = next(documento)["sopa"]

for i in range(len(sopa)):
    for j in range(len(sopa[i])):
        tk.Label(ventana, text=sopa[i][j]).grid(row=i, column=j)

ventana.mainloop()