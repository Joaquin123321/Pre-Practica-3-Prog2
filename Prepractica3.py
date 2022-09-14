class Vehiculo():

    def __init__(self) -> None:
        self.marca = "Ford"
        self.ruedas = 4
        self.color = "Azul"
        self.enMarcha = False

    def arrancar(self):
        self.enMarcha = True
        print("El auto/la moto está en marcha")

    def tipoVehiculo(self):
        if (self.ruedas == 4):
            print("Automóvil")
        else:
            if (self.ruedas == 2):
                print("Motocicleta")
    
    def mostrar(self):
        print(self.marca)
        print(self.ruedas)
        print(self.color)
        print(self.enMarcha)

miAuto = Vehiculo()
miAuto.arrancar()
miAuto.tipoVehiculo()
miAuto.mostrar()


