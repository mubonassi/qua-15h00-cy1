#Guardando e Processando Informações
#Variaveis -> São pedaços na memória do programa que guarda um tipo de informação
#Declara uma Variavel -> Define o seu nome junto com o seu valor inicial
#Ex: Variavel = Valor

nome = "Murilo Bonassi" #String
idade = 31 #Int
altura = 1.67 #Float
trabalha = True #Boolean
calculo = 1+2-3*4/5**6 #Lógico -> Guarda o resultado do processo/comando

#Exibindo as Informações
#Método 1 - Concatenando Informações
print("Meu nome é",nome)
print("Eu tenho",idade,"anos")

#Método 2 - Formatando o String
print(f"Eu tenho {altura}m de altura")
print(f"Minha situação de trabalho é {trabalha}")
print(f"1+2-3*4/5**6 = {calculo}")

#Recebendo Informações
#Função input() -> Recebe informação do usuário pelo terminal EM STRING
#Ela pode usar usada para guardar a informação na variavel
nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")
altura = input("Digite a sua altura: ")

#Exibindo as 3 variaveis em um único print
print(f"Seu nome é {nome}, com a idade de {idade} anos e a altura de {altura}m")

#Processando/Calculando Informações na Variavel
#Somando Strings
nome = input("Digite o seu nome: ")
sobrenome = input("Digite o seu sobrenome: ")
nomeCompleto = nome + " " + sobrenome
print(f"Seu nome completo é {nomeCompleto}")

#Somando Números
#Numeros precisam ser convertidos/traduzidos
#Ex: int(valor)
numero1 = int(input("Digite o Numero 1: "))
numero2 = int(input("Digite o Numero 2: "))
soma = numero1 + numero2
print(f"{numero1} + {numero2} = {soma}")