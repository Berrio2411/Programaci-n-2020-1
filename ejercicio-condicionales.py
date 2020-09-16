#------Preguntas------#
preguntaNumeroA = 'Ingrese el número entero A : '
preguntaNumeroB = 'Ingrese el número  entero b : '
#-------Mensajes-----#
mensajeMayor = 'El numero {} es mayor que el numero {} pues {} > {}'
mensajeIguales = 'El numero {} es iguales que el numero {} pues {} == {}'
#-------Entradas-----#
numeroA = int (input (preguntaNumeroA))
numeroB = int (input (preguntaNumeroB))
#-------Condicionales-----#
if (numeroA > numeroB) :
    print (mensajeMayor.format('A','B',numeroA, numeroB)) 
elif (numeroB > numeroA) :
    print (mensajeMayor.format('B','A',numeroB, numeroA)) 
else :
    print (mensajeIguales.format('A','B',numeroA, numeroB))

#Ejercicio 2
#------Preguntas------#
preguntaEdad = 'Ingrese por favor su edad: '
#-------Mensajes-----#
mensajeClasificacion = 'Usted es un {}'
#-------Entradas-----#
edad = int (input(preguntaEdad))
#-------Condicionales-----#
if (edad< 18) :
    print (mensajeClasificacion.format('menor de edad')) 
elif (edad >= 18 and edad <26) :
    print (mensajeClasificacion.format('Joven'))  
elif (edad >= 26 and edad <61) :
    print (mensajeClasificacion.format('Adulto'))  
else :
    print (mensajeClasificacion.format('Adulto Mayor')) 

#Ejercicio 3 

