"""
Escreva uma função chamada intercala_numeros que recebe como entrada duas
listas de três elementos e retorna uma lista de seis elementos,
com os números intercalados.

Exemplo:
Suponha que as listas de entrada da função sejam:
[1, 2, 3]
[4, 5, 6]
Para estas listas, a função deve retornar:
[1, 4, 2, 5, 3, 6]
"""


def intercala_numeros(list_1, list_2):
    lista_3 = []
    for i in range(3):
        lista_3.append(list_1[i])
        lista_3.append(list_2[i])
    return lista_3


lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista3 = intercala_numeros(lista1, lista2)
print(lista3)
