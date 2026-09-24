
# FOR - itera sobre uma sequencia (lista, tupla, string, etc)

frutas = ["maca", "banana", "laranja"]

for fruta in frutas:
    print(fruta)


# WHILE - repete enquanto uma condicao for verdadeira

contador = 0

while contador < 5:
    print(contador)
    contador += 1

# Cuidado: se a condicao nunca virar falsa, vira um loop infinito!


# CONTROLE DE LOOPS


# break -> interrompe o loop imediatamente
contador = 0
while True:
    print(contador)
    contador += 1
    if contador == 5:
        break

# continue -> pula o restante do bloco e vai para a proxima iteracao
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # imprime so os numeros impares

# pass -> nao faz nada, serve como marcador de posicao (placeholder)
for i in range(5):
    pass


# EXEMPLO COMBINANDO OS TRES

for i in range(10):
    if i == 8:
        break            # para quando chegar no 8
    if i % 2 == 0:
        continue         # pula os pares
    print(i)             # imprime so impares antes do 8