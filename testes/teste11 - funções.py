#Funções
#São comandos/blocos em código que executa uma função/tarefa
#função() -> função simples
#função(parametro) -> função com parametro

#dois tipos de funções:
#funções do sistema: funções pré-programadas da linguagem -> print() input() etc
#funções do script: funções criadas dentro do script

#Como criar funções/functions
#Utilizando o "def" - definição

#Funções Simples -> Apenas executam um bloco de comando
def ragequit():
    print("Cansei! Desligando o sistema...")
    #quit()
ragequit()

#Função Simples com Return
def calcularValor():
    valor = 10+10
    return valor
variavel = calcularValor()
print(variavel)

#Função com Parametros
#Parametros são variáveis da função que são preenchidos por quem chama a função (Externamente)
def somarNumeros(num1,num2):
    valor = num1+num2
    return valor

teste1 = somarNumeros(10,20)
print(teste1)

val1 = 30
val2 = 50
teste2 = somarNumeros(val1,val2)
print(teste2)