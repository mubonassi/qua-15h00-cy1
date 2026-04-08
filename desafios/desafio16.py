print("| VERIFICAÇÃO DE CONVITE |")
nome = input("Digite o seu nome: ")
idade = int(input("Fala a sua idade: "))
convite = input("Você tem um convite? (S/N): ")

if idade >= 18 and convite == "S":
    print(f"Seja bem vindo, {nome}! Pode entrar!")
elif idade < 18 and convite == "N":
    print(f"Me fez perder o tempo pra que, {nome}")
elif idade < 18:
    print(f"Você é menor de idade, sai daqui, seu pentelho {nome}")
elif convite == "N":
    print(f"Você está bloqueado de entrar nessa festa super maneira, {nome}!.")
else:
    print("que")