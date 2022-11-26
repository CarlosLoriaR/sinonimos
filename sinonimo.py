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
    #SE ELIGEN 6 ELEMENTOS DEL ARREGLO DE PALABRAS Y SE GUARDAN EN UN ARREGLO LLAMADO PALABRA.
    palabra = random.sample(palabras,6) #PALABRA ES UN ARREGLO POR LO QUE SE NECESITA UN CICLO PARA BUSCAR LAS PALABRAS EN LA WEB
    sinonimo = []
    relaciones = []
    #CICLO DE i DESDE QUE ES 0 HASTA QUE ES 6
    for i in range(0,6):
        #SE BUSCA EN INTERNET LA PALABRA DEPENDIENDO DEL INDICE DEL ARREGLO
        buscar = url+palabra[i]
        resp = requests.get(buscar)
        soup = BeautifulSoup(resp.text)

        lista = soup.find(class_='trans clickable')
        sino = lista.find('li')
        Text = sino.next_element
        sincoma = re.sub(",","",Text)
        x = sincoma.split()
        #SE ELIJE AL AZAR UNO DE LOS SINONIMOS DE LA PALABRA QUE APAREZEN EN LA PAGINA WEB
        eleccion = random.choice(x)
        #SE AGREGAR LA PALABRA QUE SE BUSCO Y EL SINONIMO ELEJIDO Y SE GUARDA COMO UN ELEMENTO DE UN ARREGLOO
        relaciones.append([palabra[i], eleccion])
        #EL SINONIMO SELECCIONADO DE CADA PALABRA SE AGREGAR A UN ARREGLO DE SINONIMOS
        sinonimo.append(eleccion)
    #SE TOMAN TODOS LOS SINONIMOS DEL ARREGLOO SINONIMO Y SE REVUELVEN DE MANERA RANDOM
    sinonimor = random.sample(sinonimo,6)
    #VARIABLE PARA QUE APAREZCA EL NUMERO A LADO DE LOS SINONIMOS
    j=1
    #PRUEBA PARA QUE VEA COMO QUEDO EL ARREGLOO DE RELACIONES. TAL VEZ PUEDA SERVIR PARA VERIFICAR SI LAS RESPUESTAS FUERON CORRECTAS
    print(relaciones)
    for i in range(0,6):
        #SE IMPRIME LAS PALABRAS Y SINONIMOS. LOS SINONIMOS YA SE ENCUENTRAN EN DESORDEN
        print(palabra[i]+"\t\t",j,sinonimor[i])
        j=j+1

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
