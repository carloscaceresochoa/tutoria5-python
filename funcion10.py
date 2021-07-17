def operacion(n1=None):
    if(n1==None):
        print("Parametro Vacio")
    else:
        cuadrado=n1**2
        raizc=n1**0.5
        return cuadrado,raizc
    
n=int(input("digite el numero"))
op=operacion(n)
for r in op:
    print(r)

print(n," elevado a las 2 ",op[0])
print(n," raiz de 2 ",op[1])

    
