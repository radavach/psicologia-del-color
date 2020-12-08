from tkinter import *
from tkinter.ttk import *

from funciones import *

if __name__ == "__main__":

  categorias = cargarCategorias()
  coloresArm = cargarColoresArmonia()
  coloresPos = cargarColoresPositivos()
  coloresNeg = cargarColoresNegativos()

  ventana = Tk()

  ventana.title('Psicologia del color')
  ventana.geometry("640x160")
  ventana.option_add("*Label.Font", "helvetica 50 bold")

  opcion1 = StringVar(ventana)
  opcion1.set(categorias[0])
  etiqueta1 = Label(ventana, text="Categoria de colores", font="Helvetica 10 bold italic")
  etiqueta1.grid(row=0, column=0)
  entrada1 = OptionMenu(ventana, opcion1, opcion1.get(), *categorias)
  entrada1.grid(row=0, column=1)
  boton1 = Button(ventana, text="Categoria", command=lambda: obtenerColoresPorCategoria(opcion1.get()))
  boton1.grid(row=0, column=2)

  etiqueta2 = Label(ventana, text="Colores por edad", font="Helvetica 10 bold italic")
  etiqueta2.grid(row=1, column=0)
  entrada2 = Entry(ventana)
  entrada2.grid(row=1, column=1)
  boton2 = Button(ventana, text="Preferencias", command=lambda: obtenerColoresPorCategoria(opcion1.get()))
  boton2.grid(row=1, column=2)

  opcion3 = StringVar(ventana)
  opcion3.set(coloresPos[0])
  etiqueta3 = Label(ventana, text="Sentimientos positivos por color", font="Helvetica 10 bold italic")
  etiqueta3.grid(row=2, column=0)
  entrada3 = OptionMenu(ventana, opcion3, opcion3.get(), *coloresPos)
  entrada3.grid(row=2, column=1)
  boton3 = Button(ventana, text="Sentimientos positivos", command=lambda: obtenerColoresPorCategoria(opcion1.get()))
  boton3.grid(row=2, column=2)

  opcion4 = StringVar(ventana)
  opcion4.set(coloresNeg[0])
  etiqueta4 = Label(ventana, text="Sentimientos negativos por color", font="Helvetica 10 bold italic")
  etiqueta4.grid(row=3, column=0)
  entrada4 = OptionMenu(ventana, opcion4, opcion4.get(), *coloresNeg)
  entrada4.grid(row=3, column=1)
  boton4 = Button(ventana, text="Sentimientos negativos", command=lambda: obtenerColoresPorCategoria(opcion1.get()))
  boton4.grid(row=3, column=2)

  opcion5 = StringVar(ventana)
  opcion5.set(coloresArm[0])
  etiqueta5 = Label(ventana, text="Armonia del color...", font="Helvetica 10 bold italic")
  etiqueta5.grid(row=4, column=0)
  entrada5 = OptionMenu(ventana, opcion5, opcion5.get(), *coloresArm)
  entrada5.grid(row=4, column=1)
  boton5 = Button(ventana, text="Combinaciones", command=lambda: obtenerColoresPorCategoria(opcion1.get()))
  boton5.grid(row=4, column=2)

  ventana.mainloop()
