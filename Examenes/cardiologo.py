import doctor as d 
class Cardiologo (d.Doctor):
    def __init__ (self,nombreIn,idIn,sexoIn,universidadIn,experienciaIn,consultorioIn,salarioIn):
        d.Doctor.__init__(self,nombreIn,idIn,sexoIn,universidadIn)
        self.experiencia=experienciaIn
        self.consultorio=consultorioIn
        self.salario=salarioIn
    def mostrar_atributos(self):
        print(f'Hola soy el doctor {self.nombre},mi numero de identificación es {self.id},soy de genero {self.sexo} y estudie en la universidad {self.universidad},cuento con una experiencia de {self.experiencia} años, mi consultorio es el {self.consultorio} y tengo un salario de {self.salario}')
    def mostrar_sintomas (self,lista):
        for elemento in lista:
            print(elemento)
sintomas =['Nauseas','Dolor de cabeza','fiebre']
cardiologo1=Cardiologo('Santiago',1007822329,'Masculino','CES',15,403,5000)
cardiologo1.mostrar_atributos() 
cardiologo1.mostrar_sintomas(sintomas)
print('Ya se que tiene este paciente')
