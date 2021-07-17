#clase Camisa atributos privado encapsulacion
class Camisa:
    #atributos
    __talla=""
    __precio=""
    __color=""
    __marca=""
    
    #constructor
    
    def __init__(self,talla,precio,color,marca):
        self.color=color
        self.__talla=talla
        self.__precio=precio
        self.__color=color
        self.__marca=marca
        
        
    
    #metodos

    def mostrar(self):
        print("datos camisa")
        print("Talla",self.__talla)
        print("precio",self.__precio)
        print("color",self.__color) 
        print("marca",self.__marca)
    
    def descuentocamisa(self,descuento):
        self.__precio=self.__precio-((descuento/100)*self.__precio)


camisa=Camisa("L",70000,"Blanco","Arturo Calle")  
camisa.descuentocamisa(30)
camisa.mostrar()