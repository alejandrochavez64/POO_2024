#7.- Hacer un programa que muestre todos los numeros impares entre 2 numeros que decida el usuario

n1=int(input("Numero #1: "))
n2=int(input("Numero #2: "))

if n1<n2:
  for i in range(n1,n2+1):
   impar=i%2
   if impar==1:
     print(f"Numero impar: {i}")
else:
 print("El numero 2 debe ser mayor el el numero 1")    