class Persona:
    def __init__(self,estaturaIngresado,pesoIngresado,nombreIngresado,idIngresado,edadIngresado):
        self.raza='Hummano'
        self.estatura= estaturaIngresado
        self.peso= pesoIngresado
        self.nombre= nombreIngresado
        self.id= idIngresado
        self.edad= edadIngresado
        print('Hola mundo esto vivo')
    def caminar(self):
        print('Voy a caminar')
    def saludo (self,saludoEspecial):
        print(saludoEspecial)
class Arquitecto (Persona):
    def dibujarPlanos(self):
        print (f'Hola soy {self.nombre} y voy a dibujar el plano')
class Ingenierio_Biomedico(Persona):
    def cultivaCelulas(self):
        print (f'Hola soy {self.nombre} y voy a cultivar celulas')


karla= Arquitecto(1.62,50,'Karla',1008532456,23)
karla.caminar()

karla.saludo('Holi Crayoli')
karla.dibujarPlanos()


