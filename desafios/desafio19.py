print(">> CALCULADORA V2 <<")
print("-"*20)

n1 = float(input("Digite o #1 Número: "))
n2 = float(input("Digite o #2 Número: "))
print("-- Escolha o operador -- ( + - / * ** )")
op = input("Digite o Operador: ")

if op == "+":
    r = n1+n2
elif op == "-":
    r = n1-n2
elif op == "/":
    r = n1/n2
elif op == "*":
    r = n1*n2
elif op == "**":
    r = n1**n2
else:
    r = False

if r == False:
    print("ERRO!")
else:
    print(f"{n1} {op} {n2} = {r}")