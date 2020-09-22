# Dada una lista muéstrela en pantalla elemento a elemento.
def mostrarLista (lista):
    for elemento in lista:
        print(elemento)

numeros=[1,2,3,4,5,6,7,8]
letras=["a","b","c","d","e","f","g","h"]
mostrarLista(letras)
mostrarLista(numeros)

# Dada una lista de números enteros muestre en pantalla el número más grande, 
# el más pequeño y el promedio de la lista
def infoList(lista):
  mayor = max (lista)
  menor = min (lista)
  acumulador = 0
  for elemento in lista :
    acumulador += elemento
  sizeList =   len (lista)
  promedio = acumulador / sizeList
  print (f'el número mayor en la lista es el {mayor}, el menor {menor} y el promedio {promedio}')
edades = [23,22,12,21,17,25,22,18]
infoList(edades)

#Salude n veces
def saludar (cantidad=0):
    print("hola " *cantidad)
saludar(8)

#Que devuelva todos los números pares de una lista de números enteros
def paresLista(lista):
  pares = []
  for elemento in lista:
    if elemento % 2 == 0 :
      pares.append (elemento)
  return pares

edades = [23,22,12,56,17,43,66,13]
edadesPares = paresLista(edades)
print (edadesPares)

#Que devuelva únicamente los elementos mayores a 24
def mayoresLista(lista):
  mayores = []
  for elemento in lista:
    if elemento > 24 :
      mayores.append (elemento)
  return mayores
edades = [15,42,34,12,18,9,25,71]
edadesMayores = mayoresLista(edades)
print (edadesMayores)

numerosss=[34,23,25,27,34,16,37,11,13]
numerosMayores= mayoresLista(numerosss)
print(numerosMayores)

#Se sabe que el IMC se calcula dividiendo el peso por la altura al cuadrado, 
#realice una función que lo calcule.
def calcularIMC (peso, altura):
  return peso /(altura**2)
imc = calcularIMC(65, 1.78)
print (imc) 

# Crea un función que sirva para despedirte del que esta ejecutando el código
def chao():
  print ("Muchas gracias por venir,fue un placer tenerte por aca!!")
chao()