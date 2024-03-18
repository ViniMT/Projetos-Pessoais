class Carro:
    def __init__(self, marca, modelo, fipe, ano, quilometragem):
        self.marca = marca
        self.modelo = modelo
        self.fipe = fipe
        self.ano = ano
        self.quilometragem = quilometragem

    def get_marca(self):
        return self.marca
    def set_marca(self, marca):
        self.marca = marca

    def get_modelo(self):
        return self.modelo
    def set_modelo(self, modelo):
        self.modelo = modelo

    def get_fipe(self):
        return self.fipe
    def set_fipe(self, fipe):
        self.fipe = fipe

    def get_ano(self):
        return self.ano
    def set_ano(self, ano):
        self.ano = ano

    def get_quilometragem(self):
        return self.quilometragem
    def set_quilometragem(self, quilometragem):
        self.quilometragem = quilometragem

    def atualizar_fipe(self, novo_valor):
        self.fipe = novo_valor

    def atualizar_quilometragem(self, novo_valor):
        self.quilometragem = novo_valor

carro = Carro("Mercedes-Benz", "AMG GT", 2000000, 2024, 10)

print("Valores atuais:")
print("Marca:", carro.get_marca())
print("Modelo:", carro.get_modelo())
print("FIPE:", carro.get_fipe())
print("Ano:", carro.get_ano())
print("Quilometragem:", carro.get_quilometragem())

# Atualização de valores

carro.atualizar_fipe(input(f'Difite o novo valor da Fipe'))
carro.atualizar_quilometragem(input(f'Digite o novo valor da quilometragem'))

print('Valores atualizados:')
print('Fipe:', carro.get_fipe())
print('Quilometragem:', carro.get_quilometragem())