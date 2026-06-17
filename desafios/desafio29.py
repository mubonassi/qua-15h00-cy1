print("| CONTAGEM DE CARACTERES |")
print("-"*40)

palavra = input("Digite a palavra para contar os caracteres: ")

contagem = 0

for i in palavra:
    contagem += 1

print(f"A palavra {palavra} contém {contagem} caracteres")