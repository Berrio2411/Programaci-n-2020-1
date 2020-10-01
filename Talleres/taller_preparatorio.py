# Dada una lista de número mostrar en pantalla el mayor número, el menor y el promedio de la lista
def infoLista(lista):
    mayor = max (lista)
    menor = min (lista)
    acumulador = 0
    for elemento in lista :
        acumulador += elemento
    sizeList =   len (lista)
    promedio = acumulador / sizeList
    print (f'el número mayor en la lista es el {mayor}, el menor {menor} y el promedio {promedio}')
numeros = [5,8,12,16,25,23,8,11,10]
infoLista(numeros) 

# Dada una lista números, devuelva únicamente los números pares
def paresLista(lista):
    pares = []
    for elemento in lista:
        if elemento % 2 == 0 :
            pares.append (elemento)
    return pares

edades = [23,22,12,56,17,43,66,13]
edadesPares = paresLista(edades)
print (edadesPares)

#Dado un mensaje mostrarlo en pantalla
def mensaje ():
    print('Hola,epero te encuentres muy bien')
mensaje()

#Dado un número le reste 12 y devuelva el resultado
def restaNumero(numero1):
    return numero1-12
resta=restaNumero(35)
print(resta)

# Dado un número lo sume 12 y devuelva el resultado
def sumaNumero(numero1):
    return numero1+12
suma=sumaNumero(40)
print(suma)

#Dado un número lo divide por 12 y devuelva el resultado
def divisionNumero(numero1):
    return numero1/12
division=divisionNumero(36)
print(division)

#Dado un número lo multiplique por 12 y devuelva el resultado
def multiplicacionNumero(numero1):
    return numero1*12
multiplicacion=multiplicacionNumero(4)
print(multiplicacion)

# Dada una de las 4 funciones anteriores y su entrada mostrar en pantalla el resultado
def mostrarResultado(sumaNumero,numero1):
    resultado=sumaNumero(numero1)
    print(f'la suma de los numeros es {resultado}')
mostrarResultado(sumaNumero,35)








