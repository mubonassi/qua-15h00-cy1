print("> POSITIVO, NEGATIVO OU NEUTRO")

numero = float(input("Digite um número para ser verificado: "))

if numero > 0:
    print("O número é positivo!")
else:
    if numero == 0:
        print("O número é neutro!")
    else:
        print("O número é negativo")