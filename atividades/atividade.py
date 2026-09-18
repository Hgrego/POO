from abc import ABC, abstractmethod


class Veiculo(ABC):
    def __init__(self, modelo):
        self.modelo = modelo

    @abstractmethod
    def acelerar(self):
        pass


class Carro(Veiculo):
    def acelerar(self):
        print(f"O carro {self.modelo} acelerou rapidamente pela pista!")


class Moto(Veiculo):
    def acelerar(self):
        print(f"A moto {self.modelo} acelerou com muita agilidade!")


class Caminhao(Veiculo):
    def acelerar(self):
        print(f"O caminhão {self.modelo} acelerou com força e potência!")


# Bônus: nova classe de veículo
class CarroEletrico(Veiculo):
    def acelerar(self):
        print(f"O carro elétrico {self.modelo} acelerou silenciosamente!")


# Lista heterogênea: diferentes tipos de veículos
pista_de_corrida = [
    Carro("Toyota Corolla"),
    Moto("Honda CB 500"),
    Caminhao("Volvo FH"),
    CarroEletrico("Tesla Model 3")
]


# Simulação polimórfica da corrida
for veiculo in pista_de_corrida:
    veiculo.acelerar()