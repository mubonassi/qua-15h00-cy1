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