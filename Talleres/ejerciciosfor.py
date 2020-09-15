#Ejercicio 1
sumatoria=0
for i in range(101):
    sumatoria+=i
print(sumatoria)

#Ejercicio 2
preguntaNumero="Ingresa un número entero para calcular su factorial : "
factorial=1
numeroIngresado= int(input(preguntaNumero))
for i in range(numeroIngresado):
    factorial=factorial*(i+1)
print(factorial)

