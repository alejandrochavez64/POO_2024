#5.- Hacer un programa que muestre todos los numeros entre 2 numeros que diga el usuario

n1=int(input("Numero #1: "))
n2=int(input("Numero #2: "))

if n1<n2:
 for i in range(n1,n2+1):
  print(f"El siguiente numero es: {i}")
else:
  print("El numero 2 debe ser mayor el el numero 1")    

