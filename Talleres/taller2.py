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
preguntaNumeroA = "Ingrese un número entero por favor : "
preguntaNumeroB = "Ingrese un número mayor al ultimo ingresado : "
mensajeInformacion = "{} es mayor a {} por eso sigue el juego"
mensajeEntrada = "Ingresaste un numero mayor, solo acabaras cuando ingreses uno menor al ultimo numero ingresado"

primerNumero =  int (input (preguntaNumeroA))
segundoNumero =  int (input (preguntaNumeroB))

while (segundoNumero > primerNumero) :
  print (mensajeInformacion.format (segundoNumero, primerNumero))
  primerNumero = segundoNumero
  print (mensajeEntrada)
  segundoNumero =  int (input (preguntaNumeroB))


#Ejercicio4
total=0
monto=float(input("Monto de una venta: $"))
while monto!=0:
    if monto<0:
        print("Monto no válido.")
    else:
        total+=monto
    monto=float(input("Monto de una venta: $"))
if total>1000:
    total-=total*0.1
print("Monto total a pagar: $", total) 





