from sinonimo import *
def Empezar():
    #OCULTA LA VENTANA ACTUAL Y MUESTRA LA DE SINONIMOS
    main.withdraw()
    Sinonimos()

main = Tk()
main.geometry("800x600+100+30")
main.title("Syno - Juego de Sinonimos")
h1 = Label(main, text="Bienvenido a Syno\n ESTA ES UNA PRUEBA DE MENU")
h1.place(x=200,y=10,width=400,height=30)
#LLama a la funcion Empezar
btn = Button(main, text="Empezar", command=Empezar)
btn.place(x=350,y=400,width=100,height=30)

main.mainloop()