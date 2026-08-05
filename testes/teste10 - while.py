#Estrutura de Repetição - While
#While -> Estrutura de repetição CONDICIONADA
#Repita até (condição) não for mais verdadeira

numero = 0
while numero == 0:
    numero = int(input("Digite um número que não seja zero: "))
print("fim da repetição")

#Repetição indefinida/loop infinito

while True:
    escolha = input("Digite 'quebrar' para sair da repetição: ")

    if escolha == 'quebrar':
        break
print("fim da repetição")