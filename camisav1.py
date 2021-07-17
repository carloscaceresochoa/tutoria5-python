#clase Camisa
class Camisa:
    #atributos
    talla=""
    precio=""
    color=""
    marca=""
    
    #metodos

    def mostrar(self):
        print("datos camisa")
        print("Talla",self.talla)
        print("precio",self.precio)
        print("color",self.color) 
        print("marca",self.marca)
    
    def descuentocamisa(self,descuento):
        self.precio=self.precio-((descuento/100)*self.precio)


camisa=Camisa()  
camisa.talla="L"
camisa.precio=70000
camisa.color="Blanco"
camisa.marca="Arturo Calle"
camisa.descuentocamisa(30)
camisa.mostrar()