print("--- LIQUIDANDO ESTOQUE ---")
print("-"*30)

listaProdutos = ["Carta Tun Tun Tun Sahur","Booster Pack Italian Brainrot","Booster Box Italian Brainrot","Carta Bombardillo Crocodillo","Deck Completo Tang Tang Keletang","Carta Foil Ballerina Cappucinna"]

print("-- Lista de produtos: ")
print(listaProdutos)

print("-- Selecione o produto pelo seu index")
produto = int(input("Digite aqui: "))

print(f"Produto selecionado: {listaProdutos[produto]}")

listaProdutos[produto] = "((ESGOTADO))"

print("-- Lista de produtos: ")
print(listaProdutos)