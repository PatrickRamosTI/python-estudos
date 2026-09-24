"""
Listas
Lista = colecao ordenada e mutavel de itens, definida com colchetes [].
"""

frutas = ["maca", "banana", "laranja"]

# OPERACOES COMUNS

frutas.append("uva")        # adiciona no final
frutas.insert(1, "pera")    # insere em posicao especifica
frutas.remove("banana")     # remove pelo valor
frutas.pop()                 # remove e retorna o ultimo item
frutas.pop(0)                 # remove e retorna item em posicao especifica
frutas.sort()                 # ordena a lista
frutas.reverse()              # inverte a ordem
print(len(frutas))            # tamanho da lista


# ACESSO E FATIAMENTO (SLICING)

print(frutas[0])       # primeiro item
print(frutas[-1])      # ultimo item
print(frutas[1:3])     # do indice 1 ate o 2 (exclui o 3)
print(frutas[:2])      # do inicio ate o indice 1
print(frutas[::-1])    # lista invertida



# ITERACAO

for fruta in frutas:
    print(fruta)


# LIST COMPREHENSION (forma compacta de criar listas)

quadrados = [x**2 for x in range(5)]
print(quadrados)  # [0, 1, 4, 9, 16]