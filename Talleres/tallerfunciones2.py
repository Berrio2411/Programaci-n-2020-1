#Dados 2 numeros crear una función que devuelva quien es mayor o si son iguales


def infoNumero (numero1,numero2):
    if(numero1>numero2):
        print(f'el numero {numero1} es mayor que el numero {numero2}')
    elif(numero2>numero1):
        print(f'el numero {numero2} es mayor que el numero {numero1}')
    else:
        print(f'los numeros son iguales')

infoNumero(3,5)

#Dada una lista de nombres cree una función que muestre en pantalla nombre por nombre
def mostrarLista (lista):
    for elemento in lista:
        print(elemento)

nombres=['Santiago','Isabella','Carmen','Hector','Mario','Duvan']
mostrarLista(nombres)

#Crear una funcion que devuelva el IMC
def calcularIMC (peso, altura):
    return peso /(altura**2)
imc = calcularIMC(65,1.78)
print (imc) 

# Dada la funcion IMC y los valores de peso y altura mostrar en pantalla el IMC calculado
def mostarIMC (calcularIMC,peso,altura):
    imc2= calcularIMC(peso,altura)
    print(f'El IMC calculado es de {imc2}')
mostarIMC(calcularIMC,65,1.78)


