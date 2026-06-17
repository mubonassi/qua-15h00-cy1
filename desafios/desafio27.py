print("| SOMANDO COM REPETIÇÃO |")
print("-"*40)

intervalo = int(input("Digite o intervalo a ser somado: "))

res = 0
conta = ""

for i in range(1,intervalo+1):
    num = int(input(f"Digite o {i}# número: "))

    if num < 0:
        print("Não se pode somar negativo")
        num = 0

    res += num
    conta += str(num)
    if i < intervalo:
        conta += " + "

print(f"Conta: {conta} = {res}")