dicionario = {
    "Quanto é 2 + 2?": 4, 
    "Quanto é 10 + 9?": 19,
    "Quanto é 5 + 12": 17
}


for chave, valor in dicionario.items():
    print("Pergunta:")
    print(chave)
    resposta = int(input("resposta: "))

    if resposta == valor:
        print("Acertou!")
    
    else:
        print("Você errou!")
        break

        
 