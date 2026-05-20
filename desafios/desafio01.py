print("| Simples Calculos |")
numero1 = int(input("Digite o Numero 1: "))
numero2 = int(input("Digite o Numero 2: "))

#Método 1 - Uma variavel para cada operação
soma = numero1 + numero2
subtracao = numero1 - numero2
multi = numero1 * numero2
div = numero1 / numero2
pot = numero1 ** numero2

print(f"{numero1} + {numero2} = {soma}")
print(f"{numero1} - {numero2} = {subtracao}")
print(f"{numero1} / {numero2} = {div}")
print(f"{numero1} * {numero2} = {multi}")
print(f"{numero1} ** {numero2} = {pot}")

#Método 2 - Reutilizando a variavel
#resultado = numero1+numero2
#print(f"{numero1} + {numero2} = {resultado}")
#resultado = numero1-numero2
#print(f"{numero1} - {numero2} = {resultado}")