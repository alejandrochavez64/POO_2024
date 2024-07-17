"""

   Existe una estructura de condicion llama "if" 
   la cual evalua una condicion para encontrar el valor "True" y si se cumple
   la condicion se ejecuta la linea o lineas codigo 

   Tenes 4 variantes del if

   1.- if simple
   2.- if compuesto
   3.- if anidado
   4.- if y elif
   
"""

#Ejemplo 1 if simple

# color=input("Ingresa un color: ")

# if color=="rojo":
#     print("Soy el color rojo")

#Ejemplo 2 if compuesto

# color=input("Ingresa un color: ")

# if color=="rojo":
#     print("Soy el color rojo")
# else:
#     print("No soy el color rojo soy otra cosa")    


#Ejemplo 3 if anidado

# color=input("Ingresa un color: ")

# if color=="rojo":
#     print("Soy el color rojo")
#     if color!="rojo":
#       print("No Soy el color rojo")
# else:
#     print("No soy el color rojo soy otra cosa")    



#Ejemplo 4 if y elif

color=input("Ingresa un color: ")

if color=="rojo":
    print("Soy el color rojo")
elif color=="amarillo":
    print("Soy el color amarillo")
elif color=="azul":
    print("Soy el color azul")
elif color=="morado":
    print("Soy el color morado")    
else:
   print("No soy ningun de los anteriores")    


#Ejemplo 4 Crear un programa que solicite el numero de la semana 
# e imprima en pantalla el dia que le corresponde 

dia=int(input("Ingresa un dia de la semana: "))

if dia==1:
   print("Soy Domingo")
elif dia==2:
   print("Soy Lunes")
elif dia==3:
   print("Soy Martes")
elif dia==4:
   print("Soy Miercoles")
elif dia==5:
   print("Soy Jueves")
elif dia==6:
   print("Soy Viernes")    
elif dia==7:
   print("Soy Sabado")
else:
   print("No correspondo o ningun dia de la semana")   








