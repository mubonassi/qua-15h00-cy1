print("> ENTREVISTA DE'MPREGO")

print("Responda com 'sim' ou 'não'")
resposta = input("Você veio para a entrevista?: ")

if resposta == "sim":
    resposta = input("Você trouxe o currículo?: ")
    if resposta == "sim":
        print("Showps, bora começar a entrevista!")
    else:
        print("Po, precisa de currículo. Vai lá buscar. Pede Uber. Ou onibus. Você pode ir andando também. Ou se arrastando. É rico? Pode ir de helicoptero também. Ou não. Você pode dormir no sofá daqui.")
else:
    print("Ah, então, o que está fazendo aqui?")