#--Ejercicio1---
preguntaNumero="ingrese un numero entero o 0 para finalizar : "
numeroIngresado= int(input(preguntaNumero))
Suma= 0
while(numeroIngresado!=0):
    Suma+=numeroIngresado
    numeroIngresado=int(input(preguntaNumero))

print(Suma)

#--Ejercicio2--
preguntaNumeroX="Ingresa un numero entero por favor : "
preguntaNumeroY="Ingresa un numero entero mayor al primero : "
mensajeError="Recuerda que el segundo numero debe ser mayor a {}"

numeroX=int(input(preguntaNumeroX))
numeroY=int(input(preguntaNumeroY))
while(numeroX>numeroY):
    print(mensajeError.format(numeroX))
    numeroY=int(input(preguntaNumeroY))  

#--Ejericio3--





