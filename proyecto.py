from tkinter import *
from tkinter.ttk import *

import json
import requests

from funciones import *

class ColorWindow(Toplevel):
  def __init__(self, color, master=None):
    super().__init__(master=master)
    window = self

    ## variables
    window.title("Psicología del color")
    window.geometry("600x400")
    
    armonies = armoniaColor(color)
    properties = caracteristicasColor(color)
    posfeel = sentimientosPositivos(color)
    negfeel = sentimientosNegativos(color)

    ## construir widgets
    titulo = Label(window, text="COLOR")
    titulo.grid(column=0, row=0)

    colorfrm = Frame(window, borderwidth=5, relief="ridge", width=140, height=140)
    colorhx = Label(window, text="#"+armonies['analogo'][2])
    colorfrm.grid(column=0, row=1, rowspan=4)
    colorhx.grid(column=0, row=4)

    colorlbl = Label(window, text=color.upper())
    colorlbl.grid(column=1, row=0)

    caracteristicaslbl = Label(window, text="Características")
    caracteristicastxt = Text(window, width=20, height=5)
    caracteristicastxt.insert(INSERT, "Categorías:" + "\n" 
    + '\n'.join(map(str, properties['categorias'])).title() 
    + "\nRangos de edad: \n" + ', '.join(map(str, properties['edades'])))
    caracteristicaslbl.grid(column=1, row=1)
    caracteristicastxt.grid(column=1, row=2)

    sigpositivos = Label(window, text="Significados evocados:")
    sigpositivostxt = Text(window, width=20, height=5)
    sigpositivostxt.insert(INSERT, '\n'.join(map(str, posfeel)).title())
    sigpositivos.grid(column=1, row=3)
    sigpositivostxt.grid(column=1, row=4)

    signegativos = Label(window, text="Significados negativos asociados:")
    signegativostxt = Text(window, width=40, height=5)
    signegativostxt.insert(INSERT, '\n'.join(map(str, negfeel)).title())
    signegativos.grid(column=0, row=5, columnspan=2)
    signegativostxt.grid(column=0, row=6, columnspan=2)

    # Menu con opciones de armonias
    ids = ['Análogo', 'Monocromático', 'Triada', 'Complementario', 'Separación Complementaria', 'Doble Separación Complementaria', 'Cuadro']
    vals = list(armonies.keys())
    options = dict(list(zip(ids, vals)))
    armonialbl = Label(window, text="Armonía")
    self.armoniacbx = Combobox(window, values=list(options.keys()))
    self.armoniacbx.current(0)
    armonialbl.grid(column=2, row=0, columnspan=2)
    self.armoniacbx.grid(column=2, row=1, columnspan=2)

    #### colores armonia ####
    color1 = Frame(window, borderwidth=5, relief="ridge", width=100, height=100)
    self.color1hex = StringVar()
    self.color1hex.set("#" + armonies[options[self.armoniacbx.get()]][0])
    color1lbl = Label(window, textvariable=self.color1hex)
    
    color2 = Frame(window, borderwidth=5, relief="ridge", width=100, height=100)
    self.color2hex = StringVar()
    self.color2hex.set("#" + armonies[options[self.armoniacbx.get()]][1])
    color2lbl = Label(window, textvariable=self.color2hex)

    color3 = Frame(window, borderwidth=5, relief="ridge", width=100, height=100)
    self.color3hex = StringVar()
    self.color3hex.set("#" + armonies[options[self.armoniacbx.get()]][3])
    color3lbl = Label(window, textvariable=self.color3hex)

    color4 = Frame(window, borderwidth=5, relief="ridge", width=100, height=100)
    self.color4hex = StringVar()
    self.color4hex.set("#" + armonies[options[self.armoniacbx.get()]][4])
    color4lbl = Label(window, textvariable=self.color4hex)
    
    color1.grid(column=2, row=2)
    color1lbl.grid(column=2, row=2)
    color2.grid(column=3, row=2)
    color2lbl.grid(column=3, row=2)
    color3.grid(column=3, row=4)
    color3lbl.grid(column=3, row=4)
    color4.grid(column=2, row=4)
    color4lbl.grid(column=2, row=4)

    def armony_changed(armonies, options):
      print(options[self.armoniacbx.get()])
      self.color1hex.set("#" + armonies[options[self.armoniacbx.get()]][0])
      self.color2hex.set("#" + armonies[options[self.armoniacbx.get()]][1])
      self.color3hex.set("#" + armonies[options[self.armoniacbx.get()]][3])
      self.color4hex.set("#" + armonies[options[self.armoniacbx.get()]][4])

    ## Se selecciona otra armonia
    self.armoniacbx.bind("<<ComboboxSelected>>", lambda elements: armony_changed(armonies, options))

