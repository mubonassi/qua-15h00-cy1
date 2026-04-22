print("| FRUTA FAVORITA |")
print("-"*20)

frutas = ["Maçã","Uva","Pitanga","Pitaya","Maracuja","Morango","Mexirica","Laranja","Abacaxi","Lichia","Manga","Melancia","Amora","Abacate","Tomate","Pera","Banana","Maçã Verde","Blueberry","Framboesa","Cereja","Melão","Mamão","Coco","Jabuticaba","Romã","Limão","Goiaba","Acerola","Caqui","Kiwi","Pessego","Jaca","Guarana","Açaí","Caju"]

print("Selecione sua fruta favorita da lista!")
print(f"Lista de Frutas: {frutas}")

fruta = int(input("Digite a opção: "))

print("--Fruta Selecionada--")
print(f"Favorita: {frutas[fruta]}")