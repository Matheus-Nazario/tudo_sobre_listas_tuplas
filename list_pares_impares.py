"""
Preencha uma lista com 10 números digitados pelo usuário. A partir desta lista,
gere uma lista com os números pares e outra com os números ímpares.
Exemplo:
Suponha que a lista digitada seja: [1, 4, 7, 9, 5, 3, 7, 9, 8, 8].
Para esta lista, o programa deve gerar as seguintes listas:
[4, 8, 8]
[1, 7, 9, 5, 3, 7, 9]
"""
lista = []

for i in range(1, 11):
    num = int(input("Digite um número: "))
    lista.append(num)

lista_pares = []
lista_impares = []
count = 0

for i in lista:
    if i % 2 == 0:
        lista_pares.append(i)
    else:
        lista_impares.append(i)

print(lista_pares)
print(lista_impares)
