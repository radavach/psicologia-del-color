from tkinter import *
from tkinter.ttk import *
import json

from funciones import *

class colorWindow(Toplevel):
  def __init__(self,master = None):
    super().__init__(master = master)

    ventana = self

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

  # ventana.mainloop()

class selectColor(Toplevel):

  def accept(self,var):
    print(var.get(var.curselection()))
    
  def close(self):
    self.destroy()

  def __del__(self):
    
    master.deiconify()

  def __init__(self, feel, age, category, record, menu, master=None):

    super().__init__(master = master)
    master.withdraw()

    record.insert(0,{"feel":feel, "age":age, "category":category})
    menu.delete(0, END)
    menu.insert(0,*record)

    self.title('Psicologia del color')
    self.configure(width=300, height=300)
    self.option_add("*Label.Font", "helvetica 50 bold")

    colores = cargarColoresPositivos()

    scrollbar = Scrollbar(self, orient="vertical")
    selectMenu = Listbox(self,yscrollcommand=scrollbar.set, width=15, height=6, selectmode=SINGLE)
    scrollbar.config(command=selectMenu.yview)
    selectMenu.insert(END, *colores)
    scrollbar.pack(side=LEFT, fill=Y)
    selectMenu.pack(side=LEFT)

    buttonAccept = Button(self, text="aceptar")
    buttonAccept.bind("<Button>", lambda color: self.accept(selectMenu))
    buttonAccept.pack(side=RIGHT)

    buttonCancel = Button(self, text="cancelar")
    buttonCancel.bind("<Button>", lambda _ : self.close())
    buttonCancel.pack(side=RIGHT)

if __name__ == "__main__":
  record = [
    {"feel": "felicidad", "age": "1-18", "category": ""},
    {"feel": "", "age": "25-35", "category":"frio"},
    {"feel": "exitacion", "age": "1-18", "category": "frio"}]

  master = Tk()
  master.title('Psicologia del color')
  master.option_add("*Label.Font", "helvetica 50 bold")
  master.configure(width=900, height=300)
  width = master.winfo_reqwidth()
  height = master.winfo_reqheight()

  label = Label(master, text="Psicologia del color", font="Arial 40 bold")
  label.place(relx=0.06, rely=0.08)

  label = Label(master, text="Sentimiento:", font="Arial 12")
  label.place(relx=0.06, rely=0.4)
  entry1 = Entry(master)
  entry1.place(relx=0.28, rely=0.4, width=(width*0.36))

  ages = cargarEdades()
  ages.append("")
  age = StringVar(master)
  label = Label(master, text="Publico objetivo:", font="Arial 12")
  label.place(relx=0.06, rely=0.54)
  menu1 = OptionMenu(master, age, age.get(), *ages)
  menu1.place(relx=0.28, rely=0.54, width=(width*0.36))

  categories = cargarCategorias()
  categories.append("")
  category = StringVar(master)
  label = Label(master, text="Categoria:", font="Arial 12")
  label.place(relx=0.06, rely=0.68)
  menu1 = OptionMenu(master, category, category.get(), *categories)
  menu1.place(relx=0.28, rely=0.68, width=(width*0.36))

  scrollbar = Scrollbar(master, orient="vertical")
  selectMenu = Listbox(master,yscrollcommand=scrollbar.set, bg='#D9D4D0', selectmode=SINGLE)
  scrollbar.config(command=selectMenu.yview)

  def reasignValues(feel,age,category,selected):
    item = json.loads(re.sub("'",'"',selected.get(selected.curselection())))
    
    feel.delete(0,END)
    feel.insert(0,item["feel"])
    age.set(item["age"])
    category.set(item["category"])

  selectMenu.insert(END, *record)
  selectMenu.place(relx=0.65, rely=0.4, width=(width*0.3), height=(height*0.5))
  scrollbar.place(relx=0.95, rely=0.4, height=(height*0.5))
  selectMenu.bind("<Double-1>", lambda elements: reasignValues(entry1,age,category,selectMenu))

  def validateEntries(feel,age,category,record,selectMenu,master):
    if((len(feel) > 0) or (len(age) > 0) or (len(category) > 0)):
      selectColor(feel,age,category,record,selectMenu,master)

  btn = Button(master, text="Buscar coincidencias")
  btn.bind("<Button>", lambda e: validateEntries(entry1.get(),age.get(),category.get(),record,selectMenu,master))
  btn.place(relx=0.28, rely=0.8, width=(width*0.36))

  mainloop()