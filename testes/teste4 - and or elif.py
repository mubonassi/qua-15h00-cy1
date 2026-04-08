#Estrutura de Condição Encadeada e Composta

numero = int(input("Digite um número: "))

#If Composto (AND e OR) -> Trabalhando com múltiplas condições
#AND (e) -> Todas as condições necessitam ser verdadeiras
if numero >= 0 and numero <= 10:
    print("Você digitou um número entre 0 a 10")
else:
    print("Você não digitou um número entre 0 a 10. Que pena, tente novamente.")

#OR (ou) -> Uma das condições necessitam ser verdadeiras
if numero == 6 or numero == 8:
    print("Você digitou um dos números secretos!")
else:
    print("Você NÃO digitou um dos números secretos!")

#If Encadeado -> Multiplas condições sucessoras
#elif (else if ou "ou se") -> Uma nova condição caso a anterior tenha retornado falso

if numero > 0:
    print("Número positivo")
elif numero < 0:
    print("Número negativo")
else:
    print("Número neutro")