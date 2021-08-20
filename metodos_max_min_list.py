"""
Preencha uma lista com 10 números digitados pelo usuário e exiba:
o maior número da lista
o menor número da lista
a quantidade de números pares contidos na lista
a média dos números contidos na lista
todos os números menores do que a média calculada no item anterior
"""


lista = []

for pergunta in range(1, 11):
    num = int(input("Digite um número:"))
    lista.append(num)

print("O Menor número da lista é {}".format(min(lista)))
print("O Maior número da lista é {}".format(max(lista)))

lista_pares = []
cont = 0
for i in lista:
    if i % 2 == 0:
        lista_pares.append(i)
        cont += 1

print("A quantidade de pares são {}".format(cont))

total = sum(lista)
media = total / len(lista)

print("A Soma dos números da lista é {}".format(total))
print("A Média dos números da lista é {}".format(media))
