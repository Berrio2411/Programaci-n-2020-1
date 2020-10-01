import paciente as p 
class Estable ( p.Paciente):
    def __init__ (self,nombreIn,idIn,sexoIn,afiliadoIn,tiempoIn,temperaturaIn,animoIn):
        p.Paciente.__init__(self,nombreIn,idIn,sexoIn,afiliadoIn)
        self.tiempo=tiempoIn
        self.temperatura=temperaturaIn
        self.animo=animoIn
    def cuidados(self,list):
        for cuidados in listaCuidados:
            print(f'el paciente de nombre {self.nombre} seguirá la recomendacion de {cuidados}')


listaCuidados=['Dormir minimo 8 horas','Reposo','Pastillas cada 6 horas','Aislamiento']

pacienteestable1=Estable('Santiago',1007822329,'Masculino','SURA',2,37,'feliz')
pacienteestable1.cuidados(listaCuidados)
