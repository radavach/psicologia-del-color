from tkinter import *
from tkinter.ttk import *
from tkinter.scrolledtext import *

import json
import requests

from funciones import *

class ColorWindow(Toplevel):
  def __init__(self, color, master=None):
    super().__init__(master=master)
    
    window = self

    ## variables
    window.title("Psicología del color")
    window.geometry("680x480")
    
    armonies = armoniaColor(color)
    properties = caracteristicasColor(color)
    posfeel = sentimientosPositivos(color)
    negfeel = sentimientosNegativos(color)

    ## construir widgets
    titulo = Label(window, text="COLOR", font=("Helvetica", 30, "bold"), anchor="w")
    titulo.grid(column=0, row=0, sticky=(N, W, E, S), padx=(50, 0), pady=(50, 5))

    s = Style()
    s.configure('My.TFrame', background="#"+armonies['analogo'][2])
    colorfrm = Frame(window, borderwidth=5, relief="ridge", width=140, height=140, style='My.TFrame')
    self.hx = StringVar()
    self.hx.set("#"+armonies['analogo'][2])
    colorhx = Entry(window, textvariable=self.hx, justify="center", style='TLabel', state='readonly', font="Helvetica", width=10)
    colorfrm.grid(column=0, row=1, rowspan=4, sticky=(N,W), padx=(50, 10))
    colorhx.grid(column=0, row=4, sticky=(N, W, E, S), padx=(50, 10), pady=10)

    colorlbl = Label(window, text=color.upper(), font=("Helvetica", 20, "bold"), foreground="#"+armonies['analogo'][2], anchor="w")
    colorlbl.grid(column=1, row=0, sticky=(W, S), pady=(50, 5))

    caracteristicaslbl = Label(window, text="Características", font="Helvetica")
    caracteristicastxt = ScrolledText(window, width=20, height=4, font=("Helvetica",11))
    caracteristicastxt.insert(INSERT, "Categorías:" + "\n" 
    + '\n'.join(map(str, properties['categorias'])).title() 
    + "\nRangos de edad: \n" + ', '.join(map(str, properties['edades'])))
    caracteristicastxt.configure(state="disabled")
    caracteristicaslbl.grid(column=1, row=1, sticky=(N, W, E, S))
    caracteristicastxt.grid(column=1, row=2, sticky=(N, W, E, S))

    sigpositivos = Label(window, text="Significados evocados:", font="Helvetica")
    sigpositivostxt = ScrolledText(window, width=20, height=4, font=("Helvetica",11))
    sigpositivostxt.insert(INSERT, '\n'.join(map(str, posfeel)).title())
    sigpositivostxt.configure(state='disabled')
    sigpositivos.grid(column=1, row=3, sticky=(N, W, E, S), pady=(10,0))
    sigpositivostxt.grid(column=1, row=4, sticky=(N, W, E, S))

    signegativos = Label(window, text="Significados negativos asociados:", font="Helvetica")
    signegativostxt = ScrolledText(window, width=40, height=4, font=("Helvetica",11))
    signegativostxt.insert(INSERT, '\n'.join(map(str, negfeel)).title())
    signegativostxt.configure(state="disabled")
    signegativos.grid(column=0, row=5, columnspan=2, sticky=(N, W, E, S), padx=(50, 10), pady=(10,0))
    signegativostxt.grid(column=0, row=6, columnspan=2, sticky=(N, W, E, S), padx=(50, 0))

    # Menu con opciones de armonias
    ids = ['Análogo', 'Monocromático', 'Triada', 'Complementario', 'Separación Complementaria', 'Doble Separación Complementaria', 'Cuadro']
    vals = list(armonies.keys())
    options = dict(list(zip(ids, vals)))
    armonialbl = Label(window, text="Armonía", font="Helvetica")
    self.armoniacbx = Combobox(window, values=list(options.keys()), font=("Helvetica",11))
    self.armoniacbx.current(0)
    armonialbl.grid(column=2, row=0, columnspan=2, sticky=(W,S,E), pady=(50, 5), padx=(10,0))
    self.armoniacbx.grid(column=2, row=1, columnspan=2, sticky=(W,E), padx=(10,0))

    #### colores armonia ####
    s.configure('My1.TFrame', background="#"+armonies[options[self.armoniacbx.get()]][0])
    self.color1 = Frame(window, borderwidth=5, relief="ridge", width=100, height=100, style="My1.TFrame")
    self.color1hex = StringVar()
    self.color1hex.set("#" + armonies[options[self.armoniacbx.get()]][0])
    self.color1lbl = Entry(window, textvariable=self.color1hex, width=7, justify="center", style='TLabel', state='readonly', font="Helvetica")
    
    s.configure('My2.TFrame', background="#"+armonies[options[self.armoniacbx.get()]][1])
    self.color2 = Frame(window, borderwidth=5, relief="ridge", width=100, height=100, style="My2.TFrame")
    self.color2hex = StringVar()
    self.color2hex.set("#" + armonies[options[self.armoniacbx.get()]][1])
    self.color2lbl = Entry(window, textvariable=self.color2hex, width=7, justify="center", style='TLabel', state='readonly', font="Helvetica")

    s.configure('My3.TFrame', background="#"+armonies[options[self.armoniacbx.get()]][3])
    self.color3 = Frame(window, borderwidth=5, relief="ridge", width=100, height=100, style="My3.TFrame")
    self.color3hex = StringVar()
    self.color3hex.set("#" + armonies[options[self.armoniacbx.get()]][3])
    self.color3lbl = Entry(window, textvariable=self.color3hex, width=7, justify="center", style='TLabel', state='readonly', font="Helvetica")

    s.configure('My4.TFrame', background="#"+armonies[options[self.armoniacbx.get()]][4])
    self.color4 = Frame(window, borderwidth=5, relief="ridge", width=100, height=100, style="My4.TFrame")
    self.color4hex = StringVar()
    self.color4hex.set("#" + armonies[options[self.armoniacbx.get()]][4])
    self.color4lbl = Entry(window, textvariable=self.color4hex, width=7, justify="center", style='TLabel', state='readonly', font="Helvetica")
    
    self.color1.grid(column=2, row=2, rowspan=2, padx=(10,0), pady=(10,0))
    self.color1lbl.grid(column=2, row=2, rowspan=2, sticky=(N,S,E,W), padx=(19,9), pady=(20,10))
    self.color2.grid(column=3, row=2, rowspan=2, padx=(10,0), pady=(10,0))
    self.color2lbl.grid(column=3, row=2, rowspan=2, sticky=(N,S,E,W), padx=(19,9), pady=(20,10))
    self.color3.grid(column=3, row=4, rowspan=2, padx=(10,0), pady=(10,0))
    self.color3lbl.grid(column=3, row=4, rowspan=2, sticky=(N,S,E,W), padx=(19,9), pady=(20,10))
    self.color4.grid(column=2, row=4, rowspan=2, padx=(10,0), pady=(10,0))
    self.color4lbl.grid(column=2, row=4, rowspan=2, sticky=(N,S,E,W), padx=(19,9), pady=(20,10))

    def armony_changed(armonies, options):
      s.configure('My1.TFrame', background="#"+armonies[options[self.armoniacbx.get()]][0])
      self.color1['style'] = 'My1.TFrame'
      self.color1hex.set("#" + armonies[options[self.armoniacbx.get()]][0])
      s.configure('My2.TFrame', background="#"+armonies[options[self.armoniacbx.get()]][1])
      self.color2['style'] = 'My2.TFrame'
      self.color2hex.set("#" + armonies[options[self.armoniacbx.get()]][1])
      s.configure('My3.TFrame', background="#"+armonies[options[self.armoniacbx.get()]][3])
      self.color3['style'] = 'My3.TFrame'
      self.color3hex.set("#" + armonies[options[self.armoniacbx.get()]][3])
      s.configure('My4.TFrame', background="#"+armonies[options[self.armoniacbx.get()]][4])
      self.color4['style'] = 'My4.TFrame'
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
              listFeels.append(sinonimo["sinonimo"].lower())
          else:
            print(response.status_code)
      
    print(listFeels)
    listFeels = list(set(map(lambda var: re.sub(" ","_",var.lower()),listFeels)))
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
    {"feel": "felicidad,amor", "age": "1-18", "category": ""},
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