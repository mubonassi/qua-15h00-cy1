print("| LOJA MANEIRA |")
p1 = float(input("Digite o valor do 1º produto: "))
p2 = float(input("Digite o valor do 2º produto: "))
p3 = float(input("Digite o valor do 3º produto: "))

tp = p1+p2+p3
cr = tp * 1.078
db = tp
av = tp * 0.95

print(f"Total: R${tp}")
print("-"*20)
print("> Formas de Pagamento")
print(f"- Crédito: R${cr}")
print(f"- Débito: R${db}")
print(f"- À Vista (em dinheiro): R${av}")