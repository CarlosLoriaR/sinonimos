from tkinter import *
from tkinter import ttk
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
#COLUMNA IZQUIERDA
anc = NW
w=150
h=30
fet=('Arial',16)
lbl1 = Label(ventana,font=fet,anchor=anc)
lbl1.place(x=200,y=100,width=w,height=h)

lbl2 = Label(ventana, font=fet,anchor=anc)
lbl2.place(x=200,y=150,width=w,height=h)

lbl3 = Label(ventana, font=fet,anchor=anc)
lbl3.place(x=200,y=200,width=w,height=h)

lbl4 = Label(ventana, font=fet,anchor=anc)
lbl4.place(x=200,y=250,width=w,height=h)

lbl5 = Label(ventana, font=fet,anchor=anc)
lbl5.place(x=200,y=300,width=w,height=h)

lbl6 = Label(ventana, font=fet,anchor=anc)
lbl6.place(x=200,y=350,width=w,height=h)

#COLUMNA DERECHA
wn = 50
fnum =('Arial', 16, 'bold')
bg= '#1300EB'
lbl13 = Label(ventana, font=fnum,anchor=anc,fg=bg)
lbl13.place(x=450,y=100,width=wn,height=h)
lbl7 = Label(ventana, font=fet,anchor=anc)
lbl7.place(x=500,y=100,width=w,height=h)

lbl14 = Label(ventana, font=fnum,anchor=anc,fg=bg)
lbl14.place(x=450,y=150,width=wn,height=h)
lbl8 = Label(ventana,font=fet,anchor=anc)
lbl8.place(x=500,y=150,width=w,height=h)

lbl15 = Label(ventana, font=fnum,anchor=anc,fg=bg)
lbl15.place(x=450,y=200,width=wn,height=h)
lbl9 = Label(ventana,font=fet,anchor=anc)
lbl9.place(x=500,y=200,width=w,height=h)

lbl16 = Label(ventana, font=fnum,anchor=anc,fg=bg)
lbl16.place(x=450,y=250,width=wn,height=h)
lbl10 = Label(ventana, font=fet,anchor=anc)
lbl10.place(x=500,y=250,width=w,height=h)

lbl17 = Label(ventana, font=fnum,anchor=anc,fg=bg)
lbl17.place(x=450,y=300,width=wn,height=h)
lbl11 = Label(ventana, font=fet,anchor=anc)
lbl11.place(x=500,y=300,width=w,height=h)

lbl18 = Label(ventana, font=fnum,anchor=anc,fg=bg)
lbl18.place(x=450,y=350,width=wn,height=h)
lbl12 = Label(ventana, font=fet,anchor=anc)
lbl12.place(x=500,y=350,width=w,height=h)

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
    #print(relaciones)
    #for i in range(0,6):
        #SE IMPRIME LAS PALABRAS Y SINONIMOS. LOS SINONIMOS YA SE ENCUENTRAN EN DESORDEN
     #   print(palabra[i]+"\t\t",j,sinonimor[i])
      #  j=j+1

    wcbx = 50
    hcbx =30
    st= 'readonly'
    val= ['1','2','3','4','5','6']
    cbx1 = ttk.Combobox(ventana,state=st,values=val,font=fet)
    cbx1.place(x=330,y=100,width=wcbx,height=hcbx)
    lbl1.config(text=palabra[0])
    lbl13.config(text=j)
    lbl7.config(text=sinonimor[0])

    cbx2 = ttk.Combobox(ventana,state=st,values=val,font=fet)
    cbx2.place(x=330,y=150,width=wcbx,height=hcbx)
    lbl2.config(text=palabra[1])
    lbl14.config(text=j+1)
    lbl8.config(text=sinonimor[1])

    cbx3 = ttk.Combobox(ventana,state=st,values=val,font=fet)
    cbx3.place(x=330,y=200,width=wcbx,height=hcbx)
    lbl3.config(text=palabra[2])
    lbl15.config(text=j+2)
    lbl9.config(text=sinonimor[2])

    cbx4 = ttk.Combobox(ventana,state=st,values=val,font=fet)
    cbx4.place(x=330,y=250,width=wcbx,height=hcbx)
    lbl4.config(text=palabra[3])
    lbl16.config(text=j+3)
    lbl10.config(text=sinonimor[3])

    cbx5 =ttk.Combobox(ventana,state=st,values=val,font=fet)
    cbx5.place(x=330,y=300,width=wcbx,height=hcbx)
    lbl5.config(text=palabra[4])
    lbl17.config(text=j+4)
    lbl11.config(text=sinonimor[4])

    cbx6 = ttk.Combobox(ventana,state=st,values=val,font=fet)
    cbx6.place(x=330,y=350,width=wcbx,height=hcbx)
    lbl6.config(text=palabra[5])
    lbl18.config(text=j+5)
    lbl12.config(text=sinonimor[5])

# DISEÑO
h1 = Label(ventana, text="Bienvenido a Syno\n ¿Listo para poner a prueba tus habilidades de vocabulario?")
h1.place(x=200,y=10,width=400,height=30)
btn = Button(ventana, text="Comenzar", command=Sinonimos)
btn.place(x=350,y=40,width=100,height=30)


# REDIRECCIONAR RESULTADOS DE CONSOLA A VENTANA
# class StdOutRedirect:
#      def __init__(self,  text: tk.Text) -> None:
#          self._text = text

#      def write(self,  out: str) -> None:
#          self._text.insert(tk.END,  out)


# class App(tk.Frame):
#      def __init__(self, parent, *args, **kwargs):
#          super().__init__(parent,  *args, **kwargs)
#          self.stdout_text = tk.Text(
#              self, font=("Helvetica", 15))
#          self.stdout_text.place(x=10,y=10,width=600,height=100)
#          sys.stdout = StdOutRedirect(self.stdout_text)


# if __name__ == "__main__":
#      App(ventana).place(x=100,y=100,width=600,height=100)

ventana.mainloop()
