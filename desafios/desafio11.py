print("| ALGORITMO DO BAR DO ZÉ CREUDIO |")
print("-"*40)
nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

if idade >= 18:
    print(f"Seja bem vindo, {nome}, você poderá entrar!")
else:
    print(f"Dê um fora daqui, {nome}, você não poderá entrar!")