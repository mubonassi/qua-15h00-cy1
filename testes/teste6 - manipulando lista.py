#Manipulando a lista em Python

lista = []

# -- Adicionando itens na lista
#Append -> Adiciona um item no final da lista
item1 = input("Digite um item para colocar na lista: ")
lista.append(item1)
print(lista)
item2 = input("Digite outro item para colocar na lista: ")
lista.append(item2)
print(lista)

#Extend -> Adiciona multiplos itens na lista
item3 = input("Digite outro item para colocar na lista: ")
item4 = input("Digite outro item para colocar na lista: ")
lista.extend([item3,item4])
print(lista)

# -- Removendo itens na lista
#Remove -> Remove o item pelo VALOR
remove1 = input("Digite qual item deseja deletar: ")
lista.remove(remove1)
print(lista)

#Pop -> Remove o item pelo INDEX
remove2 = int(input("Digite o # do item que deseja remover: "))
lista.pop(remove2)
print(lista)



