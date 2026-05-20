#Estrutura de Repetição
#Blocos de Código que irão se repetir (entrar em loop) e que irão terminar de repetir dependendo da estrutura

#for - repetição determinada (contada)
#range(x) - determina quantas vezes será repetido
#i - variável contadora

for i in range(3):
    print("teste")

print("fim da repetição")

#usando a variável i dentro do contexto
for i in range(3):
    print(f"Repetição: #{i}")
print("fim da repetição")

#determinando o número inicial da contagem
for i in range(1,4):
    print(f"Repetição #{i}")
print("fim da repetição")

#determinando o intervalo entre cada número no contador
for i in range(10,101,10):
    print(f"Repetição #{i}")
print("fim da repetição")