## end ColorWindow

class selectColor(Toplevel):

  def accept(self,var, master=None):
    if(var.curselection()):
      ColorWindow(var.get(var.curselection()), master)
    
  def close(self):
    self.destroy()

  def __del__(self):
    print("Cerrando selector de color")
    # master.deiconify()

  def __init__(self, feel, age, category, record, menu, master=None, sinonimos=FALSE):

    super().__init__(master = master)
    # master.withdraw()

    Nelement = {"feel":feel, "age":age, "category":category}
    label = ""
    label += "Sentimientos: {}  ".format(Nelement["feel"]) if len(Nelement["feel"]) != 0 else ""
    label += "Edad: {}  ".format(Nelement["age"]) if len(Nelement["age"]) != 0 else ""
    label += "Categoria: {}  ".format(Nelement["category"]) if len(Nelement["category"]) != 0 else ""
    if(label not in record.keys()):
      record[label] = Nelement
      menu.delete(0, END)
      menu.insert(0,*record.keys())

    feels = (re.split(",,| , |, |,| ,",feel.lower()))

    listFeels = [] + feels

    if(sinonimos):
      for f in feels:
        try:
          response = requests.get("http://sesat.fdi.ucm.es:8080/servicios/rest/sinonimos/json/"+f, timeout=0.5)
        except Exception as e:
          print(e)
        else:
          if(response.status_code == 200):
            sinonimos = response.json()["sinonimos"]
            for sinonimo in sinonimos:
              listFeels.append(sinonimo["sinonimo"])
          else:
            print(response.status_code)
      
    print(listFeels)

    self.title('Psicologia del color')
    self.configure(width=300, height=300)
    self.option_add("*Label.Font", "helvetica 50 bold")

    colores = buscarCoincidencias(listFeels,age,category)

    scrollbar = Scrollbar(self, orient="vertical")
    selectMenu = Listbox(self,yscrollcommand=scrollbar.set, width=15, height=6, selectmode=SINGLE)
    scrollbar.config(command=selectMenu.yview)
    selectMenu.insert(END, *colores)
    scrollbar.pack(side=LEFT, fill=Y)
    selectMenu.pack(side=LEFT)

    buttonAccept = Button(self, text="aceptar")
    buttonAccept.bind("<Button>", lambda color: self.accept(selectMenu, self))
    buttonAccept.pack(side=RIGHT)

    buttonCancel = Button(self, text="cancelar")
    buttonCancel.bind("<Button>", lambda _ : self.close())
    buttonCancel.pack(side=RIGHT)

if __name__ == "__main__":
  recordH = [
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
    item = record[selected.get(selected.curselection())]
    
    feel.delete(0,END)
    feel.insert(0,item["feel"])
    age.set(item["age"])
    category.set(item["category"])

  record = {}
  for dictionary in recordH:
    label = ""
    label += "Sentimientos: {}  ".format(dictionary["feel"]) if len(dictionary["feel"]) != 0 else ""
    label += "Edad: {}  ".format(dictionary["age"]) if len(dictionary["age"]) != 0 else ""
    label += "Categoria: {}  ".format(dictionary["category"]) if len(dictionary["category"]) != 0 else ""
    record[label] = dictionary
    
  selectMenu.insert(END, *record.keys())
  selectMenu.place(relx=0.65, rely=0.4, width=(width*0.3), height=(height*0.5))
  scrollbar.place(relx=0.95, rely=0.4, height=(height*0.5))
  selectMenu.bind("<Double-1>", lambda elements: reasignValues(entry1,age,category,selectMenu))

  def validateEntries(feel,age,category,record,selectMenu,master,sinonimos):
    if((len(feel) > 0) or (len(age) > 0) or (len(category) > 0)):
      try:
        selectColor(feel,age,category,record,selectMenu,master,sinonimos)
      except:
        master.deiconify()

  isChecked = IntVar()
  checkbutton = Checkbutton(master, text="Buscar sinonimos en la red", variable=isChecked)
  checkbutton.place(relx=0.06, rely=0.8)

  btn = Button(master, text="Buscar coincidencias")
  btn.bind("<Button>", lambda e: validateEntries(entry1.get(),age.get(),category.get(),record,selectMenu,master,isChecked.get()))
  btn.place(relx=0.28, rely=0.8, width=(width*0.36))

  mainloop()