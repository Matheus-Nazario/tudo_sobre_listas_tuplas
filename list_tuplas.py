# LISTAS:

# Sequencias de elementos.
# Delimitada por colchetes [ ]
a = [3, 6, 8]

# Listas heterogêneas: Pode conter diferentes tipos de dados
b = [2, "abc", 4.5]

# listas vazias
c = []

# função print pode ser utilizada para exibir os itens contidos na lista
lista = [2, 5, 6]
print(lista)

# Índice: especifica a posição de um item na lista. Índice inicial é 0
print(lista[0])

# Índices negativos indicam posições referente ao final da lista
print("final", lista[-1])

# append: adiciona item ao final da lista
lista.append(100)
print(lista)

# repetição for para percorrer a lista
for a in lista:
    if a % 2 == 0:
        print(a)


# preencher lista com dados informados pelo usuário
"""
lista = []
for a in range(5):
    n = int(input('Numero: '))
    lista.append(n)
print(lista)
"""
# ---------------------------------------------------
# PRINCIPAIS FUNÇÕES

lista = [3, 5, 7, 8, 5, 9, 8, 10]

# len: Retorna o tamanho de uma lista
print(len(lista))

# count: Contar quantas vezes um item aparece na lista
print(lista.count(5))

# index: Retorna o índice da primeira ocorrência de um item
# Se o item não for encontrado retorna uma exceção
print(lista.index(5))

# in: verificar se determinado item existe em uma lista
if 50 in lista:
    print(lista.count(50))
else:
    print("Não existe")

# insert: insere item em determinada posição
lista.insert(3, 99)
print(lista)

# pop(): Remove o último item da lista
lista.pop()
print(lista)

# pop(indice): Remove um item pelo indice
lista.pop(1)
print(lista)

# remove: Remove primeira ocorrencia de um item da lista
lista.remove(99)
print(lista)

# remover varios itens da lista
while 5 in lista:
    lista.remove(5)

# sort: ordenação da lista
lista.sort()
print(lista)

a = ["zé", "abacaxi", "joao"]
a.sort()
print(a)

# sort(reverse=True): ordenação decrescente
lista.sort(reverse=True)
print(lista)

# min: menor elemento
print(min(lista))

# max: maior elemento
print(max(lista))

# sum: somatorio da lista
print(sum(lista))

# concatenação de listas
lista1 = [2, 5, 6]
lista2 = [4, 7, 9]
lista3 = lista1 + lista2
print(lista3)

# ----------------------------------------------
# TUPLAS

# Sequencias de elementos que não podem ser alteradas
# Delimitada por parenteses ( )
tupla = (4, 7, 8)

# tuplas vazias
tuplavazia = ()

# tuplas de 1 elemento (tem uma virgula no final)
tupla = (10,)
print(tupla)

# acesso pelo índice
tupla = (5, 7, 8)
print(tupla[0])

# repetição for pode ser utilizada para percorrer a tupla
tupla = (4, 7, 9, 10)
for a in tupla:
    print(a)

# concatenção de tuplas
tupla1 = (4, 7, 9)
tupla2 = (5, 99, 100)
tupla3 = tupla1 + tupla2
print(tupla3)

# tuple: converter lista em tupla
lista = [3, 5, 8]
tupla = tuple(lista)
print(tupla)

# list: converter tupla em lista
tupla = (4, 7, 9)
lista = list(tupla)
print(lista)
