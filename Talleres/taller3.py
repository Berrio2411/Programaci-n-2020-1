#ENTRADAS
Temperatura_Corporal = [36,37,38,35,36,38,37.5,38.2,41,37.4,38.6,39.1,40.3,33]

#PREGUNTAS 
preguntasMenu = '''
            1-Convertir temperaturas
            2- Estado de salud
            3- Información máximo y minimo de temperaturas 
            4-Salir del programa
:'''
prenguntaConversiontemperatura = '''
Por favor ingrese una de las segundas opciones:
            F-Convertir a farenheit
            K-Convertir a Kelvin
            C-Convertir temperaturas a C
:'''

#MENSAJES ERROR
mensajeEntradanovalidaN= "Debes ingresar una opción de 1,2,3,4"
mensajeEntradanovalidaT= "Debes ingresar una opción de F,C,K"

#MESAJES INFORMATIVOS
mensajeSalida="Gracias por usar esta aplicacion"
mensajeOpcion=" Usted escogio la opción {}"
mensajeCelsius="No es necesaria la conversión"

#Inicio codigo
opcion= int(input(preguntasMenu) )
#Calculos preliminares
listaKelvin=[]
listaFa=[]
listaC=Temperatura_Corporal
listaEstadosSalud=[]
#----Pasando a Kelvin x C+273.15----
for elemento in listaC:
    Kelvin= elemento + 273.15
    listaKelvin.append(Kelvin)

#----Pasando a FA= x (C*18)+32----
for elemento in listaC:
    farenheit= (elemento*1.8) +32
    listaFa.append(farenheit) 

#---Detectando estados salud---
for elemento in listaC:
    estado=''
    if (elemento<36):
        estado="hipotermia"
    elif(elemento>=36 and elemento<37.6):
        estado="Normal"
    else:
        estado="Fiebre"
        listaEstadosSalud.append(estado)

#----Calcular maximos y minimos
maximo= max(listaC)
minimo= min(listaC)
frecuencia= round(len(listaC))



#Menu 
while(opcion!=4):  
    if (opcion==1):
        print(mensajeOpcion.format(1))
        #Pregunta Conversión
        conversion=input(prenguntaConversiontemperatura)
        if (conversion=="K"):
            print(listaKelvin)
        elif(conversion=="F"):
            print(listaFa)
        elif(conversion=="C"):
            print(listaC)
            print(mensajeCelsius)
        else:
            print(mensajeEntradanovalidaT)
        
    elif (opcion==2):
        print(mensajeOpcion.format(2))
        print(listaEstadosSalud)
    elif (opcion==3):
        print(mensajeOpcion.format(3))
    else:
        print(mensajeEntradanovalidaN)











#Salida
print(mensajeSalida)





