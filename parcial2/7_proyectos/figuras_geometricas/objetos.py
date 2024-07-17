from clases import *


#Instancias los objetos correspondientes
#1.- Crear un primer objeto de la clase Rectangulos que se llame: "rectangulo1", en el cual se introduzca la siguiente información: x=3,y=4, visible=True, ancho y alto 10 y 20 respectivamente. 

rectangulo1=Rectangulos(3,4,True,10,20)
rectangulo1.mostrar()
print(f"El area del rectangulo es: {rectangulo1.calcularArea(rectangulo1.getAlto(),rectangulo1.getAncho())}")

# #3.- Crear otro objeto de la clase Circulos que se llame: "circulos1", en el cual se introduzca la siguiente información: x=3,y=3, visible=True y radio de 6. 

circulo1=Circulos(3,3,True,6)
circulo1.mostrar()
print(f"El area del circulo es: {circulo1.calcularArea(circulo1.getRadio())}")