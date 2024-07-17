""" 
 Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 

 a.- Recorrer la lista y mostrarla
 b.- hacer una funcion que recorra la lista de numeros y devuelva un string
 c.- ordenarla y mostrarla
 d.- mostrar su longitud
 e.- buscar algun elemento que el usuario pida por teclado


"""
#Lista de 8 numeros enteros
numeros=[34,-56,23,67,20,10,12,34]

#1.- Recorrer la lista y mostrarla
def recorreLista():
   for i in numeros:
     print(f"{i}") 

#2.- hacer una funcion que recorra la lista de numeros y devuelva un string
def recorreListaString():
   valores="" 
   for i in numeros:
     i_str=str(i)
     valores=valores+","+i_str
   return valores   

#3.- ordenarla y mostrarla
def ordenarLista():
 numeros.sort()  
 

#4.- mostrar su longitud
def longitudLista():
   return len(numeros)


#5.- buscar algun elemento que el usuario pida por teclado
def numeroBuscar():
  num_buscar=int(input("Escribe el numero a buscar"))
  for i in numeros:
    if num_buscar==i:
     print(f"El numero a buscar es: {num_buscar} y si se encontro")
  

print(".::Menu de Opciones::.")
opcion=input("1.- Recorrer la lista y mostrarla \n 2.- Recorra la lista de numeros y devuelva un string \n 3.- Ordenarla y mostrarla \n 4.- Mostrar su longitud \n 5.-Buscar algun numero dentro de la lista \n ¿Que opción desea?  ")

if opcion=="1":
  recorreLista()
elif opcion=="2":
  print(recorreListaString())
elif opcion=="3":
  ordenarLista()
  print(numeros)
elif opcion=="4":
  print(f"La longitud de la lista es: {longitudLista()}")
elif opcion=="5":
  numeroBuscar()  
else:
  print("Opción invalida ... verifique")





