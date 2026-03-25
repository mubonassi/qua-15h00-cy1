print("> ALGORITMO DO POSTO")
print("-"*20)

faltando = float(input("Digite o quanto está faltando no tanque (em L): "))
abastece = float(input("Digite o quanto deseja abastecer (em L): "))

if abastece > faltando:
    print("Não pode abastecer, valor inválido!")
else:
    print("Você abasteceu seu tanque!")