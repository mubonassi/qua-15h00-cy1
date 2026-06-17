print("| SOMANDO NO INTERVALO |")
print("-"*40)

intervalo = int(input("Digite o intervalo a ser somado: "))

res = 0
conta = ""

for i in range(1,intervalo+1):
    res += i
    conta += str(i)
    if i < intervalo:
        conta += " + "

print(f"Conta: {conta} = {res}")