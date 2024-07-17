# Escribir un programa que muestre los cuadrados 
#(un numero multiplicado por si mismo) de los 60 primeros 
#numeros naturales. Resolverlo con while y for
#

#Con While

contador=0

# while contador<=60:
#     cuadrado=contador*contador
#     print(f"El cuadrado de {contador} es {cuadrado}")
#     contador+=1


#Con for

for contador in range(61):
    cuadrado=contador*contador
    print(f"El cuadrado de {contador} es {cuadrado}")