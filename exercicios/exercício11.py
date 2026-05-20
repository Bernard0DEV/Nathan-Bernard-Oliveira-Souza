eventos = []

print("Oque você deseja fazer?")
while True:
    print("1 - Adicionar evento")
    print("2 - remover evento")
    print("3 - Ver eventos")
    print("4 - Sair") 
    resposta = input("Escolha uma opção: ")

    if resposta == "1":
        evento = input("Nome do evento: ")
        dia = input("Dia do evento: ")
        horario = input("Horário do evento: ")
        descricao = input("Descrição do evento: ")
        print("Evento adicionado com sucesso!")
        eventos.append({
            "evento": evento,
            "dia": dia,
            "horario": horario,
            "descricao": descricao
        })

    elif resposta == "2":
        print("Digite o nome do evento que deseja remover")
        event_remove = input("Nome do evento: ")
        eventos = [evento for evento in eventos if evento["evento"] != event_remove]
        print("Evento removido com sucesso!")

    elif resposta == "3":
        print("Eventos:")
        for evento in eventos:
            print(f"Evento: {evento['evento']}, Dia: {evento['dia']}, Horário: {evento['horario']}, Descrição: {evento['descricao']}")

    elif resposta == "4":
        print("Fechando o programa...")
        break
