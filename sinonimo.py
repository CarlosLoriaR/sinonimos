from tkinter import *
import requests
from bs4 import BeautifulSoup
import sys
import tkinter as tk
import re
import random
#INICIALIZACIÓN
palabras = ['definicion', 'trabajo', 'desarrollo', 'concepto', 'respuesta', 'opcion', 'problema', 'apoyo']


# VENTANA
ventana = Tk()
ventana.geometry("800x600")
ventana.title("Syno - Juego de Sinonimos")


#Esto es una prueba
def Sinonimos():
    url = 'https://www.wordreference.com/sinonimos/'
    palabra = random.sample(palabras,6)
    for i in range(0,8):
        buscar = url+palabra[i]
        resp = requests.get(buscar)
        soup = BeautifulSoup(resp.text)

        lista = soup.find(class_='trans clickable')
        sino = lista.find('li')
        Text = sino.next_element
        sincoma = re.sub(",","",Text)
        x = sincoma.split()
        print(palabra[i]+"\t\t"+x[0])

# DISEÑO
h1 = Label(ventana, text="Bienvenido a Syno\n ¿Listo para poner a prueba tus habilidades de vocabulario?")
h1.pack()
btn = Button(ventana, text="Presionar", command=Sinonimos)
btn.pack()

# REDIRECCIONAR RESULTADOS DE CONSOLA A VENTANA
class StdOutRedirect:
    def __init__(self,  text: tk.Text) -> None:
        self._text = text

    def write(self,  out: str) -> None:
        self._text.insert(tk.END,  out)


class App(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent,  *args, **kwargs)
        self.stdout_text = tk.Text(
            self, font=("Helvetica", 15))
        self.stdout_text.pack(expand=True, fill=tk.BOTH)
        sys.stdout = StdOutRedirect(self.stdout_text)


if __name__ == "__main__":
    App(ventana).pack(expand=True, fill=tk.BOTH)

ventana.mainloop()
