'''funcion argumentos por nombre'''
def suma(n1=None,n2=None):
    '''funcion para realizar la suma'''
    if(n1==None or n2==None):
       return "Argumento Vacio"
    else:    
        return n1+n2


print(suma(1,2))