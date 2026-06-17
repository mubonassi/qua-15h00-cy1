#Break e Quit()
#Break -> Uma palavra chave que encerra um fluxo de repetição
for i in range(100000000000000000000):
    print(i)
    if i >= 5:
        break
print("Fim da repetição")

#quit() é uma função que ENCERRA o algoritmo
for i in range(1000000):
    print(i)
    if i >= 5:
        quit()
print("ESSE PRINT NÃO SERA MOSTRADO")