class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo


class Carro(Veiculo):
    def __init__(self, marca, modelo, qtd_portas):
        super().__init__(marca, modelo)
        self.qtd_portas = qtd_portas



carro1 = Carro("Toyota", "Corolla", 4)


print("Marca:", carro1.marca)
print("Modelo:", carro1.modelo)
print("Quantidade de portas:", carro1.qtd_portas)