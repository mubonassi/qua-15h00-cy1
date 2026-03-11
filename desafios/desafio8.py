print("| ACRESCÍMO DE 10% |")
valor = float(input("Digite um valor para receber acréscimo: "))

#método 1: utilizando uma nova variável
acrescimo = valor * 1.10 #1
acrescimo = valor + (valor*0.1) #2
acrescimo = valor + (valor/10) #3

print(f"O acréscimo de 10% deu: {acrescimo}")

#método 2: mudando dentro da variavel
valor = valor * 1.10