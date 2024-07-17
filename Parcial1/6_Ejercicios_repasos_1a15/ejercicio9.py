#9.- Hacer un programa que solicite numeros indefinidamente hasta que se introduzca el 111 y salir del programa

numero=int(input("Solicitar un numero: "))

while numero!=111:
    print(f"El numero ingresado es: {numero}")
    numero=int(input("Solicitar un numero: "))
    
    if numero==111:
       print("Listo terminaste") 
       break
    
    


