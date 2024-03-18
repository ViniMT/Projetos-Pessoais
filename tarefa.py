# Façam um teste de mesa para os algoritmos a seguir 

# Algoritmo de busca 


def busca_sequencial(array, elemento):
    for i in range(len(array)):
        if array[i] == elemento:
            return i  # Retorna o índice do elemento se encontrado
    return -1  # Retorna -1 se o elemento não for encontrado

# Exemplo de uso:
array = [3, 8, 1, 6, 2, 5, 9]
elemento = 6
resultado = busca_sequencial(array, elemento)
if resultado != -1:
    print(f'O elemento {elemento} foi encontrado no índice {resultado}.')
else:
    print(f'O elemento {elemento} não foi encontrado no array.')


# Algoritmo de ordenação


def ordenacao_selecao(array):
    n = len(array)
    for i in range(n):
        # Encontra o índice do menor elemento restante
        indice_menor = i
        for j in range(i+1, n):
            if array[j] < array[indice_menor]:
                indice_menor = j
        
        # Troca o menor elemento encontrado com o primeiro elemento não ordenado
        array[i], array[indice_menor] = array[indice_menor], array[i]

# Exemplo de uso:
array = [64, 25, 12, 22, 11]
print("Array original:", array)
ordenacao_selecao(array)
print("Array ordenado:", array)


# Ordenação quicksort

def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        menores = [x for x in array[1:] if x <= pivot]
        maiores = [x for x in array[1:] if x > pivot]
        return quicksort(menores) + [pivot] + quicksort(maiores)

# Exemplo de uso:
array = [64, 25, 12, 22, 11]
print("Array original:", array)
array_ordenado = quicksort(array)
print("Array ordenado:", array_ordenado)