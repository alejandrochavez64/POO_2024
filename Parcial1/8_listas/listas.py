"""  

 List (Array)
 son colleciones o conjunto de datos/valores bajo 
 un mismo nombre, para acceder a los valores se
 hace con un indice numerico 

 Nota: sus valores si son modificables

 La lista es una colección ordenada y modificable. Permite miembros duplicados.


"""

#Ejemplo 1 Crear una lista con valores numericos enteros e imprimir la lista 

# numeros=[23,34]
# print(numeros)

# #Recorrer la lista con un for

# for i in numeros:
#     print(i)

# #Recorrer la lista con un while
# i=0
# while i<len(numeros):
#     print(numeros[i])
#     i+=1

#Ejemplo 2 Crear una lista de palabras, posteriormente ingresar una palabra para buscar la coincidencia en lista. E indicar si aparece la palabra y en que posicion en caso contrario indicar una sola vez si no la encontro

# palabras=["hola","2024","10.23","True"]
# print(palabras)

# palabra_buscar=input("Ingresa la palabra a buscar: ")

# noencontro=True
# for i in palabras:
#   if palabra_buscar==i:
#     print(f"Encontre la palabra {palabra_buscar}, en la posicion: {palabras.index(i)} ") 
#     noencontro=False

# i=0
# while i<len(palabras):
#    if palabra_buscar==palabras[i]:
#      print(f"Encontre la palabra {palabra_buscar}, en la posicion: {i} ")
#      noencontro=False
#    i+=1  
  
# if noencontro:
#   print(f"No se encontro la palabra dentro de la lista")    
      

#ejemplo 3 Lista multilinea o multidimensional (matriz) para crear una agenda telefonica

agenda=[
  ["Carlos",6181234567],
  ["Fernando",6182334567],
  ["Matias",6691112233],
  ["Juan Polainas",6182332345]
]

print(agenda)

for i in agenda:
  print(f"{agenda.index(i)+1}.-{i}")


#ejemplo 4 Crear un programa que permita Gestionar (Administrar) peliculas, colocar un menu de opciones para agregar, remover, consultar peliculas. 
#Notas: 
# 1.- Utilizar funciones y mandar llamar desde otro archivo
# 2.- Utilizar listas para almacenar los nombres de peliculas

def insertarPeliculas():
  pelicula=input("Ingrese la pelicula: ")
  peliculas.append(pelicula)
  espereTecla()

def eliminarPeliculas():
  pelicula=input("Ingrese la pelicula: ")
  peliculas.remove(pelicula)
  espereTecla()  


peliculas=[]

print("\n\t..::: CINEPOLIS CLON :::... \n 1.- Agregar  \n 2.- Eliminar \n 3.-Consultar \n 4.- SALIR ")
opcion=input("\t Elige una opción: ").upper()

if opcion=="1" or opcion=="AGREGAR":
  insertarPeliculas()
elif opcion=="2" or opcion=="ELIMINAR":
  eliminarPeliculas()  
