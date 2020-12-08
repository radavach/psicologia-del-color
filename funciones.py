from pyswip import *
import re

prolog = Prolog()
prolog.consult("proyecto.pl")

### Convierte la lista que se obtiene al realizar la query en una lista normal ###
### Recibe: [Atom('441605'), Atom('443781')] Regresa: ['primario','frio']
def convertList(lista):
  return list(map(lambda var: re.sub('b\'|\'', '', str(var)), lista))

### Regresa una lista de las categorias registradas para los colores ###
### Ej: ['primario','secundario','neutral']
def cargarCategorias():
  categorias = list(prolog.query("findall(Categoria, categoria_color(Categoria,_), Categorias)"))[0]["Categorias"]
  return convertList(categorias)

### Regresa una lista de los colores registrados con armonias disponibles ###
### Ej: ['rojo','azul,'naranja'] ###
def cargarColoresArmonia():
  colores = list(prolog.query("setof(Color, A^B^armonia(Color,A,B), Colores)"))[0]["Colores"]
  return convertList(colores)

### Regresa una lista de los colores registrados con caracteristicas positivas ###
### Ej: ['negro','marron,'plata'] ###
def cargarColoresPositivos():
  colores = list(prolog.query("findall(Color, sentimientos_positivos(_,Color), Colores)"))[0]["Colores"]
  return convertList(colores)

### Regresa una lista de los colores registrados con caracteristicas negativas ###
### Ej: ['azul','rojo,'amarillo'] ###
def cargarColoresNegativos():
  colores = list(prolog.query("findall(Color, sentimientos_negativos(_,Color), Colores)"))[0]["Colores"]
  return convertList(colores)

### Recibe una categoria y regresa una lista con los colores asociados a esta categoria ###
### Ej: 'primario' => ['azul','rojo,'amarillo'] ###
def obtenerColoresPorCategoria(CATEGORIA):
  colores = list(prolog.query("categoria_color("+CATEGORIA+",Colores)"))[0]["Colores"]
  return convertList(colores)

#############################################################################################################
#############################################################################################################

### Recibe un color y regresa los sentimientos negativos asociados al color ###
### Ej: 'rojo' => ['tension','desafio,'impacto','agresividad'] ###
def sentimientosNegativos(COLOR):
  sentimientos = list(prolog.query("sentimientos_negativos(Sentimientos,"+COLOR+")"))[0]["Sentimientos"]
  return convertList(sentimientos)

### Recibe un color y regresa los sentimientos positivos asociados al color ###
### Ej: 'rojo' => ['masulinidad','vitalidad,'exitacion','atrevimiento'] ###
def sentimientosPositivos(COLOR):
  sentimientos = list(prolog.query("sentimientos_positivos(Sentimientos,"+COLOR+")"))[0]["Sentimientos"]
  return convertList(sentimientos)
    
### Recibe una color y regresa los un diccionario con caracteristicas asociados al color ###
### Ej: 'rojo' => {categorias:['primario','calido'], edades:['1-18','19-24','25-35','51-69']} ###
def caracteristicasColor(COLOR):
  resultado = {}

  categorias = list(prolog.query("""
      findall(
        Categoria,
        (categoria_color(Categoria,Colores),
        member("""+COLOR+""",Colores)),Categorias
      )"""))[0]["Categorias"]

  edades = list(prolog.query("""
      findall(
        Edad, 
        (color_fav_publico(Categoria,Colores),member("""+COLOR+""",Colores),publico_objetivo(Edad,Categoria)),
        Edades
      )"""))[0]["Edades"]

  resultado["categorias"] = convertList(categorias)
  resultado["edades"] = convertList(edades)
  
  return resultado

### Recibe una color y regresa un diccionario con la armonia de color y respectivos codigos en hexadecimal ###
### Ej: 'rojo' => {analogo:['FF530D', 'E82C0C', 'FF0000', 'E80C7A', 'FF0DFF'], monocromatico:['800000', 'FF4D4D', 'FF0000', '802626', 'CC0000']} ###
def armoniaColor(COLOR):
  armonias = list(prolog.query("findall([Categoria, Colores], (armonia("+COLOR+",Colores,Categoria)),Armonias)"))[0]["Armonias"]
  resultado = {}

  for armonia in armonias:
    resultado[str(armonia[0])] = convertList(armonia[1])

  return resultado