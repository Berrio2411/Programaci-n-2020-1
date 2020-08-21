nombre= (input("por favor ingrese su nombre : "))
pais= (input("ingrese su pais  de procedencia con la  primera letra en mayuscula : "))


print ("hola",nombre,"eres bienvenido")
if (pais=="China" or pais=="Italia" or pais =="Iran"):
    print(f"el pasejero de nommbre {nombre} procedente de {pais} debe estar  bajo observación")

temperatura= float(input("ingrese su temperatura en C : "))

if (temperatura<36):
    print(f"el pasejero de nommbre {nombre} procedente de {pais} sufre de hipotermia")
elif(temperatura>=36 and temperatura<=38.4):
    print(f"el pasejero de nommbre {nombre} procedente de {pais} se encuentra en estado saludable")
elif(temperatura>=38.5 and temperatura<=40):
    print(f"el pasejero de nommbre {nombre} procedente de {pais} se encuentra en estado de alerta")
else:
    print(f"el pasejero de nommbre {nombre} procedente de {pais} se encuentra en estado de peligro")
