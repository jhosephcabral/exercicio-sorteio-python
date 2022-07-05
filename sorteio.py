import random

nomes = []

nome = input("Digite um nome: ")
while nome != "":
    nomes.append(nome)
    nome = input("Digite um nome: ")

indice = random.randint(0, len(nomes)-1)
print("A pessoa sorteada foi: ", nomes[indice])