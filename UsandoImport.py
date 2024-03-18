import requests

def buscar_endereco_por_cep(cep):
    # Construindo a URL com o CEP fornecido
    url = f'https://viacep.com.br/ws/{cep}/json/'

    # Fazendo a solicitação GET para o URL
    response = requests.get(url)

    # Verificando se a solicitação foi bem-sucedida
    if response.status_code == 200:
        # Extrai os dados JSON da resposta
        data = response.json()

        # Imprime os dados obtidos
        print("CEP:", data.get('cep'))
        print("Logradouro:", data.get('logradouro'))
        print("Complemento:", data.get('complemento'))
        print("Bairro:", data.get('bairro'))
        print("Cidade:", data.get('localidade'))
        print("Estado:", data.get('uf'))
    else:
        print("Erro ao fazer a solicitação:", response.status_code)

# Obtendo o CEP do usuário
cep = input("Digite seu CEP (apenas números): ")

# Chama a função para buscar o endereço pelo CEP
buscar_endereco_por_cep(cep)
