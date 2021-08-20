lanche = ["hamburguer", "coca", "Pizza", "sorvet", "bolacha"]
'''
lanche.insert(0, 5)
print(lanche)


del lanche[0] #remove pelo indice
lanche.pop(2)#remove pelo indice
lanche.remove("bolacha")#remove pelovalor
print(lanche)
'''
lista = list()
lista.append(lanche)

print(lista)

print(lanche.index("hamburguer"))