class TortaRedonda:
    def __init__ (self,saborIngresado):
        #Definir atributos
        self.forma ='Redonda'
        self.sabor= saborIngresado 
        #Accion al crear objeto
        print('Torta recien salida del horno')
    def mostrar_atributos (self):
        print(f"soy de forma {self.forma} y de sabor {self.sabor}")
    
#Se crea la torta 
tortaChocolate=TortaRedonda('Chocolate')
tortaVainilla=TortaRedonda('Vainilla')

print(tortaChocolate.sabor)
print(tortaVainilla.sabor)
print(tortaVainilla.forma)
print(tortaChocolate.forma)