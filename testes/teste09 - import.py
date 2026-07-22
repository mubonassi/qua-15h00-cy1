#Importando Bibliotecas
#Import -> Importando bibliotecas prontas

#Importando uma biblioteca de funções matemáticas especificas
import math

num1 = 400
num2 = 35
divisao = num1/num2 #divisão pura
arrendondado = math.floor(divisao) #arrendondando o valor da divisão com a função math.floor()
#math.ceil -> arredonda para cima
#math.floor -> arredonda para baixo

print(f"Divisão: {divisao} | Arredondado: {arrendondado}")

valor = 250
raizQuadrada = math.sqrt(valor)
pi = math.pi

print(f"Raiz quadrada: {raizQuadrada} | Pi: {pi}")

#Importa uma biblioteca de funções que permite escolher valores aleatórios
import random

valor = random.randint(1,100)
print(f"Valor aleatório: {valor}")

lista = ["a","b","c","d","e","f","g"]
item = random.choice(lista)
print(f"Item aleatório: {item}")