"""
Tuplas 
Tupla = colecao ordenada e imutavel de itens, definida com parenteses ().
"""

cores = ("vermelho", "verde", "azul")

# Uma vez criada, nao pode ser alterada (nao da pra adicionar, remover ou modificar itens)
# Mais rapida e "leve" que uma lista, por ser imutavel
# Pode conter tipos diferentes de dados

# Acesso e fatiamento (igual lista)
print(cores[0])       # primeiro item
print(cores[-1])      # ultimo item
print(cores[1:3])     # fatia da tupla

# Iteracao
for cor in cores:
    print(cor)

# Tupla com um unico item (precisa da virgula)
unica = ("azul",)   # sem a virgula, nao e tupla

# Desempacotamento (unpacking)
a, b, c = cores
print(a, b, c)  # vermelho verde azul

# Funcoes uteis
print(len(cores))            # tamanho
print(cores.count("azul"))   # quantas vezes aparece
print(cores.index("verde"))  # posicao do item

# Quando usar tupla em vez de lista: quando os dados nao devem mudar
# (ex: coordenadas, configuracoes fixas, chaves de dicionario)