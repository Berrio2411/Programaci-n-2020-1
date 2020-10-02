#Dada un de número devolver el número elevado al cuadrado.
def elevarCuadrado (numero1):
    return numero1**2
cuadrado= elevarCuadrado(5)
print(cuadrado)

#Dada un de número devolver el número elevado a la tres.
def elevarCubo (numero1):
    return numero1**3
cubo=elevarCubo(2)
print(cubo)

#Dada un de número devolver el número elevado a la cuatro.
def elevarCuatro(numero1):
    return numero1**4
cuarta=elevarCuatro(6)
print(cuarta)

#Dada un de número devolver el número elevado a la cinco
def elevarCinco (numero1):
    return numero1**5
quinta=elevarCinco(4)
print(quinta)

#Crear una función que dada una de las funciones anteriores y sus entradas muestre en pantalla el resultado de las mismas
#elevado 4
def mostrarResultado (operación,numero1):
    resultado=(operación(numero1))
    print(f'el numero elavado a {operación} es {resultado}')
mostrarResultado(elevarCuatro,5)
mostrarResultado(elevarCuadrado,4)
mostrarResultado(elevarCubo,4)
mostrarResultado(elevarCinco,5)


