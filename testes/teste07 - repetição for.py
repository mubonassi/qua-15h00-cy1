#Estrutura de Repetição
#Blocos de Código que irão se repetir (entrar em loop) e que irão terminar de repetir dependendo da estrutura

#for - repetição determinada (contada)
#range(x) - determina quantas vezes será repetido
#i - variável contadora

#0,1,2
for i in range(3):
    print("teste")

print("fim da repetição")

#usando a variável i dentro do contexto
for i in range(3):
    print(f"Repetição: #{i}")
print("fim da repetição")

#determinando o número inicial da contagem
#1,2,3
for i in range(1,4):
    print(f"Repetição #{i}")
print("fim da repetição")

#determinando o intervalo entre cada número no contador
#10,20,30,40,50,60,70,80,90,100
for i in range(10,101,10):
    print(f"Repetição #{i}")
print("fim da repetição")

lista = ["a","b","c","d"]
#a,b,c,d
for i in lista:
    print(i)
print("fim da repetição")

#b,a,t,a,t,a
for i in "batata":
    print(i)
print("fim da repetição")