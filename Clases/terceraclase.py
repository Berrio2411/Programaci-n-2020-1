a = int (input ("ingrese el primer número entero : "))
b = int (input ("ingrese el segundo número entero : "))
print (a,b)

if (a==b):
    print("son números iguales")
elif (a>b): 
    print("el numero A",a,"Es mayor que el numero B",b)
else :
    print(f"El numero B {b} es mayor que el numero A {a}")

# Dada una temperatura determinar si el paciente esta sano o no
# Temperatura menor a 36 grados hipotermia
# Temperatura en el intervalo 36-38 normal
# Temperatura en el intervalo 37.5-38 alerta
# Temperatura mayor a 38 fiebre 
# Muestre el nombre del paciente y estado

name= (input("ingrese nombre del paciente : "))
temperatura= float(input("ingrese la temperatura del paciente : "))
if ( temperatura< 36):
    print(f"el paciente llamado {name} tiene hipotermia")
elif (temperatura>=36 and temperatura<37.5 ) :
    print(f"el paciente llamado {name} se encuentra sano")
elif (temperatura>=37.5 and temperatura<38 ) :
    print(f"el paciente llamado {name} se encuentra en estado de alerta")
else:
    print(f"el paciente llamado {name} tiene fiebre")