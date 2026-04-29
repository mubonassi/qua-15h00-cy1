print("| MANIPULANDO ALUNOS |")
print("-"*30)

listaAlunos = ["Danilo","Mathes","Pedro","Enzo","Henzo","Flavio","Matheus","Mates","Mateus","João","Gustavo"]
print(f"Lista atual de alunos: {listaAlunos}")

print("1) Cadastre 3 novos alunos")
aluno1 = input("Digite o 1º aluno novo: ")
aluno2 = input("Digite o 2º aluno novo: ")
aluno3 = input("Digite o 3º aluno novo: ")

listaAlunos.extend([aluno1,aluno2,aluno3])

print("2) Retire um aluno da lista pelo nome!")
alunoRemove = input("Digite o nome do aluno: ")
listaAlunos.remove(alunoRemove)

print("3) Deseja alterar o nome de um aluno?")
resposta = input("Digite aqui 'sim' ou 'não': ")

if resposta == "sim":
    alunoIndex = int(input("Digite o index do aluno que deseja alterar o nome: "))
    alunoNome = input("Digite o novo nome do aluno: ")
    listaAlunos[alunoIndex] = alunoNome

print(f"Lista Final dos Alunos: {listaAlunos}")