#Estruturas de Condição -> Criam condições para que um bloco de código seja executado
#Um comando só irá acontecer se determinada condição for verdadeira
#Condição > Ação
#Ex: Se o número digitado for 13 acontece a mensagem "você digitou o número 13"

numero = int(input("Digite um número para ser verificado: "))

#se (condição) então {ação}
if numero == 13:
    print("Você digitou o número 13")
#senão {ação}
else:
    print("Você NÃO digitou o número 13")

#Comparadores
# == -> Igual a (valor == valor)
# > -> Maior que (valor > valor)
# < -> Menor que (valor < valor)
# >= -> Maior ou igual a (valor >= valor)
# <= -> Menor ou igual a (valor <= valor)
# != -> Diferente de (valor != valor)

#Diferença entre = e ==
# = -> Atribuição -> Nome = "Danilo" -> O nome É Danilo
# == -> Comparação -> Nome == "Matheus" -> O nome é Matheus?