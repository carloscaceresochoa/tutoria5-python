def save(*args):
    '''funcion para realizar un consulta en base de datos'''
    tam=len(args)
    consulta="insert into "+args[0]+" values("
    for i in range(0,tam):
        if(type(args[i])==int or type(args[i])==float):
            consulta+=str(args[i])+","
        else:
           consulta+="'"+args[i]+"',"
    consulta=list(consulta)
    tamc=len(consulta)
    consulta[tamc-1]=')'
    consulta=''.join([str(elem) for elem in consulta])
    print(consulta)

save("empleado","1234","pedro","perez",4,"m",4.2)
    