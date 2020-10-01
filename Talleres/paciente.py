class Paciente ():
    #Crear
    def __init__ (self,nombreIn,idIn,sexoIn,afiliadoIn):
        self.nombre= nombreIn
        self.id=idIn
        self.sexo=sexoIn
        self.afiliado=afiliadoIn
        print('Paciente 1')
    def mostrar_atributos(self):
        print(f'Hola soy {self.nombre},mi numero de identificación es {self.id},soy de genero {self.sexo} y estoy afiliado a {self.afiliado} ')
    def mostrar_sintomas (self,lista):
        for elemento in lista:
            print(elemento)
sintomas =['Nauseas','Dolor de cabeza','fiebre']


paciente1=Paciente('Santiago',1007822329,'Masculino','SURA')
paciente1.mostrar_atributos() 
paciente1.mostrar_sintomas(sintomas)


