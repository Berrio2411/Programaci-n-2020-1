class Persona ():
    #Crear 
    def __init__ (self,nombreIn,edadIn,pesoIn,idIn,alturaIn,sexoIn):
        self.nombre= nombreIn
        self.edad= edadIn
        self.id= idIn
        self.peso=pesoIn
        self.altura=alturaIn
        self.sexo=sexoIn
        print('Individuo 1')
    def mostrar_atributos(self):
        print(f'Hola soy{self.nombre},tengo {self.edad} años,peso {self.peso},mi id es {1007822329},mi estatura es {self.altura} y mi sexo es {self.sexo}')

persona1=Persona('Santiago',18,65,1007822329,1.78,'Masculino')
persona1.mostrar_atributos()


