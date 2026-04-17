import os

lista_cadastro = []

while True:
    os.system("cls")
    print(lista_cadastro)

    nome = input("Digite um nome: ")
    idade = int(input("Digite a idade: "))

    dicionario_base = {
        "Nome": nome,
        "Idade": idade,
    }

    if dicionario_base in lista_cadastro:
        print("Pessoa já cadastrada!")
    else:
        lista_cadastro.append(dicionario_base)

    pergunta = input("Quer continuar a cadastrar? ")
    if pergunta not in ["Sim", "sim", "SIM", "s", "Yes", "yes", "Y", "y"]:
        break