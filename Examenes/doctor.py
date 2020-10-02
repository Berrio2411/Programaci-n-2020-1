class Doctor ():
    #Crear
    def __init__(self,nombreIn,idIn,sexoIn,universidadIn):
        self.nombre=nombreIn
        self.id=idIn
        self.sexo=sexoIn
        self.universidad=universidadIn
        print('Doctor 1')
    def mostrar_atributos(self):
        print(f'Hola soy el doctor {self.nombre},mi numero de identificación es {self.id},soy de genero {self.sexo} y estudie en la universidad {self.universidad} ')
    def mostrar_sintomas (self,lista):
        for elemento in lista:
            print(elemento)
sintomas =['Nauseas','Dolor de cabeza','fiebre']
doctor1=Doctor('Santiago',1007822329,'Masculino','CES')
doctor1.mostrar_atributos() 
doctor1.mostrar_sintomas(sintomas)
