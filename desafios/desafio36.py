#Funções
def convMb(val):
    conv = val * 1024
    return conv
def convKm(val):
    conv = val * 1000
    return conv
def convLt(val):
    conv = val * 1000
    return conv
def convC(val):
    conv = (val*1.8)+32
    return conv
def convDol(val):
    conv = val*5.35
    return conv
def convTon(val):
    conv = val*1000
    return conv

print("| FERRAMENTAS DE CONVERSÃO |")
print("-"*60)

while True:
    print("-"*60)
    print("-- Selecione a Ferramenta --")
    print("1) Megabytes > Kilobytes")
    print("2) Kilometros > Metros")
    print("3) Litros > Mililitros")
    print("4) Celsius > Fahrenheit")
    print("5) Dólar > Real")
    print("6) Toneladas > Kilos")
    print("0) Sair")

    op = input(">> Digite a operação desejada: ")
    print("-"*60)
    if op in ["1","2","3","4","5","6","0"]:
        valor = float(input("Digite o valor para ser convertido: "))
        if op == "1":
            convertido = str(convMb(valor)) + "kb"
        if op == "2":
            convertido = str(convKm(valor)) + "km"
        if op == "3":
            convertido = str(convLt(valor)) + "ml"
        if op == "4":
            convertido = str(convC(valor)) + "ºF"
        if op == "5":
            convertido = "R$" + str(convDol(valor))
        if op == "6":
            convertido = str(convTon(valor)) + "kg"
        if op == "0":
            break
        print(f"Valor convertido: {convertido}")
        print("-"*60)
    else:
        print("Operação não encontrada, seu burro")
    input("Aperte enter para continuar...")