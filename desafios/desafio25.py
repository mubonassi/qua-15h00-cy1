print("| PARES E IMPARES |")
print("-"*30)

intervalo = int(input("Digite o intervalo de pares e impares: "))

pares = []
for i in range(2,intervalo+1,2):
    pares.append(i)

impares = ""
for i in range(1,intervalo+1,2):
    #impares = impares + str(i) + " "
    impares += f"{i} "

print(f"Pares: {pares}")
print(f"Impares: {impares}")