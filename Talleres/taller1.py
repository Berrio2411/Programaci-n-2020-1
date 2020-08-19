name = (input("por favor ingrese su nombre : "))
estatura = float(input("ingrese la  estatura del paciente : "))
peso = float(input("ingrese el peso del paciente en Kg : "))

imc = peso /estatura**2
print(imc)

if (imc <18.5):
    print(f"el paciente llamado {name} sufre de infrapeso ")
elif(imc>=18.5 and imc<25):
    print(f"el paciente llamado {name} tiene un peso normal")
elif(imc>=25 and imc<30):
    print(f"el paciente llamado{name} sufre de sobrepeso")
elif(imc>=30 and imc<35):
    print(f"el paciente llamado {name} sufre de obesidad")
else:
    print(f"el paciente llamado {name} sufre de obesidad mórbida")
