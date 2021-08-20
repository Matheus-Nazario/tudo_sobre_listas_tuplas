"""
Preencha duas tuplas com 5 números cada, informados pelo usuário. Concatene as
duas tuplas e exiba a tupla resultante.
Dica: primeiro crie duas listas, e então,
converta as listas em tuplas utilizando a função tuple.

Exemplo: Suplonhas que as tuplas contenham o números:
(3, 1, 5, 3, 5)
(5, 5, 7, 3, 1).
Como resultado, o programa deve gerar a tupla:
(3, 1, 5, 3, 5, 5, 5, 7, 3, 1).
"""

lista_tupla_1 = []
lista_tupla_2 = []


for i in range(1, 11):
    if i < 6:
        num = int(input("Digite um número para lista 1: "))
        lista_tupla_1.append(num)
    else:
        num = int(input("Digite um número para lista 2: "))
        lista_tupla_2.append(num)

lista_as_duas = lista_tupla_1 + lista_tupla_2
lista_tupla = tuple(lista_as_duas)
print(lista_tupla)
