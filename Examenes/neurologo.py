import doctor as d 
class Neurologo (d.Doctor):
    def __init__ (self,nombreIn,idIn,sexoIn,universidadIn,experienciaIn,consultorioIn,salarioIn):
        d.Doctor.__init__(self,nombreIn,idIn,sexoIn,universidadIn)
        self.experiencia=experienciaIn
        self.consultorio=consultorioIn
        self.salario=salarioIn
    def mostrar_atributos(self):
        print(f'Hola soy el doctor {self.nombre},mi numero de identificación es {self.id},soy de genero {self.sexo} y estudie en la universidad {self.universidad},cuento con una experiencia de {self.experiencia} años, mi consultorio es el {self.consultorio} y tengo un salario de {self.salario}')
    def pacientes(self,list):
        for pacientes in listaPacientes:
            print(f'atendré al paciente {pacientes}')
listaPacientes=['Juan','Santiago','Pablo','Carlos']
neurologo1=Neurologo('Santiago',1007822329,'Masculino','CES',15,403,5000)
neurologo1.mostrar_atributos() 
neurologo1.pacientes(listaPacientes)


