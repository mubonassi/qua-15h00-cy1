def escolherFruta():
    print("| FRUTA FAVORITA |")
    print("-"*20)

    frutas = ["Maçã","Uva","Pitanga","Pitaya","Maracuja","Morango","Mexirica","Laranja","Abacaxi","Lichia","Manga","Melancia","Amora","Abacate","Tomate","Pera","Banana","Maçã Verde","Blueberry","Framboesa","Cereja","Melão","Mamão","Coco","Jabuticaba","Romã","Limão","Goiaba","Acerola","Caqui","Kiwi","Pessego","Jaca","Guarana","Açaí","Caju"]

    print("Selecione sua fruta favorita da lista!")
    print(f"Lista de Frutas: {frutas}")

    fruta = int(input("Digite a opção: "))

    print("--Fruta Selecionada--")
    print(f"Favorita: {frutas[fruta]}")

def cadastrar():
    print("|SISTEMA DE CADASTRO E LOGIN|")
    print("-"*30)

    print(">> CADASTRANDO")
    usuarioCad = input("Digite o nome do usuário: ")
    senhaCad = input("Digite a senha: ")

    print(">> LOGIN")
    usuarioLogin = input("Usuário: ")
    senhaLogin = input("Senha: ")

    if usuarioCad == usuarioLogin and senhaCad == senhaLogin:
        print("BIP BIP BIP, CONTA ACESSADA COM SUCESSO BIP BIP")
    else:
        print("BIP BIP, LOGIN CONSEGUIDO COM FALHA! BIP")

print("| CAIXA DE FERRAMENTAS |")
print("-"*60)

while True:
    print("Escolha uma das opções: ")
    print("1) Escolher uma fruta em uma lista de frutas")
    print("2) Cadastrar e fazer login")
    print("3) Bye bye")

    escolha = input("Digite aqui: ")
    print("-"*30)
    if escolha == "1":
        escolherFruta()
    elif escolha == "2":
        cadastrar()
    elif escolha == "3":
        break
    else:
        print("que")
    print("-"*30)