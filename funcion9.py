def computoasignatura(*args,**kwargs):
    '''la funcion parametros indeterminados
        recibe por posicion y parametro'''
    total=0
    for k in kwargs:
        print(kwargs[k])
    for arg in args:
        total+=arg
    definitiva=total/3
    print("definitiva ","{0:.2f}".format(definitiva))

computoasignatura(3.2,2.0,4.0,nombre="juan",apellido="perez",asignatura="modulo python")    
    