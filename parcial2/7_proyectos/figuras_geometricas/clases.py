
#Clase Principal y Abstracta 
class Figuras:
    def __init__(self,x,y,visible):
       self.x=x
       self.y=y
       self.visible=visible 

    def estaVisible(self):
        return self.visible

    def mostrar(self):
        print (f"La figura se esta mostrando")

    def ocultar(self):
        print (f"La figura se esta ocultando")

    def mover(self,x,y):
        print(f"La fugura se mueve en la siguiente coordenada: {self.getX(),self.getY()}")

    def calcularArea(self):
        return self.calcularArea

    #Metodos de gettes y Setters faltantes

    def setX(self,x):
        self.x=x

    def setY(self,y):
        self.y=y

    def getX(self):
       return self.x

    def getY(self):
        return self.y     

  
#Clases Scuendiarias
#Rectangulo

class Rectangulos(Figuras):
    def __init__(self,x,y,visible,alto,ancho):
        super().__init__(x,y,visible)
        self.__alto=alto
        self.__ancho=ancho

    def mostrar(self):
        print(f"El Rectangulo se encuentra visible: {self.estaVisible()} y se esta localizado en coordenada X,Y {self.getX(),self.getY()}, ademas tiene un alto y ancho de: {self.getAlto(), self.getAncho()} ")    

    def ocultar(self):
        print(f"El Rectangulo se esta ocultando")    
    
    def calcularArea(self,alto,ancho):
        area=alto*ancho
        return area 

    #Resto de los metodos set y get 
    def getAlto(self):
        return self.__alto

    def getAncho(self):
        return self.__ancho

    def setAlto(self,alto):
        self.__alto=alto

    def setAncho(self,ancho):
        self.__ancho=ancho    

   


class Circulos(Figuras):
    def __init__(self,x,y,visible,radio):
        super().__init__(x,y,visible)
        self.__radio=radio

    def mostrar(self):
        print(f"El Circulo se encuentra visible: {self.estaVisible()} y se esta localizado en coordenada X,Y {self.getX(),self.getY()}, ademas tiene un radio de: {self.getRadio()} ")     

    def ocultar(self):
        print(f"El Circulo se esta ocultando")    

    def calcularArea(self,radio):
        area=3.1416*radio*radio
        return area 

    #Resto de los metodos set y get 
    def getRadio(self):
        return self.__radio     
    
    def setRadio(self,radio):
        self.__radio=radio

