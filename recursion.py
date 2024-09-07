'''def multiplicacion(a:int, b:int) -> int:
    if a == 0:
        return 0
    return b + multiplicacion(a - 1, b)
print(multiplicacion(4,5))'''

class Vehiculo:
    def __init__ (self, marca:str, combustible:str, tipo:str):
        self.marca = marca
        self.combustible = combustible
        self.tipo = tipo
    def encender(self ):
        pass
    def arrancar(self ):
        pass
    def __str__(self ):
        return f"El vehiculo es {self.marca} y utiliza como combustible {self.combustible} y es de tipo {self.tipo}."


class Moto(Vehiculo):
    def __init__(self,marca:str,combustible:str, tipo:str):
        super().__init__(marca, combustible, tipo)

class Carro(Vehiculo):
    pass

motocicleta = Moto("honda","corriente","enduro")
mi_carro = Carro("Mazda","extra","todo terreno")
print(motocicleta)
print(mi_carro)