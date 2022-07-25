
# Listas ou vectores =

# from mailbox import NotEmptyError


# nomes =[]

# for i in range(3):

#     nome = input(f"Digite o nome do(a) {i + 1} aluno (a): ")

#     nomes.append(nome)
# print(nomes)

# Percorrendo os elementos da lista
# for nome in nomes:
#     print(nome)

# Enumerar
# for i, nome in enumerate(nomes):
#     print(f"{i + 1} - {nome}")

# lista_maluca = [1, "A", None, [], 2.0, True]
# print(lista_maluca[-2])
# print(len(lista_maluca))


# nome = "osmando"
# for letra in nome:
#     print(letra)

# Modificar o valor da lista

# lista = [1, 2 , 3, 4 , 5]
# lista[3] = 5
# print(lista)

# Usando split
# nome = "O s m a n d o".split(" ")#Tem que agregar um espaço
# nome[0] = "o"
# print(nome)

# nome = "Osmando"
# lista = [1, 2, 3, 4]
# print(nome[1:3])
# print(lista[2::])  # Começa no indice 2 e vai até o final

# # Adicionar lista
# lista.append(5)
# print(lista)

# # Remover um item da lista
# lista.pop()
# print(lista)

# # remover item pelo indice
# lista.pop(2)
# print(lista)

# # Slicing de vectores [inicio:fim:passo]
# numeros = [1, 2, 3, 4, 5]
# for numero in numeros[::-1]:
#     print(numero)

# print(numeros[::2])

"""
Faça um programa que leia e monte dois vetores de números inteiros com 3 números cada. Depois
de montados gere um terceiro vetor formado pela diferença dos dois vetores lidos, um quarto vetor
formado pela soma dos dois vetores lidos e por último um quinto vetor formado pela multiplicação
dos dois vetores lidos.

"""
# vetor1 = 0
# vetor2 = 0
# vetor_diferenca = 0
# vetor_soma = 0
# vetor_multiplicacao = [], [], [], [], []
# for i in range(3):
#     vetor1.append = int(input("Digite o {i + 1}º número do vetor 1: "))
#     vetor2.append(int(input(f"Digite o {i + 1}º número do vetor 2: ")))
#     vetor_diferenca.append(vetor1[i] - vetor2[i])
#     vetor_soma.append(vetor1[i] + vetor2[i])
#     vetor_multiplicacao.append(vetor1[i] * vetor2[i])

# print(f"Vetor 1: {vetor1}")
# print(f"Vetor 2: {vetor2}")
# print(f"Vetor Diferença: {vetor_diferenca}")
# print(f"Vetor Soma: {vetor_soma}")
# print(f"Vetor Multiplicação: {vetor_multiplicacao}")