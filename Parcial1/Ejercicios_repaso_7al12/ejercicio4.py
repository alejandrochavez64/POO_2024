"""  
  Crear un script que tenga 4 variables, una lista, una cadena, un entero y un logico,  
  y que imprima un mensaje de acuerdo al tipo de dato de cada variable. Usar funciones


"""

def declaracionVariables():
  global lista, cadena, entero, logico
  lista=[20,34.56,10]
  cadena="dagoberto.fiscal@utd.com"
  entero=100
  logico=True

def variableLista(lista):
  print(f"Los valores de la variable lista son: {lista} y es de tipo: {type(lista)}")

def variableCadena(cadena):  
  print(f"Los valores de la variable cadena es: {cadena} y es de tipo: {type(cadena)}")

def variableEntero(entero):
  print(f"Los valores de la variable entero es: {entero} y es de tipo: {type(entero)}")

def variableLogica(logico):
  print(f"Los valores de la variable logico es: {logico} y es de tipo: {type(logico)}")


#declaracionVariables()
lista=[20,34.56,10]
cadena="dagoberto.fiscal@utd.com"
entero=100
logico=True

variableLista(lista)
variableCadena(cadena)
variableEntero(entero)
variableLogica(logico)

