#Ciclos Whyle
preguntaNumero= "igrese un número del 1 al 10 : "



#Mensaje
mensajeFallido="Fallaste,no es el número secreto"
mensajeAcertado="Felicitaciones,adivinisate el número"
mensajeFinal="gracias por jugar"
mensajevida="Ten cuidado perdiste {} vidas ,te quedan {}"
mensajeDerrota= "has perdido"


numeroSecreto=6
vidasPerdidas=0
numeroIgresado= int(input(preguntaNumero))

while(numeroSecreto != numeroIgresado and vidasPerdidas<=2):
    vidasPerdidas=  vidasPerdidas+1
    print(mensajevida.format(vidasPerdidas,3-vidasPerdidas))
    print(mensajeFallido) 
    if vidasPerdidas<3:  
        numeroIgresado= int(input(preguntaNumero))
if vidasPerdidas<3:
    print(mensajeAcertado)
    print(mensajeFinal)

else:
    print(mensajeDerrota)
    print(mensajeFinal)


#Actividad vocales 
#Preguntas
preguntaVocal="ingrese una vocal en minuscula : "
vocalCorrecta="a"
vocalIngresada= (input(preguntaVocal))

#Mensajes
mensajeVocalcorrecta="Adivinaste la vocal"
mensajeVocalmala="No adivinaste la vocal"


while(vocalCorrecta != vocalIngresada): 
    print(mensajeVocalmala)
    vocalIngresada=(input(preguntaVocal))
print(mensajeVocalcorrecta)
print(mensajeFinal)




