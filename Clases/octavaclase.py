import random

numeroAletorio =  random.randint(1,6)
print(numeroAletorio) 

preguntaNumero = "Que número crees que salió : "
numeroCorrecto = numeroAletorio
numeroIgresado= int(input(preguntaNumero))
errores=0 

#Mensajes
mensajeFallido="Fallaste,no es el número secreto"
mensajeAcertado="Felicitaciones,adivinisate el número"
mensajeerror="Ten cuidado te equivocaste,van {} errores "

while(numeroIgresado!= numeroCorrecto):
    errores=errores+1
    print(mensajeerror.format(errores,1+errores))
    print(mensajeFallido)
    numeroIgresado=int(input(preguntaNumero)) 
print(mensajeAcertado) 


#----se crea lista de alimentos favoritos---
listaAlimentos=[]
listaAlimentos=["Comida arabe","Frijoles","Pizza","Ajiaco","Mote de queso"]
print("hola,bienvenido a mi lista de alimentos favoritos")
sizeList= len(listaAlimentos)

for i in range(sizeList):
        print(f"estos son unos de ellos: {listaAlimentos[i]}")

print(f"Pero mi favorita sin duda es {listaAlimentos[2]}:")






