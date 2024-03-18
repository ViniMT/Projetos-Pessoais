import csv

def exportar_para_csv(veiculos, ex050324):
    with open(ex050324 + '.csv', 'w', newline='') as ex050324_csv:
        writer = csv.writer(ex050324_csv)
        writer.writerow(['Marca', 'Modelo', 'FIPE', 'Ano', 'Quilometragem'])
        for veiculo in veiculos:
            writer.writerow([veiculo.get_marca(), veiculo.get_modelo(), veiculo.get_fipe(), veiculo.get_ano(), veiculo.get_quilometragem()])

# Criando instâncias de veículos
carro1 = Carro("Mercedes-Benz", "AMG GT", 2000000, 2024, 10)
carro2 = Carro("Fiat", "Palio", 50000, 2010, 80000)

# Criando uma lista com as instâncias de veículos
lista_veiculos = [carro1, carro2]

# Exportando para CSV
exportar_para_csv(lista_veiculos, 'exercicio')
