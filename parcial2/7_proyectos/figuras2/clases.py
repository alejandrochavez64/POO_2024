#Clase Principal 
class Figuras:
    def calcularArea(self):
        return self.area
  
#Clases Scuendiarias
#Rectangulo

class Rectangulos(Figuras):
    def __init__(self,largo,ancho):
        self._largo=largo
        self._ancho=ancho
    
    def calcularArea(self,largo,ancho):
        area=largo*ancho
        return area 

    #Resto de los metodos set y get 
    def getLargo(self):
        return self._largo

    def getAncho(self):
        return self._ancho

    def setLargo(self,largo):
        self._largo=largo

    def setAncho(self,ancho):
        self._ancho=ancho    

   

class Circulo(Figuras):
    def __init__(self,radio):
        self._radio=radio
    
    def calcularArea(self,radio):
        area=3.1416*radio*radio
        return area 

    #Resto de los metodos set y get 

    def getRadio(self):
        return self._radio

    def setRadio(self,radio):
        self._radio=radio


