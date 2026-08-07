class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def aplicar_desconto(self, porcentagem):
        self.preco -= self.preco * (porcentagem / 100)


class Livro(Produto):
    def __init__(self, nome, preco, autor):
        super().__init__(nome, preco)
        self.autor = autor


class Eletronico(Produto):
    def __init__(self, nome, preco, voltagem):
        super().__init__(nome, preco)
        self.voltagem = voltagem


livro = Livro("Python para Iniciantes", 80.00, "João Silva")
eletronico = Eletronico("Notebook", 3500.00, "220V")

livro.aplicar_desconto(15)
eletronico.aplicar_desconto(10)

print("=== Livro ===")
print("Nome:", livro.nome)
print("Autor:", livro.autor)
print(f"Preço com desconto: R$ {livro.preco:.2f}")

print("\n=== Eletrônico ===")
print("Nome:", eletronico.nome)
print("Voltagem:", eletronico.voltagem)
print(f"Preço com desconto: R$ {eletronico.preco:.2f}")
