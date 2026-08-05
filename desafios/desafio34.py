import random

print("| SHOW DO PY-LHÃO! |")
print("-"*60)

perguntas = ["Qual é a cor do cavalo branco do napoleão?","Quantos anos duraram a guerra dos cem anos?","Quantos meses possuem 28 dias?"]
respostas = ["Preto","116","12"]

pergunta = random.randint(0,2)
print(">> RESPONDA A PERGUNTA ABAIXO <<")

erros = 0

while True:
    print(perguntas[pergunta])
    resposta = input("> Digite aqui sua resposta: ")

    if respostas[pergunta] == resposta:
        print("yay")
        if erros > 0:
            print(f"E você errou: {erros}")
        else:
            print("ERROU NENHUMA! É MESTRE SEPARÇA AI")

        break
    elif resposta == "desisto":
        print(f"A resposta era: {respostas[pergunta]}")

        break
    else:
        print("nay")
        erros += 1