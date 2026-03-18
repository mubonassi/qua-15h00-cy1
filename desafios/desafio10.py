print("| Adivinhando Senha |")
print("-"*20)
senha = "abc123"
tentativa = input("> Digite a senha que deseja adivinhar: ")

if tentativa == senha:
    print("Você quebrou a senha!")
else:
    print(f"Você não quebrou a senha!\nA senha era: {senha}")