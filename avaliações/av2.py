class Veiculo:
    def __init__(self, modelo, placa, valor_diaria):
        self.set_modelo(modelo)
        self.set_placa(placa)
        self.set_valor_diaria(valor_diaria)

    # Getter e Setter do modelo
    def get_modelo(self):
        return self.__modelo

    def set_modelo(self, modelo):
        if not modelo.strip():
            raise ValueError("O modelo não pode estar vazio.")
        self.__modelo = modelo

    # Getter e Setter da placa
    def get_placa(self):
        return self.__placa

    def set_placa(self, placa):
        if not placa.strip():
            raise ValueError("A placa não pode estar vazia.")
        self.__placa = placa.upper()

    # Getter e Setter do valor da diária
    def get_valor_diaria(self):
        return self.__valor_diaria

    def set_valor_diaria(self, valor):
        if valor <= 0:
            raise ValueError("O valor da diária deve ser maior que zero.")
        self.__valor_diaria = valor

    # Método que será sobrescrito pelas subclasses
    def calcular_aluguel(self, dias):
        if dias <= 0:
            raise ValueError("A quantidade de dias deve ser maior que zero.")

        return self.__valor_diaria * dias

    def exibir_dados(self):
        print(f"Modelo: {self.__modelo}")
        print(f"Placa: {self.__placa}")
        print(f"Valor da diária: R$ {self.__valor_diaria:.2f}")


class Carro(Veiculo):
    def __init__(self, modelo, placa, valor_diaria, portas):
        super().__init__(modelo, placa, valor_diaria)

        if portas <= 0:
            raise ValueError("A quantidade de portas deve ser maior que zero.")

        self.portas = portas

    # Sobrescrita + Polimorfismo
    def calcular_aluguel(self, dias):
        if dias <= 0:
            raise ValueError("A quantidade de dias deve ser maior que zero.")

        valor_base = self.get_valor_diaria() * dias
        taxa_limpeza = 50

        return valor_base + taxa_limpeza

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Portas: {self.portas}")


class Moto(Veiculo):
    def __init__(self, modelo, placa, valor_diaria, cilindradas):
        super().__init__(modelo, placa, valor_diaria)

        if cilindradas <= 0:
            raise ValueError("As cilindradas devem ser maiores que zero.")

        self.cilindradas = cilindradas

    # Sobrescrita + Polimorfismo
    def calcular_aluguel(self, dias):
        if dias <= 0:
            raise ValueError("A quantidade de dias deve ser maior que zero.")

        valor_base = self.get_valor_diaria() * dias
        desconto = valor_base * 0.10

        return valor_base - desconto

    def exibir_dados(self):
        super().exibir_dados()
        print(f"Cilindradas: {self.cilindradas} cc")


# Lista centralizada com objetos heterogêneos
veiculos = []


def cadastrar_carro():
    try:
        modelo = input("Modelo do carro: ")
        placa = input("Placa: ")

        valor_diaria = float(
            input("Valor da diária: R$ ").replace(",", ".")
        )

        portas = int(input("Quantidade de portas: "))

        carro = Carro(
            modelo,
            placa,
            valor_diaria,
            portas
        )

    except ValueError as erro:
        print(f"\nErro: {erro}")

    else:
        veiculos.append(carro)
        print("\nCarro cadastrado com sucesso!")

    finally:
        print("Operação de cadastro finalizada.\n")


def cadastrar_moto():
    try:
        modelo = input("Modelo da moto: ")
        placa = input("Placa: ")

        valor_diaria = float(
            input("Valor da diária: R$ ").replace(",", ".")
        )

        cilindradas = int(
            input("Cilindradas: ")
        )

        moto = Moto(
            modelo,
            placa,
            valor_diaria,
            cilindradas
        )

    except ValueError as erro:
        print(f"\nErro: {erro}")

    else:
        veiculos.append(moto)
        print("\nMoto cadastrada com sucesso!")

    finally:
        print("Operação de cadastro finalizada.\n")


def listar_veiculos():
    try:
        if len(veiculos) == 0:
            print("Nenhum veículo cadastrado.")

        print("\n========== VEÍCULOS CADASTRADOS ==========")

        for i, veiculo in enumerate(veiculos, start=1):
            print(f"\n--- Veículo {i} ---")
            veiculo.exibir_dados()

    except LookupError as erro:
        print(f"\nAviso: {erro}")

    finally:
        print("\n===========================================\n")


def calcular_aluguel():
    try:
        if len(veiculos) == 0:
            raise LookupError("Nenhum veículo cadastrado.")

        listar_veiculos()

        numero = int(
            input("Digite o número do veículo: ")
        )

        if numero < 1 or numero > len(veiculos):
            raise LookupError("Veículo não encontrado.")

        dias = int(
            input("Quantidade de dias de aluguel: ")
        )

        if dias <= 0:
            raise ValueError(
                "A quantidade de dias deve ser maior que zero."
            )

        veiculo = veiculos[numero - 1]

        # POLIMORFISMO:
        # o Python executará o calcular_aluguel()
        # correspondente ao tipo do objeto.
        valor = veiculo.calcular_aluguel(dias)

    except ValueError as erro:
        print(f"\nErro: {erro}")

    except LookupError as erro:
        print(f"\nErro: {erro}")

    else:
        print("\n========== ALUGUEL ==========")
        print(f"Veículo: {veiculo.get_modelo()}")
        print(f"Placa: {veiculo.get_placa()}")
        print(f"Dias: {dias}")
        print(f"Valor total: R$ {valor:.2f}")
        print("=============================\n")

    finally:
        print("Operação de aluguel finalizada.\n")


def buscar_veiculo():
    try:
        if len(veiculos) == 0:
            raise LookupError("Nenhum veículo cadastrado.")

        placa = input("Digite a placa para buscar: ").upper()

        veiculo_encontrado = None

        for veiculo in veiculos:
            if veiculo.get_placa() == placa:
                veiculo_encontrado = veiculo
                break

        if veiculo_encontrado is None:
            raise LookupError(
                "Nenhum veículo encontrado com essa placa."
            )

    except LookupError as erro:
        print(f"\nErro: {erro}")

    else:
        print("\n========== VEÍCULO ENCONTRADO ==========")
        veiculo_encontrado.exibir_dados()
        print("=========================================\n")

    finally:
        print("Operação de busca finalizada.\n")


def menu():
    while True:
        print("""
========================================
       SISTEMA DE GESTÃO DE FROTA
========================================

1 - Cadastrar carro
2 - Cadastrar moto
3 - Listar veículos
4 - Buscar veículo por placa
5 - Calcular aluguel
0 - Sair

========================================
""")

        try:
            opcao = int(input("Escolha uma opção: "))

        except ValueError:
            print("\nErro: digite apenas números.")
            continue

        else:
            if opcao == 1:
                cadastrar_carro()

            elif opcao == 2:
                cadastrar_moto()

            elif opcao == 3:
                listar_veiculos()

            elif opcao == 4:
                buscar_veiculo()

            elif opcao == 5:
                calcular_aluguel()

            elif opcao == 0:
                print("\nSistema encerrado. Até mais!")
                break

            else:
                print("\nErro: opção inexistente. Escolha uma opção do menu.")


# Início do programa
menu()