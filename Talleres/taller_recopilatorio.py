#Datos inciales
listaDolares = [20000,30000,4000,2500,1000,7600]

#Preguntas
preguntaMenu='''
Por favor ingrese una de estas opciones :
            1-Convertir Dolares
            2-Mostrar categoria de ingresos
            3-Ver máximo ,minimo y promedio de ingrresos
            4-Salir del programa
:'''
preguntaconverionDolares='''
Por favor ingrese una de estas opciones :
            C-Convertir a pesos colombianos
            D-Convertir a dolares
            E-Convertir a euros 
:'''
#---Mensajes Error---# 
mensajeEntradaNoValidaN = 'Recuerde ingresar una opción válida 1,2,3,4'
mensajeConversionNovalida ='Recuerde ingresar una opcion valida C,D,E'

#---Mensajes Informativos---#
mensajeOpcion = 'Usted escogio la opción {}'
mensajeSalida = 'Gracias por usar el programa'
mensajeDolares='No es necesaria la conversion ,igual se muestran los valores'

#---Inicio codigo---#
opcion=int(input(preguntaMenu))

#---Calculos preliminares---#
listaPesos=[]
listaEuros=[]
listaClasificacion=[]

#---Convertir de dolares a pesos = COP 3700---#
for elemento in listaDolares:
    pesos=elemento*3700
    listaPesos.append(pesos)

#---Convertir de dolares a euros= COP 0,84---#
for elemento in listaDolares:
    euro=elemento *0,84
    listaEuros.append(euro)

#---Estados de la cuenta---#
for elemento in listaDolares:
    clasificacion=''
    if (elemento<1000):
        clasificacion='ingresos bajos'
    elif(elemento>= 1000 and elemento <7000):
        clasificacion='ingresos medios'
    elif(elemento>=7000 and elemento<20000):
        clasificacion='ingresos altos'
    else:
        clasificacion='Ingresos elevados'
    listaClasificacion.append(clasificacion)

#---Máximos y minimos---#
mayor =  max (listaDolares)
menor =  min (listaDolares)
acumulado=0
for elemento in listaDolares:
    acumulado += elemento
    promedio= acumulado/len(listaDolares)

promedioDolares=round(promedio,2)

#Menu
while(opcion!=4):
    if(opcion==1):
        print(mensajeOpcion.format(1))
        conversion= input(preguntaconverionDolares)
        if(conversion=='C'):
            print(listaPesos)
        elif(conversion=='D'):
            print(mensajeDolares)
            print(listaDolares)
        elif(conversion=='E'):
            print(listaEuros)
        else:
            print(mensajeConversionNovalida)
    elif(opcion==2):
        print(mensajeOpcion.format(2))
        print(listaClasificacion)
    elif(opcion==3):
        print(mensajeOpcion.format(3))
        print('El ingreso máximo fue',mayor)
        print('El ingreso minimo fue',menor)
        print('El ingreso promedio fue',promedioDolares)
    else:
        print(mensajeEntradaNoValidaN)


    #Variable opción1
    
    opcion=int(input(preguntaMenu))






#Despedida
print(mensajeSalida)








