import random

print("| GACCHA DOIDO! |")

premios = ["Papel Higienico","Linguiça","Controle Remoto","Fone de Ouvido","Palito de Dente","iPhone Pro Max 19","Papelão"]

for i in range(1,3+1):
    premio = random.choice(premios)
    print(f"{i}º Tentativa: {premio}")
    if premio == "Papelão":
        print("VOCÊ CONSEGUIU O PRÊMIO MÁXIMO! PARABENS!")
        break
    elif i == 3:
        print("Você não conseguiu o prêmio máximo e acabou as tentativas!")
    else:
        print("Deseja realizar uma nova tentativa?")
        escolha = input("Digite aqui (sim/não): ")
        if escolha == "sim":
            print("Próxima tentativa!")
        else:
            print(f"Então, você manterá o prêmio: {premio}")
            break