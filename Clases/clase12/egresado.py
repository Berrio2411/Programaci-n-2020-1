
import estudiante as es
class Egresado(es.Estudiante):
    def __init__ (self,nombreIn,edadIn,idIn,carreraIn):

        es.Estudiante.__init__(self,nombreIn,edadIn,idIn,carreraIn,'Egresado')
        self.fecha=fechaIn
    def trabajar(self,empresa):
        print(f'')
