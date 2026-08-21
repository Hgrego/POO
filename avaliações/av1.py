class Funcionario:
    def __init__(self, nome, matricula, salario_base):
        self.nome = nome
        self.matricula = matricula
        self.__salario_base = salario_base

    def get_salario_base(self):
        return self.__salario_base

    def set_salario_base(self, novo_salario):
        if novo_salario > 0:
            self.__salario_base = novo_salario

    def calcular_salario_final(self):
        return self.get_salario_base()


class Gerente(Funcionario):
    def __init__(self, nome, matricula, salario_base, bonus_gestao):
        super().__init__(nome, matricula, salario_base)
        self.bonus_gestao = bonus_gestao

    def calcular_salario_final(self):
        return self.get_salario_base() + self.bonus_gestao


class Desenvolvedor(Funcionario):
    def __init__(self, nome, matricula, salario_base, nivel):
        super().__init__(nome, matricula, salario_base)
        self.nivel = nivel

    def calcular_salario_final(self):
        if self.nivel == "Senior":
            return self.get_salario_base() + 1500
        else:
            return self.get_salario_base()


gerente = Gerente("Bruno Henrique", "0347", 8000, 2700)
desenvolvedor = Desenvolvedor("Felipe luiz", "0984", 6750, "Senior")

gerente.__salario_base = -100

print("Salario base do gerente:", gerente.get_salario_base())
print("Nome:", gerente.nome)
print("Salario final:", gerente.calcular_salario_final())

print("Nome:", desenvolvedor.nome)
print("Salario final:", desenvolvedor.calcular_salario_final())