
arrNum = [0, 5, 3, 2,]

for i in range(len(arrNum)):
    for j in range(i+1, len(arrNum)):
        if arrNum[i] > arrNum[j]:
            aux = arrNum[i]
            arrNum[i] = arrNum[j]
            arrNum[j] = aux

print(arrNum)



data = {
    "alunos": [
        {
            "nome": "João",
            "idade": 22,
            "nota": 8.5
        },
        {
            "nome": "Maria",
            "idade": 20,
            "nota": 7.8
        },
        {
            "nome": "Pedro",
            "idade": 21,
            "nota": 9.2
        },
        {
            "nome": "Ana",
            "idade": 23,
            "nota": 6.9
        },
        {
            "nome": "Carlos",
            "idade": 19,
            "nota": 8.0
        }
    ]
}

def ordenarPor(arrData, chave):
    for i in range(len(arrData["alunos"])):
        for j in range(i + 1, len(arrData["alunos"])):
            if arrData["alunos"][i][chave] > arrData["alunos"][j][chave]:
                aux = arrData["alunos"][i]
                arrData["alunos"][i] = arrData["alunos"][j]
                arrData["alunos"][j] = aux
    
print(ordenarPor(data, 'nome'))
