from tkinter import *
import requests
from bs4 import BeautifulSoup
import sys
import tkinter as tk
import re

# VENTANA
ventana = Tk()
ventana.geometry("800x600")
ventana.title("Syno - Juego de Sinonimos")

url = 'https://www.wordreference.com/sinonimos/'
buscar = url+"Amor"
resp = requests.get(buscar)
soup = BeautifulSoup(resp.text)

lista = soup.find(class_='trans clickable')
sino = lista.find('li')

#Esto es una prueba
def Sinonimos():
    Text = sino.next_element
    sincoma = re.sub(",","",Text)
    x = sincoma.split()
    print(x[0]+"\n"+x[1])

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
