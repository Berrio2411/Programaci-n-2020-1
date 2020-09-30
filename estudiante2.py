import clasepersona as p 
class Estudiante(p.Persona):
    def __init__ (self,nombreIn,edadIn,pesoIn,idIn,alturaIn,sexoIn,carreraIn,semestreIn):
        p.Persona.__init__(self,nombreIn, edadIn,pesoIn,idIn,alturaIn,sexoIn) 
        self.carrera=carreraIn
        self.semestre= semestreIn
    def estudiar(self,materia):
        print(f'Hola soy {self.nombre} y estudiaré {materia}')

estudiante1=Estudiante('Santiago',18,65,1008543236,1.78,'Masculino','Biomedica',3)

estudiante1.estudiar('Programación') 