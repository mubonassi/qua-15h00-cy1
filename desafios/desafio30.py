print("| Z-TYPE GENÉRICO! |")

palavras = ["Agrião","Paralelepípedo","Ornitorrinco","que"]

acertos = 0
erros = 0
for palavra in palavras:
    print(f"Digite a palavra: {palavra}")
    tentativa = input("Digite aqui: ")

    if tentativa == palavra:
        acertos += 1
        print("Você acertou!")
    else:
        erros += 1
        print("Você errou!")

if erros == 0:
    print("Você não errou nenhuma! Parabéns!")
elif acertos == 0:
    print("Mds, não acertou UMA PALAVRA!")
else:
    print(f"Parabéns! Você acertou {acertos} palavras, e errou {erros} palavras!")
