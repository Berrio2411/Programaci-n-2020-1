import paciente as p
class Critico (p.Paciente):
    def __init__ (self,nombreIn,idIn,sexoIn,afiliadoIn,habitacionIn,patologiaIn):
        p.Paciente.__init__(self,nombreIn,idIn,sexoIn,afiliadoIn)
        self.habitacion=habitacionIn
        self.patologia=patologiaIn
    def sintomas(self,lista):
        for elemento in lista:
            print(elemento)

listaSintomas =['Nauseas','Dolor de cabeza','fiebre']

pacientecritico1=Critico('Santiago',1007822329,'Masculino','SURA',203,'Fiebre')
pacientecritico1.sintomas(listaSintomas)



