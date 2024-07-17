"""  
 Escribir un programa  que añada valores a una lista mientras que su longitud 
 sea menor a 120, y luego mostrar la lista: Usar un while y for

"""

lista=[]

i=1
while i<=120:
   valor=int(input(f"Valor {i}: "))
   lista.append(valor)
   i+=1 

print(lista)  


for i in range(1,121):
   valor=int(input(f"Valor {i}: "))
   lista.append(valor)
   i+=1 

print(lista)    