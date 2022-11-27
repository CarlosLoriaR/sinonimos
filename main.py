from sinonimo import *
def Empezar():
    #OCULTA LA VENTANA ACTUAL Y MUESTRA LA DE SINONIMOS
    main.withdraw()
    Sinonimos()

main = Tk()
main.geometry("800x500+100+30")
main.title("Syno")
main.resizable(width=FALSE,height=FALSE)
h1 = Label(main, text="Bienvenidos a SyNo\n",font=("Helvetica",40))
h1.place(x=120,y=50,width=500,height=120)
descripcion = Label(main, text="Este es un juego para probar tus habilidades de vocabulario, se te mostraran\ndos listas de palabras y tendrás que relacionar las que sean sinonimos.",font=("Helvetica",16),justify="left")
descripcion.place(x=20,y=130)

ayudanos = Label(main, text="AYUDANOS A EVALUARTE\nAntes de comenzar busca un papel y una hoja para\nllevar tu puntuacion, al final comparala con la nuestra.",font=("Helvetica",16),justify="left")
ayudanos.config(fg="red")
ayudanos.place(x=250,y=270)

#LLama a la funcion Empezar
btn = Button(main, text="Empezar Juego", command=Empezar,bd=5,padx=20,pady=5,font=("Arial",30))
btn.place(x=200,y=400,width=400)

main.mainloop()