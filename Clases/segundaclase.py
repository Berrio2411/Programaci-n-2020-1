nombre= input("Por favor ingrese su nombre :  ")
edad= int (input("por favor ingrese su edad : "))
estatura= float(input("Por favor ingree su estatura : "))

print("hola", nombre, "eres bienvenido a este codigo")
print(edad)
print(estatura)

print(type(nombre))
print(type(edad))
print(type(estatura))

if(edad >= 18) :
    print ("usted es mayor de edad")
    print ("ya eres todo un adulto")
