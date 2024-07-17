#10.- Crear un programa que solicite la calificacion de 15 alumnos e imprimir en pantalla cuantos aproboron y cuantos no aprobaron

aprobaron=0
noaprobaron=0
for i in range(1,16):
   calificacion=int(input("Ingresa la calificacion "))
   if calificacion>=80:
     aprobaron+=1
   else:
     noaprobaron+=1   

print(f"El # de alumnos que aprobaron son: {aprobaron} y el # de alumnos no aprobados son: {noaprobaron}")     