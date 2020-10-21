import matplotlib.pyplot as plt

ciudades =['Medellin','Bogota','Cali','Cartagena' ]
poblacion=[2508500, 7181469,2420100,914552]

plt.bar(ciudades,poblacion)
plt.title('Ciudades vs población')
plt.xlabel('Ciudades colombia')
plt.ylabel('Población')
plt.savefig('GraficoCiudades.png')
plt.show()
