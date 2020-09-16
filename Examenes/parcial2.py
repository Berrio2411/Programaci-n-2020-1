listaPesos = [20000,30000,4000,2500,1000,7600]
#Preguntas
preguntaMenu='''
Por favor ingrese una de estas opciones :
            1-Convertir Pesos 
            2-Agregar nuevo valor a la lista
            3-Ver máximo ,minimo y promedio de ingrresos
            4-Retirar valor de la lista
            5-Salir del programa
:'''
preguntaconverionpesos='''
Por favor ingrese una de estas opciones :
            C-Convertir a pesos colombianos
            D-Convertir a dolares
            E-Convertir a euros 
:'''
#---Mensajes Error---# 
mensajeEntradaNoValidaN = 'Recuerde ingresar una opción válida 1,2,3,4,5'
mensajeConversionNovalida ='Recuerde ingresar una opcion valida C,D,E'
#---Mensajes Informativos---#
mensajeOpcion = 'Usted escogio la opción {}'
mensajeSalida = 'Gracias por usar el programa'
mensajePesos='No es necesaria la conversion ,igual se muestran los valores'
mensajeAgregar='Ingrese el valor que quiera agregar a la lista : '
mensajeQuitar='retira el elemento que quieras de la lista poniendo su posición ,ingresando 0 como primera posicion en la lista : '


#---Inicio codigo---#
opcion=int(input(preguntaMenu))

#---Calculos preliminares---#
listaDolares=[]
listaEuros=[]

#---Convertir de pesos a dolares---#
for elemento in listaPesos:
    dolares =elemento*0.00027
    listaDolares.append(dolares)

#---Convertir de pesos a euros---#
for elemento in listaPesos:
    euro=elemento*0.00023
    listaEuros.append(euro)

#---Máximos y minimos---#
mayor =  max (listaPesos)
menor =  min (listaPesos)
acumulado=0
for elemento in listaPesos:
    acumulado += elemento
    promedio= acumulado/len(listaPesos)

promedioPesos=round(promedio,2)

#----Menú---#
while(opcion!=5):
    if(opcion==1):
        print(mensajeOpcion.format(1))
        conversion= input(preguntaconverionpesos)
        if(conversion=='C'):
            print(mensajePesos)
            print(listaPesos)
        elif(conversion=='D'):
        
            print(listaDolares)
        elif(conversion=='E'):
            print(listaEuros)
        else:
            print(mensajeConversionNovalida)
    elif(opcion==2):
        print(mensajeOpcion.format(2))
        agregar=float(input(mensajeAgregar))
        listaPesos.append(agregar)
        print(listaPesos)
    elif(opcion==3):
        print(mensajeOpcion.format(3))
        print('El ingreso máximo fue',mayor)
        print('El ingreso minimo fue',menor)
        print('El ingreso promedio fue',promedioPesos)
    elif(opcion==4):
        print(mensajeOpcion.format(4))
        print(listaPesos)
        retirar=int(input(mensajeQuitar))
        listaPesos.pop(retirar)
        print(listaPesos)
    else:
        print(mensajeEntradaNoValidaN)

    #Variable
    
    opcion=int(input(preguntaMenu))

#Despedida
print(mensajeSalida)












