"""
 Crear un programa para comprobar si una lista esta vacia y si esta vacia llenarla con 
 palabras o frases hasta que el usuario asi lo crea conveniente, posteriormente imprimir 
 el contenido de la lista en mayusculas

"""
frases=[]

if len(frases)<=0:
 opcion="SI"   
 while opcion=="SI":
   texto=input(f"Frase {i}: ").upper()
   frases.append(texto)
   opcion=input("¿Deseas introducir otra frase?").upper()
   i+=1
 
print(frases)







