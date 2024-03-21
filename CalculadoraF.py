# Calculadora de faturamento

vendas_22 = {"jan": 15000, "fev": 15500, "mar": 14000, "abr": 16600, "mai": 16300, "jun": 17000}
vendas_23 = {"jan": 17000, "fev": 15000, "mar": 17500, "abr": 16900, "mai": 16000, "jun": 18500}

# Quero saber quanto variou percentualmente cada mês de 2023 em comparação com 2022
# Simule: se a empresa tivesse pelo menos empatado com 2022 nos meses que ela vendeu menos,
# qual teria sido o faturamento?

# Primeira forma de calcular
faturamento_total_simulado = 0
for mes in vendas_23:
    valor_22 = vendas_22[mes]
    valor_23 = vendas_23[mes]
    variacao_percentual = valor_23 / valor_22 - 1
    if valor_23 < valor_22:
        vendas_23[mes] = valor_22
    print(f"Variação do {mes}: {variacao_percentual:.2%}")
    print(faturamento_total_simulado)

# Segunda forma de calcular
faturamento_total_simulado = 0
for mes in vendas_23:
    valor_22 = vendas_22[mes]
    valor_23 = vendas_23[mes]
    variacao_percentual = valor_23 / valor_22 - 1
    if variacao_percentual < 0:
        faturamento_total_simulado = faturamento_total_simulado + valor_22
    else:
        faturamento_total_simulado = faturamento_total_simulado + valor_23

faturamento_total = sum(vendas_23.values())

print(faturamento_total_simulado)
print(faturamento_total)
